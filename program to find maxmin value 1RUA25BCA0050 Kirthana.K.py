Program to find minmax value of 3 numbers
1RUA25BCA0050 Kirthana.K

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


if a > b and a > c:
    print("Maximum:", a)
elif b > a and b > c:
    print("Maximum:", b)
else:
    print("Maximum:", c)


if a < b and a < c:
    print("Minimum:", a)
elif b < a and b < c:
    print("Minimum:", b)
else:
    print("Minimum:", c)
