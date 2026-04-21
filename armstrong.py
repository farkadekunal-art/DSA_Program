#  Armstrong Number
num = int(input("Enter number"))
temp = num
sum = 0
while temp > 0:
    rem = temp % 10
    sum = sum + rem**3
    temp = temp // 10
if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")