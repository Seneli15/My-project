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


def display_tasks(tasks):
    """Display the current tasks."""
    print("\nDisplaying current tasks...")
    if not tasks:
        print("No tasks available!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")



def add_task(tasks):
    """Add a new task."""
    print("\nAdding a new task...")
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added successfully!")

