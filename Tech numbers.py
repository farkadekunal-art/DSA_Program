num = int(input("Enter number: "))

s = str(num)
if len(s) % 2 == 0:
    mid = len(s) // 2
    first = int(s[:mid])
    second = int(s[mid:])

    total = first + second

    if total * total == num:
        print("Tech Number")
    else:
        print("Not Tech Number")
else:
    print("Not Tech Number")