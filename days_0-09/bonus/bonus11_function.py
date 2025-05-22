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