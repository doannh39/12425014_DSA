def tong_ma_tran(a, n):
  tong = 0
  for i in range(n):
    for j in range(n):
      tong += a[i][j]
  return tong
def duong_nho_nhat(a, n):
  min_duong = float("inf") 
  for i in range(n):
    for j in range(n):
      if 0 < a[i][j] < min_duong:
        min_duong = a[i][j]
  return None if min_duong == float("inf") else min_duong
def tong_cheo_phu(a, n):
  tong = 0
  for i in range(n):
    tong += a[i][n - 1 - i]
  return tong
def kiem_tra_cheo_chinh_tang(a, n):
  for i in range(n - 1):
    if a[i][i] >= a[i + 1][i + 1]:
      return False
  return True
n = int(input("Nhập cấp ma trận vuông n (0 <= n < 100): "))
if n <= 0 or n >= 100:
  print("Giá trị n không hợp lệ hoặc ma trận rỗng!")
else:
  a = []
  for i in range(n):
    hang = [int(input(f"a[{i}][{j}] = ")) for j in range(n)]
    a.append(hang)
  print("\nMa trận vừa nhập:")
  for hang in a:
    print(*hang)
  print("\na. Tổng tất cả phần tử:", tong_ma_tran(a, n))
  kq_b = duong_nho_nhat(a, n)
  print(
      "b. Giá trị dương nhỏ nhất:",
      kq_b if kq_b is not None else "Không có số dương",
  )
  print("c. Tổng đường chéo phụ:", tong_cheo_phu(a, n))
  print(
      "d. Đường chéo chính tăng dần:",
      "Có" if kiem_tra_cheo_chinh_tang(a, n) else "Không",
  )