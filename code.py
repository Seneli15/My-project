def add(x, y):
    return x + y
print("1. Add")
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(f"Result: {add(num1, num2)}")
elif choice == '2':
    print(f"Result: {subtract(num1, num2)}")
elif choice == '3':
    print(f"Result: {multiply(num1, num2)}")
elif choice == '4':
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid input!")

def modulus(x, y):
    return x % y

print("5. Modulus")


def mark_task_done(tasks):
    """Mark a task as completed."""
    print("\nMarking a task as done...")
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num] = tasks[task_num] + " ✅"
            save_tasks(tasks)
            print(f"Task '{tasks[task_num]}' marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Add this option to the menu
while True:
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")  # New Feature
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_tasks(tasks)
    elif choice == '2':
        add_task(tasks)
    elif choice == '3':
        remove_task(tasks)
    elif choice == '4':  # New Feature
        mark_task_done(tasks)
    elif choice == '5':
        print("\nExiting... Goodbye!")
        break
    else:
        print("\nInvalid choice! Please try again.")


choice = input("Enter choice (1/2/3/4/5): ")

if choice == '5':
    print(f"Result: {modulus(num1, num2)}")

