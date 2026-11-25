def DeQuy(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return (1/n) + DeQuy(n - 1)
n = int(input("Nhap 1 so nguyen de tinh de quy: "))
result = DeQuy(n)
print(f"Ket qua tinh De quy la: {result}")