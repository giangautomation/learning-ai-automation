import datetime

print("Nhap 2 so de thuc hien cac phep tinh")
a = int(input("So a: "))
while True:
    b = int(input("So b: "))
    if b < a:
        break
    print("So b phai lon hon a! Vui long nhap lai: ")
print("Tong a + b =", a + b)
print("Hieu a - b =", a - b)
print("Tich a x b =",a * b)
print("Thuong a : b =",a / b)

print("==========")
print("Nhap ten va nam sinh, in ra tuoi (tu dien nam hien tai)")
ten = input("Ten cua ban la: ")
nam_sinh = int(input("Nam sinh cua ban la: "))
nam_hien_tai = datetime.datetime.now().year
tuoi = nam_hien_tai - nam_sinh
print(f"Xin chao {ten}, hien tai ban {tuoi} tuoi")

print("==========")
print("Nhap so km da di va gia xang moi lit, tinh tien xang voi muc tieu hao 6 lit/100km")
so_km = int(input("Nhap so km: "))
gia_xang = int(input("Nhap gia xang "))
tien_xang = (so_km * 6 / 100) * gia_xang
print(f"Tien xang de di {so_km:.0f} KM la {tien_xang:,.0f} VND")