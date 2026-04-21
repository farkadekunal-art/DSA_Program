num = int(input("Enter number: "))
temp = num
sum = 0

fact = [1,1,2,6,24,120,720,5040,40320,362880]

while temp > 0:
    rem = temp % 10
    sum = sum + fact[rem]
    temp = temp // 10

if sum == num:
    print("Peterson Number")
else:
    print("Not Peterson Number")