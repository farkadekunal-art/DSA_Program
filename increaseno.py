n = int(input("Enter number: "))

for i in range(1, n + 1):
    print(i)
# Increase Number Pattern

rows = 100

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  