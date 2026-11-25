import random
num =[random.randint(0, 1000) for _ in range(1000)]
max = num[0]
min = num[0]
for i in num:
    if i > max:
        max = i
    if i < min:
        min = i
print(f"So lon nhat: {max}")
print(f"So nho nhat: {min}")