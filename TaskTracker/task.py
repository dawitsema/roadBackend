from datetime import datetime
class Task:
    id_counter = 1
    def __init__ (self, description):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.description = description
        self.status = "To Do"
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def update_desciption(self, description):
        self.description = description
        self.updated_at = self.update_time()
        
    def update_time(self):
        self.updated_at = datetime.now()
        
    
    def mark_as_completed(self):
        self.status = "Done"
        
    def to_json(self):
        return {"id": self.id, "description": self.description, "status": self.status, "created_at": self.created_at.isoformat(), "updated_at": self.updated_at.isoformat()}
    
    
    
    
    
        
    
        
        