import sqlite3
from database.connection import get_connection

def salvar(short_url, original_link, expires_datetime):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO urls (short_url, original_url, expires_at) VALUES (?, ?, ?)",
            (short_url, original_link, expires_datetime)
        )
        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()

def url_exist(code):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT 1 FROM urls WHERE short_url = (?)",
        (code,)
    )

    exist = cur.fetchone() is not None

    conn.close()
    return exist

def get_original_url(code):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT original_url, expires_at FROM urls WHERE short_url = (?)",
        (code,)
    )

    row = cur.fetchone()
    conn.close()

    if not row:
        return None

    return row["original_url"]

