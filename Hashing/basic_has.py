n = int(input())

#take arr elements 
arr = list(map(int , input("Enter the numbers").split()))

#precompute frequencies using a list (like hash table)
hash_table = [0] * 13

for num in arr:
    hash_table[num] +=1

# take number of queries
q = int(input("Enter the number of queries"))

#ans each query
for _ in range(q):
    number = int(input("Enter the number to check : "))
    print("Count : ", hash_table[number])