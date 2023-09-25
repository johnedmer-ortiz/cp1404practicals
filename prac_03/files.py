"""
CP1404 - prac_03 - files
"""

name = input("Enter name: ")
out_file = open("name.txt", "w")
print(f"{name}", file=out_file)
out_file.close()

in_file = open("name.txt", "r")
print(f"Your name is {in_file.readline()}")
in_file.close()

in_file = open("numbers.txt", "r")
#print(f"{int(out_file.readline()) + int(out_file.readline())}")
result = 0
for i in range(2):
    result = result + int(in_file.readline())
print(result)
in_file.close()

in_file = open("numbers.txt", "r")
result = 0
for line in in_file:
    result = int(line) + result
print(result)
in_file.close()