
d1 = {"Kirthana": 98, "Koushik": 99}
d2 = {"Padmavathi": 98, "Uday": 99}


d1.update(d2)
print("After using update():")
print(d1)


d1 = {"Kirthana": 98, "Koushik": 99}
d2 = {"Padmavathi": 98, "Uday": 99}


d3 = d1 | d2
print("\nAfter using | operator:")
print(d3)
