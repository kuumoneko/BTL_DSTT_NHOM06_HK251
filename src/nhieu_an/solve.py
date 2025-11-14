def kiem_tra(phuongtrinh, dieukien, bien):
    if len(phuongtrinh) != len(dieukien) or len(phuongtrinh[0]) != len(bien):
        return False
    for i in range(len(phuongtrinh)):
        sum = 0
        for j in range(len(bien)):
            sum += phuongtrinh[i][j] * bien[j]
        if sum > dieukien[i]:
            return False

    return True


def tinh(cantinh, bien):
    sum = 0
    for i in range(len(cantinh)):
        sum += cantinh[i] * bien[i] * -1
    return sum


def dequy(
    cap, bien_hien_tai, phuong_trinh, dieu_kien, he_so_ham_muc_tieu, pham_vi_bien
):
    if cap + 1 == len(pham_vi_bien):
        gia_tri_hien_tai = tinh(he_so_ham_muc_tieu, bien_hien_tai)
        return {
            "gia_tri": gia_tri_hien_tai,
            "bien_toi_uu": bien_hien_tai.copy(),  # Trả về một bản sao để không bị thay đổi
        }

    ket_qua_tot_nhat = {"gia_tri": -1, "bien_toi_uu": []}

    start, end = pham_vi_bien[cap]

    for gia_tri in range(start, end):
        bien_hien_tai[cap] = gia_tri
        if not kiem_tra(phuong_trinh, dieu_kien, bien_hien_tai):
            continue  # Nếu không hợp lệ, thử giá trị tiếp theo

        ket_qua_tu_nhanh_con = dequy(
            cap + 1,
            bien_hien_tai,
            phuong_trinh,
            dieu_kien,
            he_so_ham_muc_tieu,
            pham_vi_bien,
        )
        if ket_qua_tu_nhanh_con["gia_tri"] > ket_qua_tot_nhat["gia_tri"]:
            ket_qua_tot_nhat = ket_qua_tu_nhanh_con
    bien_hien_tai[cap] = 0
    return ket_qua_tot_nhat


def solve(phuongtrinh, dieu_kien, he_so_ham_muc_tieu, pham_vi_bien):
    return dequy(
        cap=0,
        bien_hien_tai=[pham_vi_bien[i][0] for i in range(len(pham_vi_bien))],
        phuong_trinh=phuongtrinh,
        dieu_kien=dieu_kien,
        he_so_ham_muc_tieu=he_so_ham_muc_tieu,
        pham_vi_bien=pham_vi_bien,
    )
