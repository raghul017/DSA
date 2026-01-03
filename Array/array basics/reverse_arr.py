# s = "A man, a plan, a canal: Panama"
# l , r = 0 , len(s) -1
# is_palindome = True

# while l < r:
#     while l < r and not s[l].isalnum():
#         l +=1
#     while l < r and not s[r].isalnum():
#         r -=1
#     if s[l].lower() != s[r].lower():
#         is_palindome = False
#         break
#     l+=1
#     r-=1


# print(is_palindome)

def sortedSquares(nums):
    for i in range(len(nums)):
        nums[i] = (nums[i]**2)
    return nums.sort()

print(sortedSquares([-4,-1,0,3,10]))