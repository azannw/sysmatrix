import sqlite3
import time

DB_NAME = "data/sysmatrix.db"

def init_db():
    """Initialize the database and create the table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS samples
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp REAL,
                  cpu_percent REAL,
                  memory_percent REAL,
                  disk_percent REAL,
                  uptime_seconds INTEGER)''')
    conn.commit()
    conn.close()

def save_sample(data):
    """Save a dictionary of metrics to the database."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''INSERT INTO samples 
                 (timestamp, cpu_percent, memory_percent, disk_percent, uptime_seconds)
                 VALUES (?, ?, ?, ?, ?)''',
              (data['timestamp'], 
               data['cpu_percent'],
               data['memory_percent'], 
               data['disk_percent'], 
               data['uptime_seconds']))
    conn.commit()
    conn.close()

def fetch_history(limit=10):
    """Fetch the last N records from the database."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM samples ORDER BY timestamp DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()
    return rows
