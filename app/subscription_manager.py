from file_manager import read_file, write_file
from datetime import datetime


def add_subscription(name, cost, billing_cycle, start_date):
    subscriptions = read_file(file_path="subscriptions.json")
    start_date = start_date or datetime.now().strftime("%Y-%m-%d")
    subscription = {
        "id": len(subscriptions) + 1,
        "name": name,
        "cost": float(cost),
        "billing_cycle": billing_cycle,  # e.g., "monthly", "yearly"
        "start_date": start_date  # e.g., "2025-01-16"
    }
    subscriptions.append(subscription)
    write_file(subscriptions, file_path="subscriptions.json")
    print(f"Subscription added: {subscription}")
    return subscription


def view_subscriptions():
    subscriptions = read_file(file_path="subscriptions.json")
    for subscription in subscriptions:
        print(f"ID: {subscription['id']}\nName: {subscription['name']}\nCost: ${subscription['cost']:.2f}\nBilling Cycle: {subscription['billing_cycle']}\nStart Date: {subscription['start_date']}\n")


def delete_subscription(subscription_id):
    subscriptions = read_file(file_path="subscriptions.json")
    updated_subscriptions = [sub for sub in subscriptions if sub["id"] != subscription_id]
    if len(subscriptions) == len(updated_subscriptions):
        print("Subscription not found.")
        return False

    # Reassign IDs after deletion
    for index, subscription in enumerate(updated_subscriptions):
        subscription["id"] = index + 1

    write_file(updated_subscriptions, file_path="subscriptions.json")
    print("Subscription deleted successfully.")
    return True


def calculate_total_subscription_cost():
    subscriptions = read_file(file_path="subscriptions.json")
    total = sum(sub["cost"] for sub in subscriptions)
    print(f"Total Subscription Cost: ${total:.2f} per billing cycle.")
    return total
