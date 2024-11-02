import sqlite3, random, datetime
from models import Event

DB_FILE="app.db"

def getNewId():
    return random.getrandbits(28)

def connect():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, available BOOLEAN, title TEXT, timestamp TEXT)")
    conn.commit()
    conn.close()

def insert(event):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("INSERT INTO event VALUES (?,?,?,?)", (
        event.date,
        event.club_name,
        event.location,
        event.cuny_id,
        event.start_time,
        event.end_time,
        event.food_item,
        event.food_quantity
        
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
    return events

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