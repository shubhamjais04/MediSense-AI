"""
MediSense AI — SQLite Database Utilities
Stores and retrieves prediction history
"""

import sqlite3, os, datetime
import pandas as pd

BASE    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE, 'medisense_history.db')


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''CREATE TABLE IF NOT EXISTS predictions (
        id            INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp     TEXT,
        symptoms      TEXT,
        top1_disease  TEXT,
        top1_prob     REAL,
        top2_disease  TEXT,
        top2_prob     REAL,
        top3_disease  TEXT,
        top3_prob     REAL,
        severity      REAL,
        risk_level    TEXT,
        duration_days INTEGER,
        frequency     TEXT
    )''')
    conn.commit()
    conn.close()


def save_prediction(selected_symptoms, top3, severity, risk_level, duration_days, frequency):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''INSERT INTO predictions
        (timestamp, symptoms, top1_disease, top1_prob, top2_disease, top2_prob,
         top3_disease, top3_prob, severity, risk_level, duration_days, frequency)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', (
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
        ', '.join(selected_symptoms),
        top3[0]['disease'], top3[0]['probability'],
        top3[1]['disease'] if len(top3) > 1 else '',
        top3[1]['probability'] if len(top3) > 1 else 0.0,
        top3[2]['disease'] if len(top3) > 2 else '',
        top3[2]['probability'] if len(top3) > 2 else 0.0,
        severity, risk_level, duration_days, frequency,
    ))
    conn.commit()
    conn.close()


def get_history(limit=100):
    init_db()
    conn  = sqlite3.connect(DB_PATH)
    df    = pd.read_sql_query(
        f'SELECT * FROM predictions ORDER BY id DESC LIMIT {limit}', conn
    )
    conn.close()
    return df


def get_analytics():
    df = get_history(limit=500)
    if df.empty:
        return None
    return {
        'total':            len(df),
        'top_diseases':     df['top1_disease'].value_counts().head(10).to_dict(),
        'avg_severity':     round(df['severity'].mean(), 2),
        'risk_dist':        df['risk_level'].value_counts().to_dict(),
        'recent':           df.head(5),
    }
