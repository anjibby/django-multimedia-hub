import psycopg2
from psycopg2 import extras

# Database connection configuration
DB_CONFIG = {
    "dbname": "todo_db",
    "user": "postgres",
    "password": "anjibby",  # Replace with your local PostgreSQL password
    "host": "localhost",
    "port": "5432"
}

def get_connection():
    """Establishes and returns a database connection."""
    return psycopg2.connect(**DB_CONFIG)

def add_task(task_name):
    """CREATE: Adds a new task to the database."""
    query = "INSERT INTO todos (task_name) VALUES (%s) RETURNING id;"
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (task_name,))
                task_id = cur.fetchone()[0]
                conn.commit()
                print(f"✅ Task added successfully with ID: {task_id}")
    except Exception as e:
        print(f"❌ Error adding task: {e}")

def view_tasks():
    """READ: Fetches and displays all tasks."""
    query = "SELECT id, task_name, status, created_at FROM todos ORDER BY id ASC;"
    try:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=extras.DictCursor) as cur:
                cur.execute(query)
                tasks = cur.fetchall()
                
                if not tasks:
                    print("\n--- No tasks found ---")
                    return
                
                print("\n" + "="*50)
                print(f"{'ID':<5} | {'Task Name':<25} | {'Status':<10}")
                print("="*50)
                for task in tasks:
                    print(f"{task['id']:<5} | {task['task_name']:<25} | {task['status']:<10}")
                print("="*50 + "\n")
    except Exception as e:
        print(f"❌ Error fetching tasks: {e}")

def update_task_status(task_id, new_status="Completed"):
    """UPDATE: Updates the status of an existing task."""
    query = "UPDATE todos SET status = %s WHERE id = %s;"
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (new_status, task_id))
                conn.commit()
                if cur.rowcount > 0:
                    print(f"✅ Task ID {task_id} updated to '{new_status}'.")
                else:
                    print(f"⚠️ Task ID {task_id} not found.")
    except Exception as e:
        print(f"❌ Error updating task: {e}")

def delete_task(task_id):
    """DELETE: Removes a task from the database by ID."""
    query = "DELETE FROM todos WHERE id = %s;"
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (task_id,))
                conn.commit()
                if cur.rowcount > 0:
                    print(f"✅ Task ID {task_id} deleted successfully.")
                else:
                    print(f"⚠️ Task ID {task_id} not found.")
    except Exception as e:
        print(f"❌ Error deleting task: {e}")

def main_menu():
    """Interactive CLI interface."""
    while True:
        print("\n=== TO-DO LIST MANAGER ===")
        print("1. View All Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            name = input("Enter task description: ").strip()
            if name:
                add_task(name)
            else:
                print("⚠️ Task description cannot be empty.")
        elif choice == "3":
            try:
                task_id = int(input("Enter Task ID to mark completed: "))
                update_task_status(task_id, "Completed")
            except ValueError:
                print("⚠️ Please enter a valid numerical ID.")
        elif choice == "4":
            try:
                task_id = int(input("Enter Task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("⚠️ Please enter a valid numerical ID.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()