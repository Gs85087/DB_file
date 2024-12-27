import sqlite3

def query_database(db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    print("Projects Data:")
    # Query all data from the 'projects' table
    cursor.execute("SELECT * FROM projects")
    projects_data = cursor.fetchall()
    for project in projects_data:
        print(project)
    
    print("\nTasks Data:")
    # Query all data from the 'tasks' table
    cursor.execute("SELECT * FROM tasks")
    tasks_data = cursor.fetchall()
    for task in tasks_data:
        print(task)
    
    # Close the database connection
    conn.close()

# Usage example
db_path = 'realistic_db.db'
query_database(db_path)