# app/db.py

import sqlite3

DB_FILE = "contracts.db"

def init_db():aa
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS contracts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            summary TEXT,
            clauses TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_analysis(filename, summary, clauses_json):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO contracts (filename, summary, clauses) VALUES (?, ?, ?)",
              (filename, summary, clauses_json))
    conn.commit()
    conn.close()

def get_all_contracts():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT id, filename, summary, clauses FROM contracts")
    rows = c.fetchall()
    conn.close()
    return rows
