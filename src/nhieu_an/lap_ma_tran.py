def lap_ma_tran(du_lieu):
    ma_tran = [[] for _ in range(4)]
    phuong_trinh_can_tinh = []
    gioi_han = [
        du_lieu["so_dui_ga"],
        du_lieu["so_tui_khoai_tay"],
        du_lieu["so_ly_nuoc_chanh"],
        du_lieu["so_ly_coca"],
    ]
    for i in range(len(du_lieu["thuc_don"])):
        combo = du_lieu["thuc_don"][i]
        duiga = ma_tran[0]
        tui_khoai_tay = ma_tran[1]
        ly_nuoc_chanh = ma_tran[2]
        ly_coca = ma_tran[3]

        duiga.append(combo["dui_ga"])
        tui_khoai_tay.append(combo["tui_khoai_tay"])
        ly_nuoc_chanh.append(combo["ly_nuoc_chanh"])
        ly_coca.append(combo["ly_coca"])
        phuong_trinh_can_tinh.append(-1 * int(combo["gia"]))
    return {
        "ma_tran": ma_tran,
        "phuong_trinh_can_tinh": phuong_trinh_can_tinh,
        "gioi_han": gioi_han,
    }
