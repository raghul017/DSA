import math
def find_divisors(num):
    divisors = []
    value = math.sqrt(num)
    for i in range (1 , int(value) +1):
        if (num % i==0):
            divisors.append(i)
            if (i !=num//i):
                divisors.append(num//i)
    divisors.sort()
    return divisors

number = int(input("Enter a number: "))
divisors = find_divisors(number)
print("The divisors of", number, "are:", divisors)