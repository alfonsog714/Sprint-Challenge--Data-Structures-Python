import time
from binary_search_tree import BinarySearchTree

"""
Navigate into the names directory. Here you will find two text files containing 10,000 names each, along with a program names.py that compares the two files and prints out duplicate name entries. Try running the code with python3 names.py. Be patient because it might take a while: approximately six seconds on my laptop. What is the runtime complexity of this code?

Six seconds is an eternity so you've been tasked with speeding up the code. Can you get the runtime to under a second? Under one hundredth of a second?

You may NOT use the built in Python list or set for this problem

(Hint: You might try importing a data structure you built during the week)
"""

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = []
# duplicates = set(names_1) & set(names_2)

tree = BinarySearchTree(names_1[0])
for name in names_1[1:]:
    tree.insert(name)

for name in names_2:
    if tree.contains(name):
        duplicates.append(name)

# O(n^2)
# for name_1 in names_1: # O(n) because the run complexity depends on the amount of names inputted
#     for name_2 in names_2: # O(n) because the run complexity depends on the amount of names inputted, same as above
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

