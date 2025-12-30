
s = "Learning python"
vowels = set()

for ch in s.lower():
    if ch in "aeiou":
        vowels.add(ch)

print("Vowels present:", vowels)
