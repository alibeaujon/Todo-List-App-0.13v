while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.lower()
    user_action = user_action.strip() #elimina los saltos de linea

    match user_action:
            case 'add' | "a":
                todo = input('Enter a todo: ') + "\n"

                file = open('../todos.txt', 'r') #w=write, r=read
                todos = file.readlines() #NO readline...s
                file.close()

                todos.append(todo)

                file = open('../todos.txt', 'w') #w=write, r=read
                file.writelines(todos)
                file.close()
            case "show" | "display" | "s":
                file = open('../todos.txt', 'r')  # w=write, r=read
                todos = file.readlines()  # NO readline...s
                file.close()

                '''new_todos = []
                for item in todos:
                    new_item = item.strip("\n")
                    new_todos.append(new_item)'''

                # Comprehension
                new_todos = [item.strip("\n") for item in todos] #Comprehension

                for index, item in enumerate(new_todos):
                    item = item.strip("\n")
                    row = f"{index + 1}-/-{item}"
                    print(row)
                    "print(index_plus, '-', item)"
                print(f"The lenght is: {len(todos)}")
            case "edit" | "e":
                file = open('../todos.txt', 'r')  # w=write, r=read
                todos = file.readlines()  # NO readline...s
                file.close()

                number = int(input("Number of todo to edit: "))
                number = number - 1
                print("Current todo that will be replaced is: ", todos[number])
                new_todo = input("Enter new todo: ")
                todos[number] = new_todo
                print(new_todo)
            case "complete" | "c":
                file = open('../todos.txt', 'r')  # w=write, r=read
                todos = file.readlines()  # NO readline...s
                file.close()

                number = int(input('Number of the todo to compete: '))
                todos.pop(number - 1)
            case "exit" | "x":
                break


print('Bye!')
