import sqlite3, random, datetime
from models import User

DB_FILE="app.db"

def getNewId():
    return random.getrandbits(28)

def connect():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, available BOOLEAN, title TEXT, timestamp TEXT)")
    conn.commit()
    conn.close()

def insert(user):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES (?,?,?,?)", (
        user.cuny_id,
        user.username,
        user.role,
        user.created_at
    ))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM events")
    rows = cur.fetchall()
    events = []
    for i in rows:
        event = Event(i[0], True if i[1] == 1 else False, i[2], i[3])
        events.append(event)
    conn.close()
    return books

def update(book):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("UPDATE books SET available=?, title=? WHERE id=?", (book.available, book.title, book.id))
    conn.commit()
    conn.close()

def delete(theId):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (theId,))
    conn.commit()
    conn.close()

def deleteAll():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("DELETE FROM books")
    conn.commit()
    conn.close()


#Insert Food-Value
def insert_food(food_item):
    # Insert a new food item into the food_items table
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO food_items (
            item, quantity, pickup_time, time_posted, food_type, pending,
            event_id, cuny_id, date, club_name, status, location, start_time, end_time
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        food_item.item,                    # Food item name
        food_item.quantity,                # Quantity of food item
        food_item.pickup_time,            # Pickup time for food
        food_item.time_posted,            # Time item was posted
        food_item.food_type,              # Type of food
        food_item.pending,                 # Pending status
        food_item.event_id,               # Associated event ID
        food_item.cuny_id,                # CUNY ID of the poster
        food_item.date,                   # Associated date
        food_item.club_name,              # Club name
        food_item.status,                  # Status of the food item
        food_item.location,                # Location for pickup
        food_item.start_time,              # Start time of the event
        food_item.end_time                 # End time of the event
    ))
    conn.commit()                        # Commit changes to the database
    conn.close()                         # Close the database connection
