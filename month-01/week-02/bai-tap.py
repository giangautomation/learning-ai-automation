l=25
w=12
cv=(l+w)*2
dt=l*w

do_C = 47
do_F = do_C*1.8+32

don_gia = 3450
so_luong = 210
thue = 0.08
tong_tien = don_gia*so_luong*(1+thue)

print("Bai 1: Tinh chu vi va dien tich hinh chu nhat")
print("Chu vi hinh chu nhat =",cv)
print("Dien tich hinh chu nhat =",dt)
print("==========")
print("Bai 2: Doi do C sang do F")
print("Do F =",do_F)
print("==========")
print("Bai 3: Tinh tong tien")
print("Tong tien =",tong_tien)

#Bai tap Wednesday of Month 1
print("==========")
print("Xin chao")
print("Toi", "ten", "Lan")
print("A", "B", sep="-")
print("Dong 1", end=" | ")
print("Dong 2")
print("Dong 1\nDong 2")

print("==========")
ten = input("Ban ten la gi? ")
print("Xin chao", ten)

print("==========")
print("Test input chi tra ve chuoi str du go so")
tuoi = input("Tuoi: ")
print(type(tuoi))

print("==========")
print("Ep kieu str -> int")
so_tuoi = int(input("Tuoi: "))
print(type(so_tuoi))
print(so_tuoi + 1)

print("==========")
print("Ghep chuoi va dinh dang chuoi")
print("Tuoi cua ban:", 25) #Dau phay trong print
print("Xin chao " + ten) #phai tu them dau cach
print("Tuoi " + str(25)) #Dau + chi dung cho chuoi + chuoi, phai ep chuoi
f_ten = "GiangNguyen"
f_tuoi = 28
print(f"Xin chao {f_ten}! Nam sau ban {f_tuoi + 1} tuoi.") #Dung f-string
x = 12345.234113
print(f"{x:.2f}") #2 so sau dau thap phan
print(f"{x:,.0f}") #co dau phay hang nghin, lam tron so
print(f"{x:,.2f}")