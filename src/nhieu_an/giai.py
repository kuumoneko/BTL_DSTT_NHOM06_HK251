import numpy as np
from scipy.optimize import linprog
from src.nhieu_an.tim_nghiem_nguyen import dequy

# kiểm tra nghiệm có hợp lệ hay không
def check_an(solution):
    for i in range(len(solution)):
        if solution[i] < 0:
            return False
        if solution[i] % 1 != 0:
            return False
    return True

def bai_nhieu_an(dulieu):
    # Lập ma trận từ dữ liệu bài toán

    ma_tran = [[] for _ in range(4)]
    phuong_trinh_can_tinh = []
    gioi_han = [
        dulieu["so_dui_ga"],
        dulieu["so_tui_khoai_tay"],
        dulieu["so_ly_nuoc_chanh"],
        dulieu["so_ly_coca"],
    ]
    for i in range(len(dulieu["thuc_don"])):
        combo = dulieu["thuc_don"][i]
        duiga = ma_tran[0]
        tui_khoai_tay = ma_tran[1]
        ly_nuoc_chanh = ma_tran[2]
        ly_coca = ma_tran[3]

        duiga.append(combo["dui_ga"])
        tui_khoai_tay.append(combo["tui_khoai_tay"])
        ly_nuoc_chanh.append(combo["ly_nuoc_chanh"])
        ly_coca.append(combo["ly_coca"])
        phuong_trinh_can_tinh.append(-1 * int(combo["gia"]))

    bien = [(0, None) for _ in range(len(dulieu["thuc_don"]))]

    phuong_trinh_can_tinh = np.array(phuong_trinh_can_tinh)
    ve_trai = np.array(ma_tran)
    ve_phai = np.array(gioi_han)

    # giải hệ phương trình với quy tắc làm cho hàm đích có giá trị cao nhất
    result = linprog(
        c=phuong_trinh_can_tinh,
        A_ub=ve_trai,
        b_ub=ve_phai,
        bounds=bien,
        method="highs",
    )
    if result.success:
        nghiem = result.x
        # Nghiệm lẻ thì tìm lại nghiệm nguyên khác
        if not check_an(nghiem):
            pham_vi_bien = [
                [max(int(nghiem[i]) - 2, 0), int(nghiem[i]) + 2]
                for i in range(len(nghiem))
            ]
            # print(pham_vi_bien)
            result = dequy(
                cap=0,
                bien_hien_tai=[pham_vi_bien[i][0] for i in range(len(pham_vi_bien))],
                phuong_trinh=ma_tran,
                dieu_kien=gioi_han,
                he_so_ham_muc_tieu=phuong_trinh_can_tinh,
                pham_vi_bien=pham_vi_bien,
            )
            # print(res//ult)
            print(
                f"Số tiên lớn nhất có thể nhận được là: {result['gia_tri']} nghìn đồng"
            )
            print(f"Cách bán: ", end="")
            for i in range(len(result["bien_toi_uu"])):
                if (int(result["bien_toi_uu"][i])) == 0:
                    continue
                print(
                    f"{result["bien_toi_uu"][i]} phần combo thứ {i +1}",
                    end=", " if i + 1 < len(result["bien_toi_uu"]) else "",
                )
        # nếu là nghiệm nguyên thì in ra kết quả luôn
        else:
            max_profit = -result.fun
            print(f"Số tiên lớn nhất có thể nhận được là: {max_profit} nghìn đồng")
            print(f"Cách bán: ", end="")
            for i in range(len(nghiem)):
                if (int(nghiem[i])) == 0:
                    continue
                print(
                    f"{nghiem[i]} phần combo thứ {i +1}",
                    end=", " if i + 1 < len(nghiem) else "",
                )
    else:
        print("Không có nghiệm hợp lệ")
