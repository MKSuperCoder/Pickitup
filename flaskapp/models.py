class User:
  def __init__(self, cuny_id, username, role, created_at):
    self.cuny_id = cuny_id
    self.username = username
    self.role = role
    self.created_at = created_at

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
      'cuny_id':   self.cuny_id,
      'username': self.username,
      'role': self.role,
      'created_at ':self.created_at 
    }
  
  
class FoodItems:
  #Food items with necessary attributes
  def __init__(self, id, item, quantity, pickup_time, time_posted, food_type, pending,
                 event_id, cuny_id, date, club_name, status, location, start_time, end_time):
        # Initialize the food item 
        self.id = id                      # Unique identifier for the food item
        self.item = item                  
        self.quantity = quantity          
        self.pickup_time = pickup_time    
        self.time_posted = time_posted    
        self.food_type = food_type        
        self.pending = pending            
        self.event_id = event_id          
        self.cuny_id = cuny_id           
        self.date = date                 
        self.club_name = club_name        
        self.status = status              
        self.location = location          
        self.start_time = start_time      
        self.end_time = end_time          

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
        # Convert the food item into a dictionary format for JSON responses
        return {
            'id': self.id,
            'item': self.item,
            'quantity': self.quantity,
            'pickup_time': self.pickup_time,
            'time_posted': self.time_posted,
            'food_type': self.food_type,
            'pending': self.pending,
            'event_id': self.event_id,
            'cuny_id': self.cuny_id,
            'date': self.date,
            'club_name': self.club_name,
            'status': self.status,
            'location': self.location,
            'start_time': self.start_time,
            'end_time': self.end_time
        }