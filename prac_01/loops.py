for i in range(1, 21, 2):
    print(i, end=' ')
print()

for j in range(0, 110, 10):
    print(j, end=' ')
print()

for k in range(20, 0, -1):
    print(k, end=' ')
print()

num_stars = int(input("Number of stars: "))
for l in range (0, num_stars):
    print('*', end='')
print()

for m in range (0, num_stars):
    print((m+1) * '*')
print()
