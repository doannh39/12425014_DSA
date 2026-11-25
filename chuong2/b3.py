def NguyenTo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True
n = int(input("Nhap so nguyen bat ki de kiem tra so nguyen to: "))
result = NguyenTo(n)
print(f"So nay la so nguyen to: {result}")