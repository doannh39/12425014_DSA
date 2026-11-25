n = int(input("Nhap so nguyen bat ki de tinh so hoan hao: "))
for i in range(1, n):
    tong = 0
    for j in range(1, i):
        if i % j == 0:
            tong = tong + j
    if tong == i and i > 0:
        print(f"So hoan hao cua {n} la: {i}")