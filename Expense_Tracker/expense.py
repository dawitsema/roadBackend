from datetime import datetime

class Expense:
    def __init__(self, id, description, amount) -> None:
        self.id = id
        self.description = description
        self.amount = amount
        self.created_at = datetime.now(None).isoformat()
        
    def to_json(self):
        return {'id': self.id, "description": self.description, "amount": self.amount, "created_at": self.created_at}
        
    
        
        
        
    
    