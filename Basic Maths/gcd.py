
# method 1

def gcd(a, b):
    ans = 1
    for i in range(1 , min(a,b)+1):
        if(a%i==0 and b%i==0):
            ans = i
    return ans
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
value  = gcd(num1, num2)
print("The GCD is:", value)

# method 2 euclid's algorithm

def gcd_euclid(a, b):
    if b == 0:
        return a
    if a < b:
        return gcd_euclid(b, a)
    return gcd_euclid(b, a % b)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
value  = gcd_euclid(num1, num2)
print("The GCD is:", value)


# optimized method

def gcd_optimized(a, b):
    while b != 0:
        a, b = b, a % b
    return a
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
value  = gcd_optimized(num1, num2)
print("The GCD is:", value)