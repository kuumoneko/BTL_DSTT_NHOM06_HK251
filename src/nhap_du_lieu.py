"""
Để gây quỹ từ thiện, câu lạc bộ thiện nguyện của một trường THPT tổ chức hoạt động bán hàng với bốn mặt hàng là đùi gà rán, khoai tây chiên, nước chanh, nước coca.
Câu lạc bộ thiết kế hai thực đơn.
Thực đơn 1 có giá X nghìn đồng, bao gồm a cốc nước chanh và b túi khoai tây chiên, c ly nước chanh, d ly coca.
Thực đơn 2 có giá Y nghìn đồng, bao gồm e đùi gà rán, f túi khoai tây chiên, g ly nước chanh, h ly coca.

Biết rằng câu lạc bộ chỉ làm được không quá Q đùi gà rán, W túi khoai tây chiên, E ly nước chanh, R ly coca.

Số tiền lớn nhất mà câu lạc bộ có thể nhận được sau khi bán hết hàng bằng bao nhiêu nghìn đồng?

"""


def nhap_du_lieu():
    print("-" * 30 + " Kho " + "-" * 30)
    so_dui_ga = int(input("Số lượng đùi gà rán có thể làm được: "))
    so_tui_khoai_tay = int(input("Số lượng túi khoai tây có thể làm được: "))
    so_ly_nuoc_chanh = int(input("Số lượng ly nước chanh có thể làm được: "))
    so_ly_coca = int(input("Số lượng ly coca có thể làm được: "))
    print("-" * 30 + " Thực đơn 1 " + "-" * 30)
    gia_thuc_don_1 = int(input("Giá thực đơn 1: "))
    dui_ga_1 = int(input("Số lượng đùi gà rán thực đơn 1: "))
    tui_khoai_tay_1 = int(input("Số lượng túi khoai tây thực đơn 1: "))
    ly_nuoc_chanh_1 = int(input("Số lượng ly nước chanh thực đơn 1: "))
    ly_coca_1 = int(input("Số lượng ly coca thực đơn 1: "))
    print("-" * 30 + " Thực đơn 2 " + "-" * 30)
    gia_thuc_don_2 = int(input("Giá thực đơn 2: "))
    dui_ga_2 = int(input("Số lượng đùi gà rán thực đơn 2: "))
    tui_khoai_tay_2 = int(input("Số lượng túi khoai tây thực đơn 2: "))
    ly_nuoc_chanh_2 = int(input("Số lượng ly nước chanh thực đơn 2: "))
    ly_coca_2 = int(input("Số lượng ly coca thực đơn 2: "))
    return {
        "so_dui_ga": so_dui_ga,
        "so_tui_khoai_tay": so_tui_khoai_tay,
        "so_ly_nuoc_chanh": so_ly_nuoc_chanh,
        "so_ly_coca": so_ly_coca,
        "thuc_don_1": {
            "gia": gia_thuc_don_1,
            "dui_ga": dui_ga_1,
            "tui_khoai_tay": tui_khoai_tay_1,
            "ly_nuoc_chanh": ly_nuoc_chanh_1,
            "ly_coca": ly_coca_1,
        },
        "thuc_don_2": {
            "gia": gia_thuc_don_2,
            "dui_ga": dui_ga_2,
            "tui_khoai_tay": tui_khoai_tay_2,
            "ly_nuoc_chanh": ly_nuoc_chanh_2,
            "ly_coca": ly_coca_2,
        },
    }
    # return {
    #     "so_dui_ga": 0,
    #     "so_tui_khoai_tay": 100,
    #     "so_ly_nuoc_chanh": 165,
    #     "so_ly_coca": 0,
    #     "thuc_don_1": {
    #         "gia": 30,
    #         "dui_ga": 0,
    #         "tui_khoai_tay": 1,
    #         "ly_nuoc_chanh": 3,
    #         "ly_coca": 0,
    #     },
    #     "thuc_don_2": {
    #         "gia": 50,
    #         "dui_ga": 0,
    #         "tui_khoai_tay": 2,
    #         "ly_nuoc_chanh": 3,
    #         "ly_coca": 0,
    #     },
    # }
