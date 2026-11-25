def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)
n = int(input("Nhap so nguyen bat ky de tinh fibo: "))
result = fibo(n)
print(f"So fibo thu {n} la: {result}")