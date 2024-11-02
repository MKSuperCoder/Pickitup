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
  
  
class Event:
  def __init__(self, cuny_id, date, club_name, location, start_time, pickup_time, food_item, food_quantity):
    self.cuny_id = cuny_id
    self.date = date
    self.club_name = club_name
    self.location = location 
    self.start_time = start_time
    self.pickup_time = pickup_time
    self.food_item = food_item
    self.food_quantity = food_quantity

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
        'cuny_id': self.cuny_id,
        'date': self.date,
        'club_name':self.club_name,
        'location' : self.location,
        'start_time' : self.start_time,
        'pickup_time' : self.pickup_time,
        'food_item': self.food_item,
        'food_quantity': self.food_quantity
      }