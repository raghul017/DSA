#Hashing for lowercase letters only
#If we know all characters are lowercase English letters (a–z), there are 26 possible characters.
#So, we can use a list of size 26 — one slot for each letter.

s = "apple"

hash_table = [0] * 26

for ch in s:
    index = ord(ch) - ord('a')
    hash_table[index] += 1
    
# query 
q = int(input("Enter the number of query : "))

for _ in range(q):
    character = input("Enter the character : ")
    print(hash_table[ord(character) - ord('a')])