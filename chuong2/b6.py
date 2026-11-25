import random
def BubbleSort(DaySo):
    n = len(DaySo)
    for i in range(n):
        for j in range(0, n - i - 1):
            if DaySo[j] > DaySo[j + 1]:
                DaySo[j], DaySo[j + 1] = DaySo[j + 1], DaySo[j]
    return DaySo
n = int(input("Nhap vao mot so bat ki de tinh day so: ")) 
ds = [random.randint(0, n) for i in range(n)]
print("Mang truoc khi sap xep se la: ", ds)
BubbleSort(ds)
print("Mang sau khi sap xep se la: ", ds)