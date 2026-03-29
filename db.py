import sqlite3
from config import DB_PATH

def connect():
    return sqlite3.connect(DB_PATH)

def init(conn):
    conn.executescript('''
        CREATE TABLE IF NOT EXISTS inventory (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            data        TEXT,
            pavadinimas TEXT,
            kiekis      REAL,
            vnt         TEXT,
            kaina       REAL
        );
        CREATE TABLE IF NOT EXISTS products (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT UNIQUE,
            count INTEGER DEFAULT 1
        );
    ''')
    conn.commit()

def save(conn, items, date=None):
    from datetime import datetime
    date = date or datetime.now().strftime('%Y-%m-%d')
    for item in items:
        conn.execute(
            'INSERT INTO inventory (data, pavadinimas, kiekis, vnt, kaina) VALUES (?,?,?,?,?)',
            (date, item['name'], item['quantity'], item['unit'], item['price'])
        )
        conn.execute(
            'INSERT INTO products (name) VALUES (?) ON CONFLICT(name) DO UPDATE SET count = count + 1',
            (item['name'],)
        )
    conn.commit()

def known_names(conn, min_count=2):
    return [r[0] for r in conn.execute(
        'SELECT name FROM products WHERE count >= ? ORDER BY count DESC',
        (min_count,)
    ).fetchall()]

def all_names(conn):
    return [r[0] for r in conn.execute(
        'SELECT DISTINCT pavadinimas FROM inventory'
    ).fetchall()]