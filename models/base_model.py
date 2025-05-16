import uuid
from datetime import datetime
class BaseModel:
    '''init and create unique id and timestamps for the func'''
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    '''create an f str formation of the my BaseModel'''
    def __str__(self):
        
   




      
    