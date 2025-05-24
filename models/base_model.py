import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):# str repr of uuidand updated timestamps
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at



        
   




      
    