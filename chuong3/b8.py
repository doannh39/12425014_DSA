import math
def TongCan(k, n):
    if k == n:
        return math.sqrt(n)
    return math.sqrt(k + TongCan(k + 1, n))
n = int(input("Nhap n: "))
print(f"Tong can cua n = {TongCan(1, n)}")