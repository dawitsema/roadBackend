import datetime

class Task:
    id_counter = 1
    def __init__ (self, description):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.description = description
        self.status = "To Do"
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        
    def mark_as_started(self):
        self.status = "In Progress"
        
    def mark_as_completed(self):
        self.status = "Done"
    
    
    
        
    
        
        