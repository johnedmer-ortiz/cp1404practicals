"""
CP1404 - prac_03 - files
"""

name = input("Enter name: ")
file_name = name + ".txt"
out_file = open(file_name, "w")
print(f"{name}", file=out_file)
out_file.close()
