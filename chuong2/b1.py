def ThapHaNoi(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return 2 * ThapHaNoi(n - 1) + 1
n = int(input("Nhap so nguyen bat ki: "))
result = ThapHaNoi(n)
print(f"Tong so buoc se la: {result}")