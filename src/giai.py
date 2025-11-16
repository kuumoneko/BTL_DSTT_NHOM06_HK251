from src.hai_an.tim_phuong_trinh import tim_phuong_trinh
from src.hai_an.giai_phuong_trinh import giai_phuong_trinh
from src.hai_an.kiem_tra_nghiem import kiem_tra_nghiem
from src.hai_an.tim_mien_nghiem import tim_mien_nghiem, nghiem, tim_x_va_y
from src.hai_an.ve_do_thi import ve_do_thi


def bai_hai_an(dulieu):
    # Lập phương trình từ dữ liệu bài toán
    phuong_trinh = tim_phuong_trinh(dulieu)

    # giải phương trình
    nghiemm = giai_phuong_trinh(phuong_trinh["phuong_trinh"])
    # kiểm tra các nghiệm có thõa mãn yêu cầu bài toán hay không
    kiem_tra = kiem_tra_nghiem(nghiemm)

    # tìm cặp (x , y) đem lại doanh thu cao nhất
    result = 0
    res = {"x": 0, "y": 0}
    if kiem_tra == "vo nghiem":
        print("Không có nghiệm hợp lệ")
        exit(0)

    # tìm lại nghiệm nguyên khi các nghiệm tìm được là các nghiệm lẻ (có số sau dấu thập phân)
    if kiem_tra == "co nghiem le":
        kiem_tra = tim_mien_nghiem(phuong_trinh["phuong_trinh"])

    for i in range(len(kiem_tra)):
        x_val = 0
        y_val = 0

        if str(type(kiem_tra[i])).count("dict") > 0:
            x_val = kiem_tra[i]["x"]
            y_val = kiem_tra[i]["y"]
        else:
            temp = nghiem(kiem_tra[i])
            x_val = temp["x"]
            y_val = temp["y"]
        if (
            x_val >= phuong_trinh["phuong_trinh"]["dieu_kien"][0]["ve_phai"]
            and y_val >= phuong_trinh["phuong_trinh"]["dieu_kien"][1]["ve_phai"]
        ):
            tong_tien = (
                x_val * dulieu["thuc_don"][0]["gia"]
                + y_val * dulieu["thuc_don"][1]["gia"]
            )

            if tong_tien > result:
                result = tong_tien
                res["x"] = x_val
                res["y"] = y_val
    # hiển thị các phương trình
    print(f"Số tiền lớn nhất có thể nhận được là: {result} nghìn đồng")
    print(f"Cách bán: {int(res['x'])} combo 1 và {int(res["y"])} combo 2")

    maxx = tim_x_va_y(phuong_trinh["phuong_trinh"])
    x_max = maxx["x_max"]
    y_max = maxx["y_max"]

    ve_do_thi(
        phuong_trinh["phuong_trinh"]["phuong_trinh"],
        x_range=[0, x_max],
        y_range=[0, y_max],
    )


from src.nhieu_an.lap_ma_tran import lap_ma_tran
import numpy as np
from scipy.optimize import linprog
from src.nhieu_an.solve import solve


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
    matran = lap_ma_tran(dulieu)
    bien = [(0, None) for _ in range(len(dulieu["thuc_don"]))]

    phuong_trinh_can_tinh = np.array(matran["phuong_trinh_can_tinh"])
    ve_trai = np.array(matran["ma_tran"])
    ve_phai = np.array(matran["gioi_han"])

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
            result = solve(
                matran["ma_tran"],
                matran["gioi_han"],
                phuong_trinh_can_tinh,
                [
                    [max(int(nghiem[i]) - 2, 0), int(nghiem[i]) + 2]
                    for i in range(len(nghiem))
                ],
            )
            print(result)
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
