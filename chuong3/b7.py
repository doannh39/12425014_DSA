def SoChuSo(n):
    if n == 0:
        return 0
    return SoChuSo(n // 10) + 1
n = int(input('Nhap 1 so nguyen bat ki: '))
print(f"So chu so cua {n} = {SoChuSo(n)}")