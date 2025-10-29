# print a name n times using recursion
def print_name(name ,count):
    if count ==0:
        return
    print(name)
    print_name(name , count- 1)

# print numbers from 1 to n using recursion
def print_num(i , n):
    if i> n:
        return
    print(i)
    print_num(i + 1 , n)

print_name("Alice", 5)
print_num(1 , 5)

# print in reverse from n to 1 using recursion
def print_reverse(i , n):
    if i < n:
        return
    print(i)
    print_reverse(i - 1 , n)
print_reverse(5 ,1)
