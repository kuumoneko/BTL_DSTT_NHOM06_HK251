"""
Để gây quỹ từ thiện, câu lạc bộ thiện nguyện của một trường THPT tổ chức hoạt động bán hàng với bốn mặt hàng là đùi gà rán, khoai tây chiên, nước chanh, nước coca.
Câu lạc bộ thiết kế hai thực đơn.
Thực đơn 1 có giá X nghìn đồng, bao gồm a cốc nước chanh và b túi khoai tây chiên, c ly nước chanh, d ly coca.
Thực đơn 2 có giá Y nghìn đồng, bao gồm e đùi gà rán, f túi khoai tây chiên, g ly nước chanh, h ly coca.

Biết rằng câu lạc bộ chỉ làm được không quá Q đùi gà rán, W túi khoai tây chiên, E ly nước chanh, R ly coca.

Số tiền lớn nhất mà câu lạc bộ có thể nhận được sau khi bán hết hàng bằng bao nhiêu nghìn đồng?

"""


def nhap_du_lieu(bo_test=4):
    if bo_test == 7:
        print("-" * 30 + " Kho " + "-" * 30)
        # nhập các điều kiện
        so_dui_ga = int(input("Số lượng đùi gà rán có thể làm được: "))
        so_tui_khoai_tay = int(input("Số lượng túi khoai tây có thể làm được: "))
        so_ly_nuoc_chanh = int(input("Số lượng ly nước chanh có thể làm được: "))
        so_ly_coca = int(input("Số lượng ly coca có thể làm được: "))
        n = int(input("Số lượng combo: "))

        # nhập các thông tin của các combo
        combo = []
        for i in range(n):
            print("-" * 30 + f" Combo {i+1} " + "-" * 30)
            gia = int(input("Giá combo: "))
            dui_ga = int(input("Số lượng đùi gà rán thực đơn: "))
            tui_khoai_tay = int(input("Số lượng túi khoai tây thực đơn: "))
            ly_nuoc_chanh = int(input("Số lượng ly nước chanh thực đơn: "))
            ly_coca = int(input("Số lượng ly coca thực đơn: "))
            combo.append(
                {
                    "gia": gia,
                    "dui_ga": dui_ga,
                    "tui_khoai_tay": tui_khoai_tay,
                    "ly_nuoc_chanh": ly_nuoc_chanh,
                    "ly_coca": ly_coca,
                }
            )
        return {
            "so_dui_ga": so_dui_ga,
            "so_tui_khoai_tay": so_tui_khoai_tay,
            "so_ly_nuoc_chanh": so_ly_nuoc_chanh,
            "so_ly_coca": so_ly_coca,
            "thuc_don": combo,
        }
    if bo_test == 1:
        return {
            "so_dui_ga": 418,
            "so_tui_khoai_tay": 144,
            "so_ly_nuoc_chanh": 1020,
            "so_ly_coca": 612,
            "thuc_don": [
                {
                    "gia": 30,
                    "dui_ga": 11,
                    "tui_khoai_tay": 3,
                    "ly_nuoc_chanh": 17,
                    "ly_coca": 18,
                },
                {
                    "gia": 50,
                    "dui_ga": 19,
                    "tui_khoai_tay": 8,
                    "ly_nuoc_chanh": 60,
                    "ly_coca": 17,
                },
            ],
        }
    if bo_test == 2:
        return {
            "so_dui_ga": 0,
            "so_tui_khoai_tay": 100,
            "so_ly_nuoc_chanh": 165,
            "so_ly_coca": 0,
            "thuc_don": [
                {
                    "gia": 30,
                    "dui_ga": 0,
                    "tui_khoai_tay": 1,
                    "ly_nuoc_chanh": 2,
                    "ly_coca": 0,
                },
                {
                    "gia": 50,
                    "dui_ga": 0,
                    "tui_khoai_tay": 2,
                    "ly_nuoc_chanh": 3,
                    "ly_coca": 0,
                },
            ],
        }
    if bo_test == 3:
        return {
            "so_dui_ga": 50,
            "so_tui_khoai_tay": 45,
            "so_ly_nuoc_chanh": 30,
            "so_ly_coca": 15,
            "thuc_don": [
                {
                    "gia": 30,
                    "dui_ga": 2,
                    "tui_khoai_tay": 4,
                    "ly_nuoc_chanh": 1,
                    "ly_coca": 1,
                },
                {
                    "gia": 40,
                    "dui_ga": 3,
                    "tui_khoai_tay": 2,
                    "ly_nuoc_chanh": 2,
                    "ly_coca": 1,
                },
                {
                    "gia": 50,
                    "dui_ga": 5,
                    "tui_khoai_tay": 3,
                    "ly_nuoc_chanh": 2,
                    "ly_coca": 1,
                },
            ],
        }
    if bo_test == 4:
        return {
            "so_dui_ga": 200,
            "so_tui_khoai_tay": 1200,
            "so_ly_nuoc_chanh": 600,
            "so_ly_coca": 1000,
            "thuc_don": [
                {
                    "gia": 30,
                    "dui_ga": 1,
                    "tui_khoai_tay": 8,
                    "ly_nuoc_chanh": 1,
                    "ly_coca": 1,
                },
                {
                    "gia": 40,
                    "dui_ga": 1,
                    "tui_khoai_tay": 3,
                    "ly_nuoc_chanh": 5,
                    "ly_coca": 2,
                },
                {
                    "gia": 50,
                    "dui_ga": 1,
                    "tui_khoai_tay": 4,
                    "ly_nuoc_chanh": 1,
                    "ly_coca": 10,
                },
            ],
        }
    if bo_test == 5:
        return {
            "so_dui_ga": 200,
            "so_tui_khoai_tay": 250,
            "so_ly_nuoc_chanh": 300,
            "so_ly_coca": 400,
            "thuc_don": [
                {
                    "gia": 30,
                    "dui_ga": 1,
                    "tui_khoai_tay": 5,
                    "ly_nuoc_chanh": 4,
                    "ly_coca": 1,
                },
                {
                    "gia": 40,
                    "dui_ga": 2,
                    "tui_khoai_tay": 2,
                    "ly_nuoc_chanh": 2,
                    "ly_coca": 2,
                },
                {
                    "gia": 50,
                    "dui_ga": 3,
                    "tui_khoai_tay": 3,
                    "ly_nuoc_chanh": 3,
                    "ly_coca": 3,
                },
                {
                    "gia": 60,
                    "dui_ga": 4,
                    "tui_khoai_tay": 4,
                    "ly_nuoc_chanh": 3,
                    "ly_coca": 3,
                },
            ],
        }
    if bo_test == 6:
        return {
            "so_dui_ga": 14,
            "so_tui_khoai_tay": 21,
            "so_ly_nuoc_chanh": 21,
            "so_ly_coca": 22,
            "thuc_don": [
                {
                    "gia": 30,
                    "dui_ga": 1,
                    "tui_khoai_tay": 2,
                    "ly_nuoc_chanh": 5,
                    "ly_coca": 1,
                },
                {
                    "gia": 40,
                    "dui_ga": 1,
                    "tui_khoai_tay": 3,
                    "ly_nuoc_chanh": 2,
                    "ly_coca": 2,
                },
                {
                    "gia": 50,
                    "dui_ga": 1,
                    "tui_khoai_tay": 4,
                    "ly_nuoc_chanh": 2,
                    "ly_coca": 1,
                },
                {
                    "gia": 60,
                    "dui_ga": 2,
                    "tui_khoai_tay": 1,
                    "ly_nuoc_chanh": 1,
                    "ly_coca": 3,
                },
            ],
        }
    if bo_test == 8:
        return {
            "so_dui_ga": 44,
            "so_tui_khoai_tay": 40,
            "so_ly_nuoc_chanh": 60,
            "so_ly_coca": 52,
            "thuc_don": [
                {
                    "gia": 30,
                    "dui_ga": 1,
                    "tui_khoai_tay": 1,
                    "ly_nuoc_chanh": 1,
                    "ly_coca": 2,
                },
                {
                    "gia": 50,
                    "dui_ga": 2,
                    "tui_khoai_tay": 1,
                    "ly_nuoc_chanh": 3,
                    "ly_coca": 1,
                },
            ],
        }
