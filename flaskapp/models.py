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
    def __init__(self, event_id, cuny_id, date, club_name, status, location, start_time, end_time):
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
      return {
        'event_id': self.event_id,
        'cuny_id': self.cuny_id,
        'date': self.date,
        'club_name':self.club_name,
        'status' : self.status,
        'location' : self.location,
        'start_time' : self.start_time,
        'end_time' : self.end_time,
      }