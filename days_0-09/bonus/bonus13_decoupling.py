print("----------Decoupling-----------")
feet_inches = "5 10" #input("Enter feet and inches: ")

def parse(feetinches):
    part = feetinches.split(" ")
    feet = float(part[0])
    inches = float(part[1])
    return feet, inches  # Retornar una tupla con los valores de pies y pulgadas


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    # print(f"{feet} feet and {inches} inches is equal to: \n{meters} meters.")
    return meters

feet_inches_tuple = parse(feet_inches)
print("fi", feet_inches_tuple)
result = convert(feet_inches_tuple[0], feet_inches_tuple[1])

if result < 1:
    print("Kid is to small.")
else:
    print("Kid can us it.")

print("----------------------------")

def get_nr_items(user_input):
    items = user_input.split(",")
    items = len(items)
    return items

user_input = "Hola, como, estas, ?"
print(get_nr_items(user_input))

print("----------------------------")


def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)

