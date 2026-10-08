"""
anomaly_detection.py — starter Isolation Forest for logon anomaly detection.

Learning scaffold for Project 6. Export authentication logs from your SIEM
(Project 5) to a CSV, adapt the feature engineering to your columns, and run:

    python -I anomaly_detection.py logons.csv

Expected input: a CSV with at least these columns (rename to match yours):
    timestamp, account, source_ip, outcome   # outcome in {success, failure}

This flags statistically unusual logon events. It is a teaching example,
not a production detector — tune features and contamination to your data.
"""

import sys
import pandas as pd
from sklearn.ensemble import IsolationForest


def load_and_featurize(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["timestamp"])

    # --- Feature engineering -------------------------------------------------
    df["hour"] = df["timestamp"].dt.hour
    df["dayofweek"] = df["timestamp"].dt.dayofweek
    df["is_failure"] = (df["outcome"].str.lower() == "failure").astype(int)

    # Encode categoricals as numeric codes (simple approach for a starter).
    df["account_code"] = df["account"].astype("category").cat.codes
    df["source_ip_code"] = df["source_ip"].astype("category").cat.codes

    # Failures per account in a rolling TIME window hint at brute force.
    # A rolling window (not a cumulative sum) keeps the feature bounded so it
    # doesn't just grow with time and dominate the model.
    df = df.sort_values("timestamp")
    df["acct_fail_10min"] = (
        df.set_index("timestamp")
          .groupby("account")["is_failure"]
          .rolling("10min").sum()
          .reset_index(level=0, drop=True)
          .values
    )

    return df


FEATURES = [
    "hour",
    "dayofweek",
    "is_failure",
    "account_code",
    "source_ip_code",
    "acct_fail_10min",
]


def detect(df: pd.DataFrame) -> pd.DataFrame:
    model = IsolationForest(
        n_estimators=200,
        contamination=0.02,  # ~2% expected anomalies; tune to your data
        random_state=42,
    )
    df["anomaly_score"] = model.fit_predict(df[FEATURES])
    # IsolationForest: -1 = anomaly, 1 = normal
    df["is_anomaly"] = (df["anomaly_score"] == -1)
    return df


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: python -I anomaly_detection.py <logons.csv>")
        raise SystemExit(1)

    df = load_and_featurize(sys.argv[1])
    df = detect(df)

    anomalies = df[df["is_anomaly"]]
    print(f"Total events: {len(df)}")
    print(f"Flagged anomalies: {len(anomalies)}")
    print("\nTop flagged events:")
    cols = ["timestamp", "account", "source_ip", "outcome"]
    print(anomalies[cols].head(20).to_string(index=False))

    out = "anomalies.csv"
    anomalies.to_csv(out, index=False)
    print(f"\nWrote flagged events to {out}")


if __name__ == "__main__":
    main()
