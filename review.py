print("Tinh BMI bang du lieu nhap chieu cao va can nang")
chieu_cao = float(input("Moi nhap chieu cao (kg): "))
can_nang = float(input("Moi nhap can nang (m): "))
bmi = chieu_cao/(can_nang**2)
print(f"Chi so BMI cua ban la: {bmi:.1f}")

print("==========")
print("Doi gio sang phut va giay")
gio = int(input("Moi ban nhap so gio: "))
phut = gio * 60
giay = gio * 3600
print(f"So phut cua {gio} gio la: {phut} phut")
print(f"So giay cua {gio} gio la: {giay} giay")

print("==========")
print("Tinh tien diem theo so kwh")
def tinh_tien_dien(kwh):
    tong_tien = 0
    if kwh <= 50:
        tong_tien = kwh * 1806
    elif kwh <= 100:
        tong_tien = 50 * 1806 + (kwh-50) * 1866
    elif kwh <= 200:
        tong_tien = 50 * 1806 + 50 * 1866 + (kwh-100) * 2167
    elif kwh <= 400:
        tong_tien = 50 * 1806 + 50 * 1866 + 100 * 2167 + (kwh-200) * 2729
    else:
        tong_tien = 50 * 1806 + 50 * 1866 + 100 * 2167 + 200 * 2729 + (kwh-400) * 3050
    tong_tieng_vat = tong_tien * 1.1
    return tong_tieng_vat
so_kwh = float(input("Nhap tong so kWh tieu thu: "))
print(f"Tong tien dien phat tra (da co VAT): {tinh_tien_dien(so_kwh):,.0f} VND")