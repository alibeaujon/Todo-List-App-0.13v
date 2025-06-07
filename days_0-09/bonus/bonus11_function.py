print("----------Decopling-----------")
feet_inches = "5 10" #input("Enter feet and inches: ")

def convert(feet_inches):
    part = feet_inches.split(" ")
    feet = float(part[0])
    inches = float(part[1])

    meters = feet * 0.3048 + inches * 0.0254
    # print(f"{feet} feet and {inches} inches is equal to: \n{meters} meters.")
    return meters


print(convert(feet_inches))
result = convert(feet_inches)

if result < 1:
    print("Kid is to small.")
else:
    print("Kid can us it.")

print("----------------------------")
def greet(message):
    new_message = message.capitalize()
    print("hey Hey")
    return new_message

greeting = greet('hi') #Here defines the value

print(greeting)

new_greet = "hello"
greeting = greet(new_greet) #Here defines the value

print(greeting)


print("----------------------------")
def get_average():
    with open("files/data_11.txt", "r") as file:
        data = file.readlines()

    values = data[1:8]
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)
    return average_local

average = get_average()
average = round(average, 2)
print(average)

print("----------------------------")

def get_maximum():
    celsius_local = [14, 15.1, 12.3]
    maximum = max(celsius_local)
    return maximum


celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32

print(fahrenheit)