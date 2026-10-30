tasks = []

def show_tasks():
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

while True:
    print("\n===== TO-DO LIST APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()

        if tasks:
            try:
                task_number = int(input("Enter the task number to delete: "))

                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Deleted task: {removed_task}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Exiting To-Do List App. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")