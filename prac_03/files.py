"""
CP1404 - prac_03 - files
"""

name = input("Enter name: ")
out_file = open("name.txt", "w")
print(f"{name}", file=out_file)
out_file.close()

out_file = open("name.txt", "r")
print(f"Your name is {out_file.readline()}")
out_file.close()