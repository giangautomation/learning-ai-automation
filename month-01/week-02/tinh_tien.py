ten_hang = input("Ten hang: ")
don_gia = float(input("Don gia (VND): "))
so_luong = int(input("So luong: "))

thanh_ten = don_gia * so_luong
thue = thanh_ten * 0.08
tong = thanh_ten + thue
print(f"--- Hoa don: {ten_hang} ---")
print(f"Thanh tien: {thanh_ten:,.0f} VND")
print(f"Thue 8%: {thue:,.0f} VND")
print(f"Tong cong: {tong:,.0f} VND")