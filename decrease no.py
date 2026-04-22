n = int(input("Enter number: "))

for i in range(n, 0, -1):
    print(i)

rows = 5

for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()