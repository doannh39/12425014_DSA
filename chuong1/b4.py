import random
num = [random.randint(0, 1000) for _ in range(1000)]
#a
print(f"mang: {num}")
#b
num.sort()
print("=========")
print(f"Thu tu tu tang la: {num}")