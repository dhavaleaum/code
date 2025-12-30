
s = input("Enter a string: ")

i = 0
print("Forward:")
while i < len(s):
    print(s[i], end=" ")
    i += 1

print("\nBackward:")
i = len(s) - 1
while i >= 0:
    print(s[i], end=" ")
    i -= 1
print()
