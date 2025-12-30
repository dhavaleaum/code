
n = int(input("Enter number of elements: "))
s = set()

digits = lower = upper = 0

for i in range(n):
    val = input("Enter element: ")
    s.add(val)

for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.islower():
        lower += 1
    elif ch.isupper():
        upper += 1

print("Set:", s)
print("Length:", len(s))
print("Digits:", digits)
print("Lowercase:", lower)
print("Uppercase:", upper)
