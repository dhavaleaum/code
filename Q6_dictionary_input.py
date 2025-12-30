
keys = ['name','age','city','is_student']
data = {}

for k in keys:
    value = input(f"Enter value for {k}: ")
    data[k] = value

print("Dictionary:", data)
