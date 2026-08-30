import sqlite3

def get_connection():
    conn = sqlite3.connect("berry_broker.db")
    return conn

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            username TEXT,
            balance INTEGER DEFAULT 100,
            last_daily TEXT,
            last_rob TEXT
        )
    """)
    conn.commit()
    conn.close()

def get_user(user_id, username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()

    if user is None:
        cursor.execute(
            "INSERT INTO users (user_id, username, balance, last_daily, last_rob) VALUES (?, ?, 100, NULL, NULL)",
            (user_id, username)
        )
        conn.commit()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        user = cursor.fetchone()
    else:
        cursor.execute("UPDATE users SET username = ? WHERE user_id = ?", (username, user_id))
        conn.commit()

    conn.close()
    return user

def update_balance(user_id, new_balance):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET balance = ? WHERE user_id = ?", (new_balance, user_id))
    conn.commit()
    conn.close()

def update_last_daily(user_id, timestamp):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET last_daily = ? WHERE user_id = ?", (timestamp, user_id))
    conn.commit()
    conn.close()

def update_last_rob(user_id, timestamp):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET last_rob = ? WHERE user_id = ?", (timestamp, user_id))
    conn.commit()
    conn.close()

def get_top_users(limit=5):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username, balance FROM users ORDER BY balance DESC LIMIT ?", (limit,))
    results = cursor.fetchall()
    conn.close()
    return results
