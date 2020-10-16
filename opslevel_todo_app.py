from todo import Todo

quit = False

my_todo_list = Todo()

while not quit:
    print("Enter your next action. The options are as follow:")
    print("""
    ADD - add a new task to the to-do list
    DELETE - delete an existing task in the to-do list
    VIEW - view all items in the to-do list with their priorities
    PRIORITIES - view the competing priorities
    QUIT - quit this application
    """)
    action = input()

    if action.upper() == "ADD":
        todo_text = input("\nEnter the to-do you would like to add: ")
        todo_priority = input("\nEnter the priority of the task (1 being the highest priority): ")
        result = my_todo_list.add_item(todo_text, todo_priority)
        print(result)

    elif action.upper() == "DELETE":
        todo_text = input("\nEnter the to-do you would like to delete: ")
        result = my_todo_list.delete_item(todo_text)
        print(result)

    elif action.upper() == "VIEW":
        current_todos = my_todo_list.get_todo_list()
        print("Priority" + "\t\t" + "Task")
        for task, priority  in sorted(current_todos.items()):
            print(priority + "\t\t" + task)

    elif action.upper() == "PRIORITIES":
        repeated_priorities = my_todo_list.get_repeat_priorities()
        print("Competing Priorities:")
        for priority, tasks in repeated_priorities.items():
            print("Priority:", priority, "\t", "# of Tasks:", len(tasks))
            for task in tasks: print(task)

    elif action.upper() == "QUIT":
        quit = True
        print("Quitting the to-do list application. Have a nice day.")

    else:
        print("Invalid input. Please try again.")
    print("\n")