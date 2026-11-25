class NhanVien:

  def __init__(
      self,
      MaNV: str,
      HoVaTen: str,
      NamSinh: int,
      PhongBan: str,
      LuongCoBan: int,
      Thuong: int,
  ):
    self.MaNV = MaNV
    self.HoVaTen = HoVaTen
    self.NamSinh = NamSinh
    self.PhongBan = PhongBan
    self.LuongCoBan = LuongCoBan
    self.Thuong = Thuong
    self.ThucLinh = LuongCoBan + Thuong

  def HienThi(self):
    print(
        f"{self.MaNV} | {self.HoVaTen} | {self.NamSinh} | {self.PhongBan} | "
        f"Luong co ban: {self.LuongCoBan} | "
        f"Thuong: {self.Thuong} | "
        f"Thuc linh: {self.ThucLinh}"
    )


n = int(input("Nhap so luong NV: "))
DanhSach = []
for i in range(n):
  print(f"Nhap nhan vien thu {i + 1}")
  ma_nv = input("Ma NV: ")
  ho_va_ten = input("Ho va Ten: ")
  nam_sinh = int(input("Nam sinh: "))
  phong_ban = input("Phong ban: ")
  luong_co_ban = int(input("Luong co ban: "))
  thuong = int(input("Thuong: "))
  DanhSach.append(
      NhanVien(ma_nv, ho_va_ten, nam_sinh, phong_ban, luong_co_ban, thuong)
  )

# a
tong_thuc_linh = sum(nv.ThucLinh for nv in DanhSach)
print(f"Tong thuc linh cua ca cong ty = {tong_thuc_linh}")

# b
print("Nhan vien co muc luong co ban thap nhat: ")
if DanhSach:
  min_luong = min(nv.LuongCoBan for nv in DanhSach)
  for nv in DanhSach:
    if nv.LuongCoBan == min_luong:
      nv.HienThi()

# c
dem = sum(1 for nv in DanhSach if nv.Thuong >= 1200000)
print(f"So nhan vien co thuong >= 1.200.000 la: {dem}")

# d
print("Danh sach phong ban sau khi sap xep: ")
for i in range(len(DanhSach) - 1):
  for j in range(i + 1, len(DanhSach)):
    if DanhSach[i].PhongBan > DanhSach[j].PhongBan or (
        DanhSach[i].PhongBan == DanhSach[j].PhongBan
        and DanhSach[i].MaNV < DanhSach[j].MaNV
    ):
      DanhSach[i], DanhSach[j] = DanhSach[j], DanhSach[i]
for nv in DanhSach:
  nv.HienThi()

# e
print("Danh sach sau khi tang luong co ban len 5%")
for nv in DanhSach:
  nv.LuongCoBan = int(nv.LuongCoBan * 1.05)
  nv.ThucLinh = nv.LuongCoBan + nv.Thuong
  nv.HienThi() 