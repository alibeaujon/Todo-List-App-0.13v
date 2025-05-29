def read_todos(filepath): #Parameter
    # The program reads: filepath='todos.txt'
    # Read the file and return the list of tasks
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath): #Parameters
    # Write the list of tasks to the file
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

def get_todos(): # No parameter
    # Read and display the list of tasks
    todos_local = read_todos(filepath='todos.txt')
    for index, item in enumerate(todos_local):
        row = f"{index + 1}-{item}"
        row = row.strip()
        print(row)
    print(f"(-{len(todos_local)}-)todos in the list")

while True:
    # Prompt user for action
    user_action = input('Type Add (), Show, Edit (), '
                        'Complete () or eXit: ').lower().strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        # Add a new task
        todo = user_action[4:]
        todos = read_todos(filepath='todos.txt') #Argument=arg value

        todos.append(todo + '\n')

        write_todos(todos, filepath='todos.txt') #Argument=arg value

    elif user_action.startswith("show"):
        # Show the list of tasks
        get_todos()

    elif user_action.startswith("edit"):
        # Edit an existing task
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = read_todos(filepath='todos.txt') #Argument
            print("Current todo that will be replaced is: ", todos[number])
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            write_todos(todos_arg=todos, filepath='todos.txt')  #Arguments
        except ValueError:
            print("Command is not valid")
            continue

    elif user_action.startswith("comp"):
        # Complete and remove a task
        try:
            number = int(user_action[5:])
            todos = read_todos(filepath='todos.txt')
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(number - 1).strip()
            write_todos(todos, filepath='todos.txt')
            get_todos()
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
