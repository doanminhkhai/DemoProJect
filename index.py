class CanBo:
    def __init__(self, ma_can_bo, ho_ten, phong_ban, chuc_vu, he_so_luong):
        self.ma_can_bo = ma_can_bo
        self.ho_ten = ho_ten
        self.phong_ban = phong_ban
        self.chuc_vu = chuc_vu
        self.he_so_luong = he_so_luong

# Tạo danh sách cán bộ
def tao_danh_sach_can_bo():
    danh_sach_can_bo = []
    while True:
        ma_can_bo = int(input("Nhập mã cán bộ (nhập số âm để kết thúc): "))
        if ma_can_bo <= 0:
            break
        ho_ten = input("Nhập họ và tên cán bộ: ")
        phong_ban = input("Nhập tên phòng ban: ")
        chuc_vu = input("Nhập chức vụ: ")
        he_so_luong = float(input("Nhập hệ số lương: "))
        can_bo = CanBo(ma_can_bo, ho_ten, phong_ban, chuc_vu, he_so_luong)
        danh_sach_can_bo.append(can_bo)
    return danh_sach_can_bo

# Thêm 1 cán bộ vào danh sách
def them_can_bo(danh_sach_can_bo):
    ma_can_bo = int(input("Nhập mã cán bộ: "))
    ho_ten = input("Nhập họ và tên cán bộ: ")
    phong_ban = input("Nhập tên phòng ban: ")
    chuc_vu = input("Nhập chức vụ: ")
    he_so_luong = float(input("Nhập hệ số lương: "))
    can_bo = CanBo(ma_can_bo, ho_ten, phong_ban, chuc_vu, he_so_luong)
    vi_tri = int(input("Nhập vị trí muốn thêm vào: "))
    danh_sach_can_bo.insert(vi_tri, can_bo)

# Tính lương cho nhân viên
def tinh_luong(danh_sach_can_bo):
    for can_bo in danh_sach_can_bo:
        luong = can_bo.he_so_luong * 1150000
        print(f"Lương của {can_bo.ho_ten} là: {luong}")

# Thống kê số lượng cán bộ theo từng phòng ban
def thong_ke_phong_ban(danh_sach_can_bo):
    phong_ban = input("Nhập tên phòng ban cần thống kê: ")
    count = 0
    for can_bo in danh_sach_can_bo:
        if can_bo.phong_ban == phong_ban:
            count += 1
            print(f"{can_bo.ho_ten} - {can_bo.chuc_vu}")
    print(f"Tổng số cán bộ trong phòng ban {phong_ban} là: {count}")

# In lên màn hình tất cả cán bộ có hệ số lương >= 4.9
def in_can_bo_he_so_lon_hon(danh_sach_can_bo):
    for can_bo in danh_sach_can_bo:
        if can_bo.he_so_luong >= 4.9:
            print(f"{can_bo.ho_ten} - {can_bo.chuc_vu}")

# Tìm và in danh sách cán bộ theo Chức vụ
def tim_can_bo_theo_chuc_vu(danh_sach_can_bo):
    chuc_vu = input("Nhập chức vụ cần tìm: ")
    for can_bo in danh_sach_can_bo:
        if can_bo.chuc_vu == chuc_vu:
            print(f"{can_bo.ho_ten} - {can_bo.phong_ban}")

# Tìm và in danh sách cán bộ theo hệ số lương và phòng ban
def tim_can_bo_theo_he_so_luong_va_phong_ban(danh_sach_can_bo):
    he_so_luong = float(input("Nhập hệ số lương cần tìm: "))
    phong_ban = input("Nhập tên phòng ban cần tìm: ")
    for can_bo in danh_sach_can_bo:
        if can_bo.he_so_luong == he_so_luong and can_bo.phong_ban == phong_ban:
            print(f"{can_bo.ho_ten} - {can_bo.chuc_vu}")

# Sắp xếp danh sách cán bộ theo thứ tự của tên
def sap_xep_theo_ten(danh_sach_can_bo):
    danh_sach_can_bo.sort(key=lambda x: x.ho_ten)
# In ra toàn bộ danh sách cán bộ
def in_danh_sach_can_bo(danh_sach_can_bo):
    print("=== Danh sách cán bộ ===")
    for can_bo in danh_sach_can_bo:
        print(f"Mã cán bộ: {can_bo.ma_can_bo}")
        print(f"Họ và tên: {can_bo.ho_ten}")
        print(f"Phòng ban: {can_bo.phong_ban}")
        print(f"Chức vụ: {can_bo.chuc_vu}")
        print(f"Hệ số lương: {can_bo.he_so_luong}")
        print("==========================")
# Hàm main
def main():
    danh_sach_can_bo = []

    while True:
        print("\n======= MENU =======")
        print("1. Tạo danh sách cán bộ")
        print("2. Thêm cán bộ")
        print("3. Tính lương")
        print("4. Thống kê số lượng cán bộ theo phòng ban")
        print("5. In danh sách cán bộ có hệ số lương >= 4.9")
        print("6. Tìm và in danh sách cán bộ theo chức vụ")
        print("7. Tìm và in danh sách cán bộ theo hệ số lương và phòng ban")
        print("8. Sắp xếp danh sách cán bộ theo tên")
        print("9. In ra toàn bộ danh sách cán bộ")
        print("0. Thoát")

        lua_chon = int(input("Nhập lựa chọn của bạn: "))

        if lua_chon == 1:
            danh_sach_can_bo = tao_danh_sach_can_bo()
        elif lua_chon == 2:
            them_can_bo(danh_sach_can_bo)
        elif lua_chon == 3:
            tinh_luong(danh_sach_can_bo)
        elif lua_chon == 4:
            thong_ke_phong_ban(danh_sach_can_bo)
        elif lua_chon == 5:
            in_can_bo_he_so_lon_hon(danh_sach_can_bo)
        elif lua_chon == 6:
            tim_can_bo_theo_chuc_vu(danh_sach_can_bo)
        elif lua_chon == 7:
            tim_can_bo_theo_he_so_luong_va_phong_ban(danh_sach_can_bo)
        elif lua_chon == 8:
            sap_xep_theo_ten(danh_sach_can_bo)
        elif lua_chon == 9:
            in_danh_sach_can_bo(danh_sach_can_bo)
        elif lua_chon == 0:
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()