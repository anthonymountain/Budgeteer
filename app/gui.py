import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from expense_manager import add_expense, view_expenses, delete_expense
from goal_manager import add_goal, view_goals, update_goal_progress
import matplotlib.pyplot as plt
from subscription_manager import add_subscription, view_subscriptions, \
    delete_subscription

# Main
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("800x600")

nav_frame = tk.Frame(root)
nav_frame.pack(side=tk.TOP, fill=tk.X)
content_frame = tk.Frame(root)
content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


# Navigation
def show_home():
    for widget in content_frame.winfo_children():
        widget.destroy()
    tk.Label(content_frame, text="Welcome to Budgeteer!",
             font=("Arial", 18)).pack(pady=20)
    tk.Label(content_frame,
             text="Use the navigation buttons above to manage your expenses, "
                  "goals, and subscriptions.",
             wraplength=600, justify="center").pack(pady=10)


def show_expense_manager():
    for widget in content_frame.winfo_children():
        widget.destroy()

    tk.Label(content_frame, text="Manage Expenses", font=("Arial", 16)).pack(
        pady=10)

    # Add Expense Form
    form_frame = tk.Frame(content_frame)
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Description:").grid(row=0, column=0, padx=5,
                                                   pady=5)
    description_entry = tk.Entry(form_frame)
    description_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Amount:").grid(row=1, column=0, padx=5, pady=5)
    amount_entry = tk.Entry(form_frame)
    amount_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Category:").grid(row=2, column=0, padx=5, pady=5)
    category_entry = tk.Entry(form_frame)
    category_entry.grid(row=2, column=1, padx=5, pady=5)

    (tk.Button(form_frame, text="Add Expense",
               command=lambda: add_expense_handler(description_entry,
                                                   amount_entry,
                                                   category_entry))
     .grid(row=3, column=0, columnspan=2, pady=10))

    # Expense List
    expense_list = ttk.Treeview(content_frame, columns=("ID", "Description",
                                                        "Amount", "Category",
                                                        "Date"),
                                show="headings")
    expense_list.heading("ID", text="ID")
    expense_list.heading("Description", text="Description")
    expense_list.heading("Amount", text="Amount")
    expense_list.heading("Category", text="Category")
    expense_list.heading("Date", text="Date")
    expense_list.pack(pady=10, fill=tk.BOTH, expand=True)

    load_expenses(expense_list)

    # Delete Expense
    tk.Button(content_frame, text="Delete Selected",
              command=lambda: delete_expense_handler(expense_list)).pack(pady=5)

    tk.Button(content_frame, text="Show Chart",
              command=show_expense_chart).pack(pady=5)


def show_goal_manager():
    for widget in content_frame.winfo_children():
        widget.destroy()

    (tk.Label(content_frame, text="Manage Goals", font=("Arial", 16))
     .pack(pady=10))

    # Add Goal Form
    form_frame = tk.Frame(content_frame)
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Description:").grid(row=0, column=0, padx=5,
                                                   pady=5)
    description_entry = tk.Entry(form_frame)
    description_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Target Amount:").grid(row=1, column=0, padx=5,
                                                     pady=5)
    target_entry = tk.Entry(form_frame)
    target_entry.grid(row=1, column=1, padx=5, pady=5)

    (tk.Button(form_frame, text="Add Goal",
               command=lambda: add_goal_handler(description_entry,
                                                target_entry))
     .grid(row=2, column=0, columnspan=2, pady=10))

    # Goal List
    goal_list = ttk.Treeview(content_frame, columns=("ID", "Description",
                                                     "Target", "Progress"),
                             show="headings")
    goal_list.heading("ID", text="ID")
    goal_list.heading("Description", text="Description")
    goal_list.heading("Target", text="Target Amount")
    goal_list.heading("Progress", text="Progress")
    goal_list.pack(pady=10, fill=tk.BOTH, expand=True)

    load_goals(goal_list)

    tk.Button(content_frame, text="Update Selected",
              command=lambda: update_goal_handler(goal_list)).pack(pady=5)


