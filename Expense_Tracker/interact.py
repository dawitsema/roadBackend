from expense_manager import ExpenseManager


def display_welcome_message():
    print("\n" + "=" * 50)
    print(" Welcome to Expense Tracker CLI Application")
    print(" Manage your expenses with ease and track your financial goals!")
    print("=" * 50)

def display_menu():
    while True:
        print("1. Add an expense")
        print("2. Update an expense")
        print("3. Delete an expense")
        print("4. View all expenses")
        print("5. View a summary of all expenses")
        print("6. View a summary of expenses for a specific month")
        print("7. Add or filter by expense categories")
        print("8. Set and manage monthly budgets")
        print("9. Export expenses to a CSV file")
        choise = input("\nPlease choose an option from the menu above: ")
        if 1 <= int(choise) <= 9:
            return int(choise)
        else:
            print("\nInvalid choice, please make sure to choose from the given option only!!")
    
        
expenseManager = ExpenseManager()
display_welcome_message()
while True:
    ch = display_menu()
    if ch == 1:
        expenseManager.add_expense()
    elif ch == 2:
        expenseManager.update_expense()
    elif ch == 3:
        expenseManager.delete_expenses()
    elif ch == 4:
        expenseManager.show_expenses()
    elif ch == 5:
        expenseManager.view_summary()
    elif ch == 6:
        expenseManager.specific_month_summary()
    elif ch == 7:
        pass
    elif ch == 8:
        pass
    elif ch == 9:
        pass
    
    to_leave = input("Do you want to continue? y/n : ")
    if to_leave.lower() == 'n':
        break
    