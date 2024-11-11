import datetime

class Task:
    def __init__ (self, name, description, status):
        self.name = name
        self.description = description
        self.status = "To Do"
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def updata_task(self, new_name):
        self.name = new_name
        self.update_time()
        
    def update_time(self):
        self.updated_at = datetime.now()
        
    def mark_as_started(self):
        self.status = "In Progress"
        
    def mark_as_completed(self):
        self.status = "Done"
    
    
    
        
    
        
        