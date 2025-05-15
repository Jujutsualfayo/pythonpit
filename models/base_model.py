import uuid
from datetime import datetime

class BaseModel:
   """Initialise the base model and create unique timestamps"""
   def __init__(self):
      self.id = uuid.uuid4()
      self.created_at = datetime.now()
      self.updated_at = self.created_at

      """return the f string representation of the class"""
      def __str__(self):
         return f"[{self.__class.__name__}] ({self.id}) {self.__dict__}"

      """updates the public instance attribute updated_at with the current datetime"""
      def save(self):
         self.updated_at = datetime.now()

         """returns a dictionary containing all keys/values of __dict__ of the instance"""
      def to_dict(self):
         result = self.__dict__.copy()
         result["created_at"] = self.created_at.isoformat()
      
    