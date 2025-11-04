#Hashing for lowercase letters only
#If we know all characters are lowercase English letters (a–z), there are 26 possible characters.
#So, we can use a list of size 26 — one slot for each letter.

s = "apple"

# create hash array of size 26 (all zeros)
hash_table = [0] * 26

# precompute
for ch in s:
    index = ord(ch) - ord('a')
    hash_table[index] += 1
# Explanation:
	# •	ord(ch) gives you the ASCII value of the character.
	# •	Subtracting ord('a') maps 'a' to 0, 'b' to 1, … 'z' to 25.
	# •	Each time you see a letter, you increase its count.

# query 
q = int(input("Enter the number of query : "))

for _ in range(q):
    character = input("Enter the character : ")
    print(hash_table[ord(character) - ord('a')])


