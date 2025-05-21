waiting_list = ["comer", "dormir", "leer"]
waiting_list.sort()

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)
print("\n---------------\n")
waiting_list.sort(reverse=True)

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)
print("\n---------------\nBug-Fixing Exercises\n-------1-------")
menu = ["pasta", "pizza", "salad"]

user_choice = int(input("Enter the index of the item: "))

message = f"You chose {menu[user_choice]}."
print(message)

print("\n-------2-------\n")
menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print(f"{i}.{j}")
print("\n-------3-------\n")
menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print(f"{i}.{j}")