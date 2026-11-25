import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def them_cuoi(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        p = self.head
        while p.next:
            p = p.next
        p.next = new_node

    def tim_max(self):
        if not self.head:
            return None
        max_val = float('-inf')
        p = self.head
        while p:
            if p.data > max_val:
                max_val = p.data
            p = p.next
        return max_val

    def tinh_tong(self):
        t = 0
        p = self.head
        while p:
            t += p.data
            p = p.next
        return t

    def ktnt(self, x):
        if x < 2:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    def dem_nguyen_to(self):
        dem = 0
        p = self.head
        while p:
            if self.ktnt(p.data):
                dem += 1
            p = p.next
        return dem

    def dem_am_duong_khong(self):
        am = duong = khong = 0
        p = self.head
        while p:
            if p.data < 0:
                am += 1
            elif p.data > 0:
                duong += 1
            else:
                khong += 1
            p = p.next
        return am, duong, khong

    def dem_x(self, x):
        dem = 0
        p = self.head
        while p:
            if p.data == x:
                dem += 1
            p = p.next
        return dem

    def tim_min_duong(self):
        min_duong = float('inf')
        p = self.head
        while p:
            if 0 < p.data < min_duong:
                min_duong = p.data
            p = p.next
        return None if min_duong == float('inf') else min_duong

l = LinkedList()
n = int(input("Nhap so phan tu n: "))
for i in range(n):
    val = int(input(f"Nhap phan tu thu {i + 1}: "))
    l.them_cuoi(val)

print("a. Phan tu lon nhat:", l.tim_max())
print("b. Tong cac phan tu:", l.tinh_tong())
print("c. So luong so nguyen to:", l.dem_nguyen_to())
am, duong, khong = l.dem_am_duong_khong()
print(f"d. Am: {am}, Duong: {duong}, Bang 0: {khong}")
x = int(input("Nhap x can dem: "))
print("e. So luong so bang x:", l.dem_x(x))
print("f. Phan tu duong nho nhat:", l.tim_min_duong())