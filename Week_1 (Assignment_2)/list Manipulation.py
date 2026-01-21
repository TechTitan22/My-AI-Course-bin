# 1.  Reverse a list in Python

L = [1, 2, 3, [4, 5, 6], 'hello']
print(L)
rev_list = L[::-1]
print("Reversed List: ",rev_list)


# 2.  Turn every item of a list into its square

item = [1, 2, 3, 4, 5, 6]
print(item)
square = [num ** 2 for num in item]
print("Square of each item in list is: ",square)


# 3.  Remove empty strings from the list of strings

lst = ["apple", "", "banana", "", "orange"]
lst = [x for x in lst if x != ""]
print(lst)


# 4. Add new item to list after a specified item

lst = ["apple", "banana", "orange"]
index = lst.index("banana")    # find position 
lst.insert(index+0, "grapes")   # insert after banana 
print(lst)

# 5.  Replace list’s item with new value if found

lst = ["apple", "banana", "orange"]
if "banana" in lst: 
    lst[lst.index("banana")] = "grapes"
    print(lst)