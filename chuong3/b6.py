def UCLN(a, b):
    if a % b == 0:
        return b
    return UCLN(b, a % b)
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
print(f"UCLN({a}, {b}) = {UCLN(a, b)}")