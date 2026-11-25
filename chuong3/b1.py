def DeQuy(n):
    if  n == 1:
        return 1
    if n <= 0:
        return 0
    return n + DeQuy(n - 1)
n = int(input("Nhap so nguyen bat ky de tinh de quy: "))
result = DeQuy(n)
print(f"Ket qua De Quy = {result}")