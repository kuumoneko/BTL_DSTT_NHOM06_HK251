def kiem_tra(phuongtrinh, dieukien, bien):
    if len(phuongtrinh) != len(dieukien) or len(phuongtrinh) != len(bien):
        return False

    for i in range(len(phuongtrinh)):
        sum = 0
        for j in range(len(bien)):
            sum += phuongtrinh[i][j] * bien[j]
        if sum > dieukien[i]:
            return False

    return True


def dequy(
    cap, bien_hien_tai, phuong_trinh, dieu_kien, he_so_ham_muc_tieu, pham_vi_bien
):
    if cap == len(pham_vi_bien):
        gia_tri_hien_tai = 0
        for i in range(len(he_so_ham_muc_tieu)):
            gia_tri_hien_tai += he_so_ham_muc_tieu[i] * bien_hien_tai[i] * -1
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
