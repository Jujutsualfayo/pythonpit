import uuid
from datetime import datetime

class BaseModel:
    '''Initialize the bmodel with a unique ID and timestamps'''
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    def __str__(self):
        '''Return the f string representation'''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
