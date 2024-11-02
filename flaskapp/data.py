import sqlite3

# Function to connect to the SQLite database (or create it)
def connect(db_file):
    conn = sqlite3.connect(db_file)
    return conn

# Function to create a table
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            food_item TEXT NOT NULL,
            quantity TEXT NOT NULL,
            cuny_id TEXT NOT NULL,
            date TEXT NOT NULL,
            role TEXT NOT NULL,
            club_name TEXT NOT NULL,
            location TEXT NOT NULL,
            pickup_time TEXT NOT NULL        
        )
    """)
    conn.commit()

# Function to insert data into the users table
def insert_user(conn, food_item, quantity, cuny_id, date, role, club_name, location, pickup_time):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (food_item, quantity, cuny_id, date, role, club_name, location, pickup_time)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (food_item, quantity, cuny_id, date, role, club_name, location, pickup_time))
    conn.commit()

# Function to fetch all users
def fetch_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Main execution
if __name__ == "__main__":
    db_file = "app.db"  # Database file name
    conn = connect(db_file)  # Connect to the database

    create_table(conn)  # Create the table

    # Insert sample data
    insert_user(conn, "Apples", "10", "123456", "2024-11-02", "member", "Fruit Club", "Room 101", "12:00 PM")
    insert_user(conn, "Bananas", "20", "654321", "2024-11-02", "admin", "Fruit Club", "Room 102", "1:00 PM")
    insert_user(conn, "Pizza", "20", "654321", "2024-11-02", "admin", "Coding Club", "Fiterman 102", "1:00 PM")
    insert_user(conn, "Soda", "20", "654321", "2024-11-02", "admin", "Coding Club", "Fiterman 1002", "1:00 PM")

    # Fetch and print all users
    users = fetch_users(conn)
    for user in users:
        print(user)

    conn.close()  # Close the database connection