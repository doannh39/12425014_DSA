def fibo(n):
    if n <= 0:
        return "Nhap lai"
    elif n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return b
n = int(input("Nhap mot so nguyen: "))
result = fibo(n)
print(f"So fibo thu {n}: {result}")