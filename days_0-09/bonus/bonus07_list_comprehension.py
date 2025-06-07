print("----------Bug-Fixing Exercises---------")

temperatures = [10, 12, 14]
temperatures = [ str(temp) + "\n" for temp in temperatures]
file = open("files/bonus07.txt", 'w')
file.writelines(temperatures)

print("----------2---------")

numbers = [10.1, 12.3, 14.7]
numbers = [int(number) for number in numbers]
print(numbers)