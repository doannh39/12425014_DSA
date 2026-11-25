class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.pHead = None

    def them_cuoi(self, data):
        new_node = Node(data)
        if not self.pHead:
            self.pHead = new_node
            return
        p = self.pHead
        while p.next:
            p = p.next
        p.next = new_node

    def hien_thi(self):
        p = self.pHead
        while p:
            print(p.data, end=" -> ")
            p = p.next
        print("None")

    def dem_x(self, x):
        d = 0
        p = self.pHead
        while p:
            if p.data == x:
                d += 1
            p = p.next
        return d

    def tim_min_duong(self):
        min_duong = float('inf')
        p = self.pHead
        while p:
            if 0 < p.data < min_duong:
                min_duong = p.data
            p = p.next
        return None if min_duong == float('inf') else min_duong

    def xoa_x_dau_tien(self, x):
        p = self.pHead
        t = None
        while p and p.data != x:
            t = p
            p = p.next
        if not p:
            return
        if not t:
            self.pHead = p.next
        else:
            t.next = p.next

ds = LinkedList()
n = int(input("Nhap so phan tu n: "))
for i in range(n):
    val = int(input(f"Nhap phan tu thu {i + 1}: "))
    ds.them_cuoi(val)

ds.hien_thi()
x = int(input("Nhap x can dem: "))
print("So phan tu bang x:", ds.dem_x(x))
print("Phan tu duong nho nhat:", ds.tim_min_duong())
x_xoa = int(input("Nhap x can xoa dau tien: "))
ds.xoa_x_dau_tien(x_xoa)
ds.hien_thi()