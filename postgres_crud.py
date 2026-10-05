import psycopg2

DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "anjibby",
    "host": "localhost",
    "port": "5432"
}

def main():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # Create Table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        );
    """)
    conn.commit()
    print("Table 'users' created successfully.")

    # INSERT (Create)
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) ON CONFLICT DO NOTHING;", ("Ogunjobi Anjola", "anjola@example.com"))
    conn.commit()

    # SELECT (Read)
    cur.execute("SELECT * FROM users;")
    print("READ Users:", cur.fetchall())

    # UPDATE
    cur.execute("UPDATE users SET email = %s WHERE name = %s;", ("anjola_updated@example.com", "Ogunjobi Anjola"))
    conn.commit()

    # DELETE
    cur.execute("DELETE FROM users WHERE name = %s;", ("Ogunjobi Anjola",))
    conn.commit()
    print("CRUD Operations completed successfully!")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()