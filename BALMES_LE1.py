#Lab Exam Extension
budgets = {}
expenses = []
saving_goals = {}
currency_symbol = '$'

def main_menu():
    print("\nFinance Manager Console App")
    print("A. Set Budget")
    print("B. Add Expense")
    print("C. Set Savings Goal ")
    print("D. View Financial Summary")
    print("E. Settings")
    print("F. Exit")

def budget_planner():
    print("\nBudget Planner")
    category = input("Enter category name (e.g, groceries): ")
    if not category:
        print("Category already exists. Do you want to update the budget? (Y/N): ")
        choice = input().strip().upper()
        if choice != 'Y':
            return
    amount = input("Enter budget amount: ")
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return
    budgets[category] = amount
    print("Budget set successfully.")

def expense_tracker():
    print ("\nExpense Tracker")
    if not budgets:
        print("Please set a budget first.")
        return
    print("Categories:")
    for category in budgets.keys():
        print(category)
    category = input("Enter expense category: ")
    if category not in budgets:
        print("Category not found.")
        return
    amount = input("Enter expense amount: ")
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return
    expenses.append((category, amount))
    print("Expense added successfully.")

def saving_goals_menu():
    global saving_goals  # Add this line if saving_goals is a global variable
    print("\nSavings Goals")
    goal = input("Enter savings goal (e.g, vacation): ")
    if not goal:
        print("Goal name cannot be empty.")
        return
    if goal in saving_goals:
        print("Goal already exists. Do you want to update the goal? (Y/N): ")
        choice = input().strip().upper()
        if choice != 'Y':
            return
    target_amount = input("Enter target amount: ")
    try:
        target_amount = float(target_amount)
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return
    saving_goals[goal] = target_amount

    print("Savings goal set successfully.")

def generate_reports():
    print("\nFinancial Summary")
    if not budgets:
        print("Please set a budget first.")
        return
    total_income = sum(budgets.values())
    total_expenses = sum(expense[1] for expense in expenses)
    total_savings = sum(saving_goals.values())

    print(f"Total Income: {currency_symbol}{total_income}")
    print(f"Total Expenses: {currency_symbol}{total_expenses}")
    print(f"Total Savings Goal: {currency_symbol}{total_savings}")
    net_income = total_income - total_expenses
    print(f"Net Income: {currency_symbol}{net_income}")
    if net_income >= total_savings:
        print("Congratulations! You've achieved your savings goal.")
    else:
        remaining_savings = total_savings - net_income
        print(f"You need to save {currency_symbol}{remaining_savings} more to reach your goal.")

def settings():
    global currency_symbol
    print("\nSettings")
    new_symbol = input("Enter new currency symbol (e.g, $, €, £): ").strip()
    if new_symbol:
        currency_symbol = new_symbol
        print("Currency symbol updates successfully.")
    else:
        print("Currency symbol cannot be empty.")

def exit_program():
    print("Exiting...")

def view_budgets():
    print("\nBudgets")
    if not budgets:
        print("No budgets set yet.")
        return
    for category, amount in budgets.items():
        print(f"{category}: {currency_symbol}{amount}")

def view_expenses():
    print("\nExpenses")
    if not expenses:
        print("No expenses recorded yet.")
        return
    for category, amount in expenses:
        print(f"{category}: {currency_symbol}{amount}")

def view_saving_goals():
    print("\nSavings Goals")
    if not saving_goals:
        print("No savings goals set yet.")
        return
    for goal, target_amount in saving_goals.items():
        print(f"{goal}: {currency_symbol}{target_amount}")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice (A-I): ").strip().upper()

        if choice == 'A':
            budget_planner()
        elif choice == 'B':
            expense_tracker()
        elif choice == 'C':
            saving_goals_menu()
        elif choice == 'D':
            generate_reports()
        elif choice == 'E':
            settings()
        elif choice == 'F':
            exit_program()
        elif choice == 'G':
            view_budgets()
        elif choice == 'H':
            view_expenses()
        elif choice == 'I':
            view_saving_goals()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




