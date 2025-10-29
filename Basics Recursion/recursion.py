# # print a name n times using recursion
# def print_name(name ,count):
#     if count ==0:
#         return
#     print(name)
#     print_name(name , count- 1)
# print_name("Alice", 5)

# print("Next problem")

# # print numbers from 1 to n using recursion
# def print_num(i , n):
#     if i> n:
#         return
#     print(i)
#     print_num(i + 1 , n)

# print_num(1 , 5)

# print("Next problem")

# # print in reverse from n to 1 using recursion
# def print_reverse(i , n):
#     if i < n:
#         return
#     print(i)
#     print_reverse(i - 1 , n)
# print_reverse(5 ,1)

# print("Next problem")

# # print from 1 to n using backtracking
# def print_backtrack(i , n):
#     if i < 1:
#         return
#     print_backtrack(i-1 , n)
#     print(i)

# print_backtrack(5 , 5)

# print("Next problem")

# # print from n to 1 using backtracking
# def print_backtrack_reverse(i , n):
#     if(i > n):
#         return
#     print_backtrack_reverse(i + 1 , n)
#     print(i)

# print_backtrack_reverse(1, 5)

# print("NExt problem")

# # print sum of first n numbers
# #1
# def print_sum(i , n, total=0):
#     if(i > n):
#         return total
#     return print_sum(i +1 , n , total + i)
    
# ans = print_sum(1 , 5)
# print(ans)

# #2 parametrized sum
# def print_sum(i , sum ):
#     if(i < 1):
#         return sum
#     return print_sum(i - 1 , sum + i )
# ans = print_sum(6 , 0)
# print(ans)

# functional sum

# def func_sum(n):
#     if n == 0:
#         return 0 
#     return (n + func_sum(n-1))
# print(func_sum(5))