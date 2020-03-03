a = [9, 2, 3, 4, 6, 7]

print(a[2:4])
print(len(a))

b = range(6)
for i in b:
    print(i)

for i in range(len(a)):
    """
    len(a) return 6 and range will return 0 - 5
    i will iterate from 0 - 5
    """
    print(a[i])

a.sort()
print(a)

b = []
print("empty list: ", b)

for j in range(10):
    b.append(j)

print("List after appending", b)

# Tuple
# Python Tuple is used to store the sequence of immutable python objects.
# Tuple is similar to lists since the value of the items stored in the list
# can be changed whereas the tuple is immutable and the value of the items
# stored in the tuple can not be changed.

# Set
# The set in python can be defined as the unordered collection of various items
# enclosed within the curly braces. The elements of the set can not be duplicate.
# The elements of the python set must be immutable.
# Unlike other collections in python, there is no index attached to the elements
# of the set, i.e., we cannot directly access any element of the set by the index.
# However, we can print them all together or we can get the list of elements by looping
# through the set.
set1 = {"Ayush","John", "David", "Martin"}
set2 = {"Steave","Milan","David", "Martin"}
print(set1.intersection(set2))  # prints the intersection of the two sets

# Dictionary
# Dictionary is used to implement the key-value pair in python. The dictionary
# is the data type in python which can simulate the real-life data arrangement
# where some specific value exists for some particular key.
# In other words, we can say that a dictionary is the collection of key-value pairs
# where the value can be any python object whereas the keys are the immutable python
# object, i.e., Numbers, string or tuple.
# Dictionary simulates Java hash-map in python.
Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE"}
dict1 = {k: v for k, v in Employee.items()}
print(dict1)
print("After Update")
print(dict1)

# Let's create a dictionary, the functional way


class Dictionary(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value


obj = Dictionary()
obj.add("name", "Sid")
obj.add("Mandu", "Aish")

print(obj)