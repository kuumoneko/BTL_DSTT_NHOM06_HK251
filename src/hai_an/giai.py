import sympy as sp
from src.hai_an.tim_mien_nghiem import tim_x_va_y
from src.hai_an.ve_do_thi import ve_do_thi


def bai_hai_an(dulieu):
    x, y = sp.symbols("x y")  # tạo biến x và y

    # Lập phương trình từ dữ liệu bài toán
    phuong_trinh = {
        "phuong_trinh": [  # các bất phương trình điều kiện (vế trái <= vế phải)
            {
                "ve_trai": dulieu["thuc_don"][0]["dui_ga"] * x
                + dulieu["thuc_don"][1]["dui_ga"] * y,
                "ve_phai": dulieu["so_dui_ga"],
            },
            {
                "ve_trai": dulieu["thuc_don"][0]["tui_khoai_tay"] * x
                + dulieu["thuc_don"][1]["tui_khoai_tay"] * y,
                "ve_phai": dulieu["so_tui_khoai_tay"],
            },
            {
                "ve_trai": dulieu["thuc_don"][0]["ly_nuoc_chanh"] * x
                + dulieu["thuc_don"][1]["ly_nuoc_chanh"] * y,
                "ve_phai": dulieu["so_ly_nuoc_chanh"],
            },
            {
                "ve_trai": dulieu["thuc_don"][0]["ly_coca"] * x
                + dulieu["thuc_don"][1]["ly_coca"] * y,
                "ve_phai": dulieu["so_ly_coca"],
            },
        ],
        "dieu_kien": [  # điều kiện tiên quyết (x >= 0 và y >= 0)
            {"ve_trai": x, "ve_phai": 0},
            {"ve_trai": y, "ve_phai": 0},
        ],
    }

    # giải phương trình
    nghiem = []
    # Tìm giao điểm của các phương trình với nhau
    for i in range(len(phuong_trinh["phuong_trinh"])):
        for j in range(len(phuong_trinh["phuong_trinh"])):
            pt1 = sp.Eq(
                phuong_trinh["phuong_trinh"][i]["ve_trai"],
                phuong_trinh["phuong_trinh"][i]["ve_phai"],
            )
            pt2 = sp.Eq(
                phuong_trinh["phuong_trinh"][j]["ve_trai"],
                phuong_trinh["phuong_trinh"][j]["ve_phai"],
            )
            if str(pt1) == "True" or str(pt2) == "True":
                continue
            if str(pt1) == str(pt2):
                continue
            solution = sp.nonlinsolve([pt1, pt2], [x, y])
            nghiem.append(solution)

    # kiểm tra các nghiệm có thõa mãn yêu cầu bài toán hay không
    nghiem_nguyen = []
    for i in range(len(nghiem)):
        if str(nghiem[i]).count("/") > 0:
            nghiem_nguyen = "co nghiem le"
            break
        if str(nghiem[i]).count("-") > 0:
            continue
        if str(nghiem[i]).count("x") > 0:
            continue
        if str(nghiem[i]).count("y") > 0:
            continue
        if nghiem_nguyen.count(nghiem[i]) > 0:
            continue
        nghiem_nguyen.append(nghiem[i])

    if len(nghiem_nguyen) == 0:
        print("Không có nghiệm hợp lệ")
        exit(0)
    # tìm cặp (x , y) đem lại doanh thu cao nhất
    result = 0
    res = {"x": 0, "y": 0}
    # tìm lại nghiệm nguyên khi các nghiệm tìm được là các nghiệm lẻ (có số sau dấu thập phân)
    if nghiem_nguyen == "co nghiem le":
        results = []
        # tìm x MAX và y MAX
        maxx = tim_x_va_y(phuong_trinh)
        x_max = maxx["x_max"]
        y_max = maxx["y_max"]
        # tìm tất cả các nghiệm nguyên thuộc miện nghiệm
        for i in range(x_max + 1):
            for j in range(y_max + 1):
                results.append({"x": i, "y": j})
        nghiem_nguyen = results

    for i in range(len(nghiem_nguyen)):
        x_val = 0
        y_val = 0

        if str(type(nghiem_nguyen[i])).count("dict") > 0:
            x_val = nghiem_nguyen[i]["x"]
            y_val = nghiem_nguyen[i]["y"]
        else:
            temp = str(nghiem_nguyen[0]).split("{(")[1].split(")}")[0].split(", ")
            if temp[0] == "0":
                try:
                    x_val = float(temp[1])
                    y_val = float(temp[0])
                except:
                    try:
                        x_val = 0
                        a = int(temp[1].split("/")[0])
                        b = int(temp[1].split("/")[1])
                        y_val = float(a / b)
                    except:
                        x_val = 0
                        y_val = 0
            else:
                try:
                    x_val = float(temp[1])
                    y_val = float(temp[0])
                except:
                    try:
                        a = int(temp[0].split("/")[0])
                        b = int(temp[0].split("/")[1])
                        x_val = 0
                        y_val = float(a / b)
                    except:
                        x_val = 0
                        y_val = 0
        if (
            x_val >= phuong_trinh["dieu_kien"][0]["ve_phai"]
            and y_val >= phuong_trinh["dieu_kien"][1]["ve_phai"]
        ):
            tong_tien = (
                x_val * dulieu["thuc_don"][0]["gia"]
                + y_val * dulieu["thuc_don"][1]["gia"]
            )
            for pt in phuong_trinh["phuong_trinh"]:

                if pt["ve_trai"] == 0:
                    continue
                # ax + by
                # x,y -> symbols
                # coeff(x) -> a, y -> b
                if (x_val * pt["ve_trai"].coeff(x)) + (
                    y_val * pt["ve_trai"].coeff(y)
                ) > pt["ve_phai"]:
                    tong_tien = 0
                    break

            if tong_tien > result:
                result = tong_tien
                res["x"] = x_val
                res["y"] = y_val
    # hiển thị các phương trình
    print(f"Số tiền lớn nhất có thể nhận được là: {result} nghìn đồng")
    print(f"Cách bán: {int(res['x'])} combo 1 và {int(res["y"])} combo 2")

    maxx = tim_x_va_y(phuong_trinh)
    x_max = maxx["x_max"]
    y_max = maxx["y_max"]

    ve_do_thi(
        phuong_trinh["phuong_trinh"],
        x_range=[0, x_max],
        y_range=[0, y_max],
    )
