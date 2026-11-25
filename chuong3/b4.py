def LuyThua(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / LuyThua(x, n)
    return x * LuyThua(x, n - 1)
x= int(input("Nhap so nguyen x: "))
n = int(input("Nhap so mu n: "))
result = LuyThua(x, n)
print(f"Ket qua cua {x}^{n} = {result}")