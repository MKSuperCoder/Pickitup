from flask import Flask, render_template, request, jsonify
import os, re, datetime
import db
from models import User, Event


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


@app.route('/post_food', methods=['POST'])
def post_food():
    # Endpoint to handle posting of a new food item
    data = request.get_json()  # Get JSON data from the request
    food_item = FoodItem(
        id=None,  # New item, so ID is set to None
        item=data['item'],  # Food item name from request
        quantity=data['quantity'],  # Quantity from request
        pickup_time=data['pickup_time'],  # Pickup time from request
        time_posted=str(datetime.datetime.now()),  # Current timestamp
        food_type=data['food_type'],  # Food type from request
        pending=False,  # Default to not pending when posted
        event_id=data['event_id'],  # Event ID from request
        cuny_id=data['cuny_id'],  # CUNY ID from request
        date=data['date'],  # Date from request
        club_name=data['club_name'],  # Club name from request
        status=data['status'],  # Status from request
        location=data['location'],  # Location from request
        start_time=data['start_time'],  # Start time from request
        end_time=data['end_time']  # End time from request
    )
    db.insert_food(food_item)  # Insert the food item into the database
    return jsonify({'status': '200', 'message': 'Food posted successfully'})  # Return success message

@app.route('/request', methods=['GET'])
def getRequest():
    content_type = request.headers.get('Content-Type')
    bks = [b.serialize() for b in db.view()]
    if (content_type == 'application/json'):
        json = request.json
        for b in bks:
            if b['id'] == int(json['id']):
                return jsonify({
                    # 'error': '',
                    'res': b,
                    'status': '200',
                    'msg': 'Success getting all books in library!👍😀'
                })
        return jsonify({
            'error': f"Error ⛔❌! Book with id '{json['id']}' not found!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
                    # 'error': '',
                    'res': bks,
                    'status': '200',
                    'msg': 'Success getting all books in library!👍😀',
                    'no_of_books': len(bks)
                })


@app.route('/request/<id>', methods=['GET'])
def getRequestId(id):
    req_args = request.view_args
    # print('req_args: ', req_args)
    bks = [b.serialize() for b in db.view()]
    if req_args:
        for b in bks:
            if b['id'] == int(req_args['id']):
                return jsonify({
                    # 'error': '',
                    'res': b,
                    'status': '200',
                    'msg': 'Success getting book by ID!👍😀'
                })
        return jsonify({
            'error': f"Error ⛔❌! Book with id '{req_args['id']}' was not found!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
                    # 'error': '',
                    'res': bks,
                    'status': '200',
                    'msg': 'Success getting book by ID!👍😀',
                    'no_of_books': len(bks)
                })

@app.route("/request", methods=['PUT'])
def putRequest():
    req_data = request.get_json()
    availability = req_data['available']
    title = req_data['title']
    the_id = req_data['id']
    bks = [b.serialize() for b in db.view()]
    for b in bks:
        if b['id'] == the_id:
            bk = Book(
                the_id, 
                availability, 
                title, 
                datetime.datetime.now()
            )
            print('new book: ', bk.serialize())
            db.update(bk)
            new_bks = [b.serialize() for b in db.view()]
            print('books in lib: ', new_bks)
            return jsonify({
                # 'error': '',
                'res': bk.serialize(),
                'status': '200',
                'msg': f'Success updating the book titled {title}!👍😀'
            })        
    return jsonify({
                # 'error': '',
                'res': f'Error ⛔❌! Failed to update Book with title: {title}!',
                'status': '404'
            })
    
    


@app.route('/request/<id>', methods=['DELETE'])
def deleteRequest(id):
    req_args = request.view_args
    print('req_args: ', req_args)
    bks = [b.serialize() for b in db.view()]
    if req_args:
        for b in bks:
            if b['id'] == int(req_args['id']):
                db.delete(b['id'])
                updated_bks = [b.serialize() for b in db.view()]
                print('updated_bks: ', updated_bks)
                return jsonify({
                    'res': updated_bks,
                    'status': '200',
                    'msg': 'Success deleting book by ID!👍😀',
                    'no_of_books': len(updated_bks)
                })
    else:
        return jsonify({
            'error': f"Error ⛔❌! No Book ID sent!",
            'res': '',
            'status': '404'
        })

if __name__ == '__main__':
    app.run()



