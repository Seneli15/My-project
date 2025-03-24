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


def remove_task(tasks):
    """Remove a task by its number."""
    print("\nRemoving a task...")
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")



# Step 2: Load existing tasks
print("Initializing To-Do List...")
tasks = load_tasks()


# Step 3: Provide user options
while True:
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_tasks(tasks)
    elif choice == '2':
        add_task(tasks)
    elif choice == '3':
        remove_task(tasks)
    elif choice == '4':
        print("\nExiting... Goodbye!")
        break
    else:
        print("\nInvalid choice! Please try again.")


