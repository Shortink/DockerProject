import psycopg2
import time

def get_db():
    return psycopg2.connect(
        host="localhost",
        database="studentdb",
        user="postgres",
        password="postgres"
    )

def init_db():
    while True:
        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    student_id TEXT PRIMARY KEY,
                    student_name TEXT,
                    course TEXT,
                    present_date TEXT
                );
            """)
            conn.commit()
            cur.close()
            conn.close()
            break
        except Exception as e:
            print("Waiting for DB...", e)
            time.sleep(2)
