def DeQuy(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n * n + DeQuy(n - 1)
n = int(input("Nhap 1 so nguyen bat ki de tinh De quy: "))
result = DeQuy(n)
print(f"Ket qua De Quy la: {result}")