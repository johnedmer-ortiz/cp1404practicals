"""
CP1404 - prac_03 - files
"""

name = input("Enter name: ")
out_file = name + ".txt"
out_file = open(out_file, "w")
print(f"{name}", file=out_file)
out_file.close()
