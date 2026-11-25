n = int(input("Nhập n: "))
a = [int(input(f"a[{i}] = ")) for i in range(n)]
print("Mảng vừa nhập:", a)
k = int(input("Vị trí chèn k: "))
x = int(input("Giá trị chèn: "))
a = a[:k] + [x] + a[k:]
print("Mảng sau khi chèn:", a)