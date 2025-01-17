from expense_manager import (add_expense, view_expenses, delete_expense,
                             calculate_total_expenses,
                             calculate_expenses_by_category,
                             calculate_average_spending)
from goal_manager import add_goal, view_goals, update_goal_progress
from subscription_manager import (add_subscription, view_subscriptions,
                                  delete_subscription,
                                  calculate_total_subscription_cost)


def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Calculate Total Expenses")
        print("5. Calculate Expense By Category")
        print("6. Calculate Average Spending")
        print("7. Add Goal")
        print("8. View Goals")
        print("9. Update a Goal")
        print("10. Add Subscription")
        print("11. View Subscriptions")
        print("12. Delete Subscription")
        print("13. Calculate Total Subscription Cost")
        print("14. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD) [Leave blank for today]: ")
            expense = add_expense(description, amount, category, date)
            print(f"Expense added: {expense}")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            expense_id = int(input("Enter expense ID to delete: "))
            if delete_expense(expense_id):
                print("Expense deleted successfully.")
            else:
                print("Expense not found.")
        elif choice == "4":
            calculate_total_expenses()
        elif choice == "5":
            calculate_expenses_by_category()
        elif choice == "6":
            calculate_average_spending()
        elif choice == "7":
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            add_goal(description, amount)
        elif choice == "8":
            view_goals()
        elif choice == "9":
            goal_id = int(input("Enter goal ID to update: "))
            amount = int(input("Enter amount contributed towards goal: "))
            update_goal_progress(goal_id, amount)
        elif choice == "10":
            name = input("Enter name of bill or subscription: ")
            cost = input("Enter cost per cycle: ")
            cycle = input("Enter type of billing cycle (Monthly, Yearly): ")
            date = input("Enter start date (YYYY-MM-DD) "
                         "[Leave blank for today]: ")
            add_subscription(name, cost, cycle, date)
        elif choice == "11":
            view_subscriptions()
        elif choice == "12":
            sub_id = int(input("Enter subscription ID to delete: "))
            delete_subscription(sub_id)
        elif choice == "13":
            calculate_total_subscription_cost()
        elif choice == "14":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
