#Para crear un archivo por primera vez, pero no se puede sobre escribir.

contents = ["111131111", "222222222", "333333333"]
filenames = ["doc1.txt", "doc2.txt", "doc3.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", "w")
    file.write(content)
    file.close()

print("----------Coding Exercise: Adding to Text File---------")

member = "Solomon Right"

file = open("files/members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open("files/members.txt", 'w')
existing_members = file.writelines(existing_members)
file.close()

print("----------2---------")

contents1 = ["Hello", "Hello", "Hello"]
filenames1 = ['doc.txt', 'report.txt', 'presentation.txt']

for content1, filename1 in zip(contents1, filenames1):
    file2 = open(f"files/{filename1}", "w")
    file2.write(content1)
    file2.close()

print("---66.Coding Exercise: Reading Multiple Files------")

filenames3 = ["a.txt", "b.txt", "c.txt"]

for filename3 in filenames3:
    file3 = open(f"files/{filename3}", 'r')
    filename33 = file3.read()
    print(filename33)

print("-----67.Bug-Fixing Exercises------")
file4 = open("files/data.txt", 'w')

file4.write("100.121" + "\n")
file4.write("111.23" + "\n")
file4.close()

print("-----67.Bug-Fixing Exercises_2------")

file5 = open("files/data1.txt", 'w')
file5.write("100.12")
file5.close()
