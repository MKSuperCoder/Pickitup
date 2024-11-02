from flask import Flask, render_template, request, jsonify
import os, re, datetime
import db
from models import Event


app = Flask(__name__)

# create the database and table. Insert 10 test books into db
# Do this only once to avoid inserting the test books into 
# the db multiple times
if not os.path.isfile('app.db'):
    db.connect()

# route for landing page
# check out the template folder for the index.html file
# check out the static folder for css and js files
@app.route("/")
def index():
    return render_template("index.html")

def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
      return True
    else:
      return False



food_items = []
@app.route('/event', methods=['POST'])
def post_food():
    data = request.get_json()
    
    # Validate the incoming data
    if not data or 'foodItem' not in data or 'quantity' not in data or 'pickupTime' not in data:
        return jsonify({"error": "Invalid data"}), 400

    # Extract the data
    # event_id = data["cun"]
    cuny_id = data["cunyId"]
    date = data["date"]
    club_name = data["clubName"]
    location = data["location"] 
    start_time = data["startTime"]
    end_time = data["pickupTime"]
    food_item = data["foodItem"]
    food_quantity = data["quantity"]
    
    # Create a food entry
    event = Event(cuny_id=cuny_id,
         date = date,
         club_name = club_name, 
         location = location, 
         start_time = start_time, 
         end_time = end_time, 
         food_item = food_item, 
         food_quantity = food_quantity )
    db.insert(event)
    return render_template('index.html')
    #return jsonify({"message": "Food posted successfully!", "data": event}), 201
    
    
if __name__ ==  '__main__':
    app.run()