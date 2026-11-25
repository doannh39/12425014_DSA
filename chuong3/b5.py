def UocleMax(n):
    if n % 2 == 1:
        return n
    return UocleMax(n // 2)
n = int(input("Nhap n bat ki la so nguyen: "))
print('Uoc le Max la: ', UocleMax(n))