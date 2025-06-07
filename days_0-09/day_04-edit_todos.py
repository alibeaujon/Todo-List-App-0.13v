todos = ["comer", "dormir", "caminar"]

while True:
    user_action = input('Type add, show, edit or exit: ')
    user_action = user_action.lower()
    user_action = user_action.strip() #elimina los saltos de linea


    match user_action:
            case 'add':
                todo = input('Enter a todo: ')
                todos.append(todo)
            case "show" | "display":
                for index, item in enumerate(todos):
                    index_plus = index + 1
                    item = item.title()
                    print(index_plus, '-', item)
            case "edit":
                number = int(input("Number of todo to edit: "))
                number = number - 1
                print("Current todo that will be replaced is: ", todos[number])
                new_todo = input("Enter new todo: ")
                todos[number] = new_todo
                print(new_todo)
            case "exit":
                break


print('Bye!')
