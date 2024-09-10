# TO DO LIST APP
todo_list = []
while True:
    print("___ WELCOME TO THE TO_DO APP___")
    print("Choose a option...")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Mark task as completed")
    print("4. List tasks")
    print("5. Exit")

    option = int(input("Enter the option of your choice: "))

    if option == 1:
        opt = input("Enter the task: ")
        todo_list.append({"Task":opt, "Completed": False})

    elif option == 2:
        opt = int(input("Enter the task to remove: "))
        todo_list.pop(opt-1)

    elif option == 3:
        opt = int(input("Enter the task to mark as completed: "))
        todo_list[opt-1]["Completed"] = True

    elif option == 4:
        for index,i in enumerate(todo_list, start = 1):
            print(index, i)

    elif option == 5:
        break

    else:
        print("invalid number")

print(todo_list)