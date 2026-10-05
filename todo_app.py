import psycopg2

DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "anjibby",
    "host": "localhost",
    "port": "5432"
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def init_db():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS todos (
                    id SERIAL PRIMARY KEY,
                    task TEXT NOT NULL,
                    status VARCHAR(20) DEFAULT 'Pending'
                );
            """)

def add_task(task):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO todos (task) VALUES (%s);", (task,))

def view_tasks():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, task, status FROM todos ORDER BY id ASC;")
            return cur.fetchall()

def main():
    init_db()
    add_task("Finish Python Assignment")
    print("Tasks in Database:")
    for task in view_tasks():
        print(task)

if __name__ == "__main__":
    main()