def show_subscription_manager():
    for widget in content_frame.winfo_children():
        widget.destroy()

    (tk.Label(content_frame, text="Manage Subscriptions", font=("Arial", 16))
     .pack(pady=10))

    # Add Subscription Form
    form_frame = tk.Frame(content_frame)
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(form_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Cost:").grid(row=1, column=0, padx=5,
                                            pady=5)
    cost_entry = tk.Entry(form_frame)
    cost_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Billing Cycle:").grid(row=2, column=0, padx=5,
                                                     pady=5)
    cycle_entry = tk.Entry(form_frame)
    cycle_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Start Date:").grid(row=3, column=0, padx=5,
                                                  pady=5)
    start_date_entry = tk.Entry(form_frame)
    start_date_entry.grid(row=3, column=1, padx=5, pady=5)

    (tk.Button(form_frame, text="Add Subscription",
               command=lambda: add_subscription_handler(name_entry, cost_entry,
                                                        cycle_entry,
                                                        start_date_entry))
     .grid(row=4, column=0, columnspan=2, pady=10))

    # Subscription List
    subscription_list = ttk.Treeview(content_frame, columns=("ID", "Name",
                                                             "Cost", "Cycle",
                                                             "Start Date"),
                                     show="headings")
    subscription_list.heading("ID", text="ID")
    subscription_list.heading("Name", text="Name")
    subscription_list.heading("Cost", text="Cost")
    subscription_list.heading("Cycle", text="Billing Cycle")
    subscription_list.heading("Start Date", text="Start Date")
    subscription_list.pack(pady=10, fill=tk.BOTH, expand=True)

    load_subscriptions(subscription_list)

    (tk.Button(content_frame, text="Delete Selected",
               command=lambda: delete_subscription_handler(subscription_list))
     .pack(pady=5))

    tk.Button(content_frame, text="Calculate Recurring Expenses",
              command=calculate_recurring_expenses).pack(pady=5)


def add_expense_handler(description_entry, amount_entry, category_entry):
    description = description_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()

    if not description or not amount or not category:
        messagebox.showerror("Error", "All fields are required.")
        return

    try:
        add_expense(description, float(amount), category)
        messagebox.showinfo("Success", "Expense added successfully.")
        description_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        show_expense_manager()
    except ValueError:
        messagebox.showerror("Error", "Invalid amount entered.")


def load_expenses(treeview):
    treeview.delete(*treeview.get_children())
    expenses = view_expenses()
    for expense in expenses:
        treeview.insert("", "end", values=(
            expense["id"],
            expense["description"],
            f"${expense['amount']:.2f}",
            expense["category"],
            expense["date"]
        ))


def delete_expense_handler(treeview):
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showerror("Error", "No expense selected.")
        return

    expense_id = int(treeview.item(selected_item, "values")[0])
    if delete_expense(expense_id):
        messagebox.showinfo("Success", "Expense deleted successfully.")
        show_expense_manager()
    else:
        messagebox.showerror("Error", "Failed to delete expense.")


def show_expense_chart():
    expenses = view_expenses()
    if not expenses:
        messagebox.showinfo("No Data",
                            "No expenses available to display a chart.")
        return

    # Calculate totals by category
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        category_totals[category] = (category_totals.get(category, 0) +
                                     expense["amount"])

    # Prepare data for the chart
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    # Create the bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(categories, amounts, color='skyblue')
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.tight_layout()

    # Show the chart
    plt.show()


def add_goal_handler(description_entry, target_entry):
    description = description_entry.get()
    target_amount = target_entry.get()

    if not description or not target_amount:
        messagebox.showerror("Error", "All fields are required.")
        return

    try:
        add_goal(description, float(target_amount))
        messagebox.showinfo("Success", "Goal added successfully.")
        description_entry.delete(0, tk.END)
        target_entry.delete(0, tk.END)
        show_goal_manager()
    except ValueError:
        messagebox.showerror("Error", "Invalid target amount entered.")


