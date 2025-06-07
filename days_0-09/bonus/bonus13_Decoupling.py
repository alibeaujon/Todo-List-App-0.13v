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
