def is_armstrong_number(num):
    val = num
    sum = 0 
    while num >0:
        digit = num%10
        sum = sum + (digit ** len(str((val))))
        num = num // 10
    return sum == val

number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")