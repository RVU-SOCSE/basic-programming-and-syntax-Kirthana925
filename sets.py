# Creating two sets
set1 = {26, 25, 18, 10, "Kirthana", "Koushik"}
set2 = {18, 10, "Padmavathi", "Uday", "Priya"}

print("Set 1:", set1)
print("Set 2:", set2)

# 1. add() – Adds one element
set1.add("Vignesh")
print("\nAfter add():", set1)

# 2. update() – Adds multiple elements
set1.update([50, "Kirthana"])
print("After update():", set1)

# 3. remove() – Removes element (error if not found)
set1.remove(25)
print("After remove():", set1)

# 4. discard() – Removes element (no error if not found)
set1.discard(100)
print("After discard():", set1)

# 5. pop() – Removes random element
set1.pop()
print("After pop():", set1)

# 6. clear() – Removes all elements (using temp set)
temp_set = {1, 2, 3}
temp_set.clear()
print("After clear():", temp_set)

# 7. copy() – Copies a set
copy_set = set2.copy()
print("\nCopy of Set2:", copy_set)

# 8. union()
print("\nUnion:", set1.union(set2))

# 9. intersection()
print("Intersection:", set1.intersection(set2))

# 10. difference()
print("Difference (set1 - set2):", set1.difference(set2))

# 11. symmetric_difference()
print("Symmetric Difference:", set1.symmetric_difference(set2))

# 12. issubset()
print("\nIs set1 subset of set2?:", set1.issubset(set2))

# 13. issuperset()
print("Is set1 superset of set2?:", set1.issuperset(set2))

# 14. isdisjoint()
print("Are sets disjoint?:", set1.isdisjoint(set2))

# 15. intersection_update()
set3 = {26, 18, 10}
set4 = {18, 10, 5}
set3.intersection_update(set4)
print("\nAfter intersection_update():", set3)

# 16. difference_update()
set5 = {26, 25, 18}
set6 = {18}
set5.difference_update(set6)
print("After difference_update():", set5)

# 17. symmetric_difference_update()
set7 = {1, 2, 3}
set8 = {3, 4, 5}
set7.symmetric_difference_update(set8)
print("After symmetric_difference_update():", set7)
