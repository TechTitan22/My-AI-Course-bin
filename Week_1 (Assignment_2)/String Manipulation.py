# 1. Write a program to create a new string made of an input string’s first, 
# middle, and last character.

User_input = input("Enter a String: ")
first = User_input[0]
middle = User_input[len(User_input) // 2]
last = User_input[-1]

new_string = first + middle + last
print("New String: ",new_string)


# 2. Write a program to count occurrences of all characters within a string Given. 

char_count = {}         # dictionary to store counts 

for ch in User_input: 
    if ch in char_count: 
        char_count[ch] += 1
    else: 
        char_count[ch] = 1

for ch, count in char_count.items():
    print(ch, ":", count)


# 3. Reverse a given string 
rev_str = User_input[::-1]
print("Reversed String: ",rev_str)


# 4. Split a string on hyphens
split_string = User_input.split('-')
print(split_string)


# 5. Remove special symbols / punctuation from a string

result = ""

for ch in User_input:
    if ch.isalnum() or ch == " ":
        result += ch

print(result)