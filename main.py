def read_file():
    # Read the file and return the list of tasks
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
def write_file(todos_local):
    # Write the list of tasks to the file
    with open('todos.txt', 'w') as file_local:
        file_local.writelines(todos_local)
def show_list():
    # Read and display the list of tasks
    todos_local = read_file()
    for index, item in enumerate(todos_local):
        row = f"{index + 1}-{item}"
        row = row.strip()
        print(row)
    print(f"--({len(todos_local)})todos in the list")



while True:
    # Prompt user for action
    user_action = input('Type Add (), Show, Edit (), '
                        'Complete () or eXit: ').lower().strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        # Add a new task
        todo = user_action[4:]
        todos = read_file()

        todos.append(todo + '\n')

        write_file(todos)

    elif user_action.startswith("show"):
        # Show the list of tasks
        show_list()

    elif user_action.startswith("edit"):
        # Edit an existing task
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = read_file()
            print("Current todo that will be replaced is: ", todos[number])
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            write_file(todos)
        except ValueError:
            print("Command is not valid")
            continue

    elif user_action.startswith("comp"):
        # Complete and remove a task
        try:
            number = int(user_action[5:])
            todos = read_file()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(number - 1).strip()
            write_file(todos)
            show_list()
            print(f'Todo "{todo_to_remove}" has been completed and removed from the list.')
        except IndexError:
            print("Command is not valid")
            continue
        except ValueError:
            print("Command is not valid")
            continue

    elif user_action.startswith("exit"):
        # Exit the program
        break

    else:
        # Invalid command
        print("Command is not valid")

print('Bye!')
