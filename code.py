# Step 1: Define functions for to-do list operations

def load_tasks():
    """Load tasks from a file."""
    print("\nLoading tasks from file...")
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        print("No previous tasks found. Starting fresh!")
        return []


def save_tasks(tasks):
    """Save tasks to a file."""
    print("\nSaving tasks to file...")
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved successfully!")

