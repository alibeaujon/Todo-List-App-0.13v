filenames = ['1.Raw Data.txt', '2.Reports.txt', '3.Repreentation.txt']

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    """('.' old, '-' nuevo, 1 iteraciones)"""
    print(filename)


print("/ / / / / / / / ")

elements = ['a', 'b', 'c']

print(elements[1])

print("/ / / / / / / / ")

elements = ['a', 'b', 'c']
elements[1] = "x"
print(elements)

