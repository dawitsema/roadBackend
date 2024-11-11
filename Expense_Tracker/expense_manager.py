from expense import Expense
import json
from datetime import datetime


class ExpenseManager:
    def add_expense(self):
        description = input('what is the description of expense? description : ')
        amount = int(input('what is the amount of expense? amount : '))
        try:
            with open('expenses.json', 'r') as file:
                expenses = json.load(file)
        except FileNotFoundError:
            print("File not found. Creating a new file.")
            expenses = {}
            
        while True:
            id = input('what is the id of expense? id: ')
            if id not in expenses:
                expense = Expense(id, description, amount)
                expenses[id] = expense.to_json()
                break
            else:
                print(f'{id} exist in your data so you can\'t use it twice. please give me legit id.')
                
        with open("expenses.json", 'w') as file:
            json.dump(expenses, file, indent=2)
            
        print("Expense add to your file!")
        
        
        
    def update_expense(self):
        self.show_expenses()
        try:
            with open("expenses.json", 'r') as file:
                expenses = json.load(file)
            id = input('which expense do you want to edit? id : ')
            name = input('description: ')
            amount = input('amount: ')
            
            expenses[id]['description'] = name
            expenses[id]['amount'] = amount
            
            with open("expenses.json", 'w') as file:
                json.dump(expenses, file, indent=2)
                
        except Exception as e:
            print(f'An error occured {e}')
        
        
        
    def delete_expenses(self):
        self.show_expenses()
        try:
            with open("expenses.json", 'r') as file:
                expenses = json.load(file)
            id = input('which expense do you want to delete? id : ')
            del expenses[id]
            with open("expenses.json", 'w') as file:
                json.dump(expenses, file, indent=2)
                
        except Exception as e:
            print(f'An error occured {e}')
        
        
        
    def show_expenses(self):
        try:
            with open('expenses.json', 'r') as file:
                expenses = json.load(file)
            print("\n" + "=" * 50)
            print("\nId\t\tCreated At\t\tDescription\t\tPrice(Amount)")
            for expense in expenses.values():
                print(f"{expense['id']}\t\t{expense['created_at']}\t\t{expense['description']}\t\t{expense['amount']}")
            print("\n" + "=" * 50)
        except Exception as e:
            print(f'An error occured: {e}')
            
            
            
    def view_summary(self):
        try:
            with open('expenses.json', 'r') as file:
                expenses = json.load(file)
            
            total_sum = 0
            for expense in expenses.values():
                total_sum += int(expense['amount'])
            
            print(f'The Total Expenses : ${total_sum}')
        except Exception as e:
            print(f'An error occured {e}')
            

    def specific_month_summary(self):
        try: 
            with open('expenses.json', 'r') as file:
                expenses = json.load(file)
                
            months = input("which months data do you want? month(1 - 12): ")
            total_sum = 0
            for expense in expenses.values():
                if datetime.strptime(expense['created_at'], '%Y-%m-%d').month == months:
                    total_sum += int(expense['amount'])
                    
            print(f'The Total Expenses of month {months}: ${total_sum}')

        except Exception as e:
            print(f'An error occured {e}')
            