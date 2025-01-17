# goal_manager.py
from file_manager import read_file, write_file


def add_goal(description, target_amount):
    goals = read_file(file_path="goals.json")
    goal = {
        "id": len(goals) + 1,
        "description": description,
        "target_amount": float(target_amount),
        "progress": 0
    }
    goals.append(goal)
    write_file(goals, file_path="goals.json")
    print(f"Goal added: {goal}")
    return goal


def view_goals():
    goals = read_file(file_path="goals.json")
    for goal in goals:
        print(f"ID: {goal['id']}\nDescription: {goal['description']}\nTarget Amount: ${goal['target_amount']:.2f}\nProgress: ${goal['progress']:.2f}\n")
    return goals

def update_goal_progress(goal_id, amount):
    goals = read_file(file_path="goals.json")
    for goal in goals:
        if goal["id"] == goal_id:
            goal["progress"] += float(amount)
            write_file(goals, file_path="goals.json")
            print(f"Updated goal progress: {goal}")
            return goal
    print("Goal not found.")
    return None
