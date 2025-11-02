#Every character on your keyboard (letters, digits, punctuation, spaces, etc.) has a numeric ASCII code between 0 and 255.

#Example
# A → 65
# a → 97
# 0 → 48
# (space) → 32
# ! → 33

# So instead of worrying about uppercase/lowercase separately,
# we can directly use the ASCII number as the index of our hash table.

n = input("Enter the string : ")

hash_table = [0] * 256

for ch in n:
    hash_table[ord(ch)] +=1

#query
q= int(input("Enter the number of queries : "))
for _ in range(q):
    char = input("Enter the char  : ")[0]
    print(hash_table[ord(char)])