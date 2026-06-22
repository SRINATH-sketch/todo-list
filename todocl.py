tasks = []

while True:
    print("\n----- TO DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter Task: ")
        tasks.append(task)
        print("Task Added")

    elif choice == 2:
        if len(tasks) == 0:
            print("No Tasks Available")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == 3:
        if len(tasks) == 0:
            print("No Tasks Available")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            pos = int(input("Enter task number to delete: "))
            tasks.pop(pos - 1)
            print("Task Deleted")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")