def load_goals(treeview):
    treeview.delete(*treeview.get_children())
    goals = view_goals()
    for goal in goals:
        treeview.insert("", "end", values=(
            goal["id"],
            goal["description"],
            f"${goal['target_amount']:.2f}",
            f"${goal['progress']:.2f}"
        ))


def update_goal_handler(treeview):
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showerror("Error", "No goal selected.")
        return

    goal_id = int(treeview.item(selected_item, "values")[0])

    # Prompt the user for the amount to update
    new_progress = tk.simpledialog.askfloat("Update Goal Progress",
                                            "Enter the amount to add to the "
                                            "progress:")
    if new_progress is None:
        return  # User canceled the dialog

    if new_progress < 0:
        messagebox.showerror("Error", "Progress amount cannot be negative.")
        return

    # Update the goal progress
    if update_goal_progress(goal_id, new_progress):
        messagebox.showinfo("Success", "Goal updated successfully.")
        show_goal_manager()
    else:
        messagebox.showerror("Error", "Failed to update goal.")


def add_subscription_handler(name_entry, cost_entry, cycle_entry,
                             start_date_entry):
    name = name_entry.get()
    cost = cost_entry.get()
    cycle = cycle_entry.get()
    start_date = start_date_entry.get()

    if not name or not cost or not cycle or not start_date:
        messagebox.showerror("Error", "All fields are required.")
        return

    try:
        add_subscription(name, float(cost), cycle, start_date)
        messagebox.showinfo("Success", "Subscription added successfully.")
        name_entry.delete(0, tk.END)
        cost_entry.delete(0, tk.END)
        cycle_entry.delete(0, tk.END)
        start_date_entry.delete(0, tk.END)
        show_subscription_manager()
    except ValueError:
        messagebox.showerror("Error", "Invalid cost entered.")


def load_subscriptions(treeview):
    treeview.delete(*treeview.get_children())
    subscriptions = view_subscriptions()
    for subscription in subscriptions:
        treeview.insert("", "end", values=(
            subscription["id"],
            subscription["name"],
            f"${subscription['cost']:.2f}",
            subscription["billing_cycle"],
            subscription["start_date"]
        ))


def delete_subscription_handler(treeview):
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showerror("Error", "No subscription selected.")
        return

    subscription_id = int(treeview.item(selected_item, "values")[0])
    if delete_subscription(subscription_id):
        messagebox.showinfo("Success", "Subscription deleted successfully.")
        show_subscription_manager()
    else:
        messagebox.showerror("Error", "Failed to delete subscription.")


def calculate_recurring_expenses():
    subscriptions = view_subscriptions()
    monthly_total = 0
    yearly_total = 0

    for sub in subscriptions:
        if sub["billing_cycle"].lower() == "monthly":
            monthly_total += sub["cost"]
            yearly_total += sub["cost"] * 12
        elif sub["billing_cycle"].lower() == "yearly":
            yearly_total += sub["cost"]

    messagebox.showinfo(
        "Recurring Expenses",
        f"Total Monthly Cost: ${monthly_total:.2f}\nTotal Yearly Cost: "
        f"${yearly_total:.2f}"
    )


# Buttons
home_button = tk.Button(nav_frame, text="Home", command=show_home)
home_button.pack(side=tk.LEFT, padx=10, pady=10)

expense_button = tk.Button(nav_frame, text="Manage Expenses",
                           command=show_expense_manager)
expense_button.pack(side=tk.LEFT, padx=10, pady=10)

goal_button = tk.Button(nav_frame, text="Manage Goals",
                        command=show_goal_manager)
goal_button.pack(side=tk.LEFT, padx=10, pady=10)

subscription_button = tk.Button(nav_frame, text="Manage Subscriptions",
                                command=show_subscription_manager)
subscription_button.pack(side=tk.LEFT, padx=10, pady=10)

show_home()

root.mainloop()
