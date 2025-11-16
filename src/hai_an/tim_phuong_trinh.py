import sympy as sp

def tim_phuong_trinh(data):
    x, y = sp.symbols("x y")  # tạo biến x và y
    phuong_trinh_can_tinh = data["thuc_don"][0]["gia"] * x + data["thuc_don"][1]["gia"] * y # phương trình cần để tính toán doanh thu
    return {
        "phuong_trinh": {
            "phuong_trinh": [ # các bất phương trình điều kiện (vế trái <= vế phải)
                {
                    "ve_trai": data["thuc_don"][0]["dui_ga"] * x
                    + data["thuc_don"][1]["dui_ga"] * y,
                    "ve_phai": data["so_dui_ga"],
                },
                {
                    "ve_trai": data["thuc_don"][0]["tui_khoai_tay"] * x
                    + data["thuc_don"][1]["tui_khoai_tay"] * y,
                    "ve_phai": data["so_tui_khoai_tay"],
                },
                {
                    "ve_trai": data["thuc_don"][0]["ly_nuoc_chanh"] * x
                    + data["thuc_don"][1]["ly_nuoc_chanh"] * y,
                    "ve_phai": data["so_ly_nuoc_chanh"],
                },
                {
                    "ve_trai": data["thuc_don"][0]["ly_coca"] * x
                    + data["thuc_don"][1]["ly_coca"] * y,
                    "ve_phai": data["so_ly_coca"],
                },
            ],
            "dieu_kien": [ # điều kiện tiên quyết (x >= 0 và y >= 0)
                {"ve_trai": x, "ve_phai": 0},
                {"ve_trai": y, "ve_phai": 0},
            ],
        },
        "phuong_trinh_can_tinh": phuong_trinh_can_tinh,
    }
