"""try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    if width == length:
        exit("That looks like a square.")

    area = width * length
    print(area)

except ValueError:
    print("Enter a number.")
"""
try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print(f"{name} is not in the list")