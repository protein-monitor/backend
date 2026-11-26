import psycopg

from app.config import DATABASE_URL


def get_conn():
    return psycopg.connect(DATABASE_URL)

def check_database():
    with get_conn() as conn:
        conn.execute("SELECT 1")
