# 1. Create a list with the initial elements: 10, 20, 30, 40
my_list = [10, 20, 30, 40]

# 2. (This step is combined with step 1 for conciseness)

# 3. Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)

# 4. Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# 5. Remove the last element from my_list
my_list.pop()

# 6. Sort my_list in ascending order
my_list.sort()

# 7. Find and print the index of the value 30 in my_list
# It's good practice to check if the item exists before getting its index
# to avoid a ValueError if 30 wasn't in the list.
if 30 in my_list:
    index_30 = my_list.index(30)
    print(f"Index of 30: {index_30}")
else:
    print("30 not found in the list.")