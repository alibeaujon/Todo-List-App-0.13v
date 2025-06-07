""print("-------Bonus:Strong Password---------")

password = input("Enter new Password (8 to 16 characters): ")
result = {}
if len(password) >= 8 and len(password) <= 16:
    result["Lenght"] = True
else:
    result["Lenght"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["Digit"] = True

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["Upper-case"] = True

print(result)

if all(result.values()): # Chequea el valor del diccionario
    print('Strong Password')
else:
    print('Weak Password')

print("----------Bug-Fixing Exercises---------")

ids = ["XF345_89", "XER_76849", "XA454_55"]
x = 0

for id in ids:
    if '_' in id:
        x = x + 1
print(x)

print("----------2---------")

ids = ["XF345_89", "XER76849", "XA454_55"]
x = 0

for id in ids:
    if '_' in id:
        x = x + 1
print(x)




