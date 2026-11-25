def BinarySearch(n):
    if n <= 1:
        return 1
    return BinarySearch(n // 2) + 1
n = int(input("Nhap 1 so nguyen de tim kiem nhi phan: "))
if n > 0:
    SoBuoc = BinarySearch(n)
    print(f"So buoc se la: {SoBuoc}")
else:
    print("n phai > 0")