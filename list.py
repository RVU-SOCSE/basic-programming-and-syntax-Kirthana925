my_list = [25, 9, 43, 77, 50, "Kirthana", "Koushik", "Shalini", "Sujan", "Prathishka"]

print("Original List:")
print(my_list)

my_list.append("Prashanth")
print("\nAfter append():")
print(my_list)

my_list.insert(2, 25)
print("\nAfter insert():")
print(my_list)

my_list.extend([60, 70])
print("\nAfter extend():")
print(my_list)

my_list.remove(77)
print("\nAfter remove():")
print(my_list)

my_list.pop(3)
print("\nAfter pop():")
print(my_list)

print("\nIndex of 'Kirthana':", my_list.index("Kirthana"))

print("Count of 9:", my_list.count(9))

num_list = [25, 9, 43, 77, 5]
num_list.sort()
print("\nAfter sort():", num_list)

num_list.reverse()
print("After reverse():", num_list)

copied_list = my_list.copy()
print("\nCopied List:")
print(copied_list)

temp_list = [1, 2, 3]
temp_list.clear()
print("\nAfter clear():", temp_list)
