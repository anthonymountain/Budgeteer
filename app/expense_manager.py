from file_manager import read_file, write_file
from datetime import datetime


def add_expense(description, amount, category, date=None):
    expenses = read_file()
    date = date or datetime.now().strftime("%Y-%m-%d")
    expense = {
        "id": len(expenses) + 1,
        "description": description,
        "amount": float(amount),
        "category": category,
        "date": date
    }
    expenses.append(expense)
    write_file(expenses)
    return expense


def view_expenses():
    expenses = read_file()
    for expense in expenses:
        print(f"ID: {expense['id']}\nDescription: {expense['description']}\nAmount: ${expense['amount']:.2f}\nCategory: {expense['category']}\nDate: {expense['date']}\n")
    return expenses

def delete_expense(expense_id):
    expenses = read_file()
    updated_expenses = [expense for expense in expenses if expense["id"] != expense_id]
    if len(expenses) == len(updated_expenses):
        return False

    for index, expense in enumerate(updated_expenses):
        expense["id"] = index + 1

    write_file(updated_expenses)
    return True


def calculate_total_expenses():
    expenses = read_file()
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Expenses: ${total:.2f}")
    return total


def calculate_expenses_by_category():
    expenses = read_file()
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]

    print("Expenses by Category:")
    for category, total in category_totals.items():
        print(f"  {category}: ${total:.2f}")
    return category_totals


def calculate_average_spending():
    expenses = read_file()
    if not expenses:
        print("No expenses to calculate average.")
        return 0
    average = sum(expense["amount"] for expense in expenses) / len(expenses)
    print(f"Average Spending: ${average:.2f}")
    return average
