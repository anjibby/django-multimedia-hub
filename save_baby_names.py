import re
import psycopg2

DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "anjibby",
    "host": "localhost",
    "port": "5432"
}

def save_baby_names():
    with open("baby2008.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    pattern = r"<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>"
    matches = re.findall(pattern, html_content)

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS baby_names (
            id SERIAL PRIMARY KEY,
            rank INT NOT NULL,
            boy_name VARCHAR(50) NOT NULL,
            girl_name VARCHAR(50) NOT NULL
        );
    """)
    conn.commit()

    records = [(int(rank), boy, girl) for rank, boy, girl in matches]
    cur.executemany("INSERT INTO baby_names (rank, boy_name, girl_name) VALUES (%s, %s, %s);", records)
    conn.commit()

    print(f"Successfully saved {len(records)} baby name entries to PostgreSQL table 'baby_names'!")

    cur.close()
    conn.close()

if __name__ == "__main__":
    save_baby_names()