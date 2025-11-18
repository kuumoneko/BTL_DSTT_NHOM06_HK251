# main
from src.nhap_du_lieu import nhap_du_lieu
from src.hai_an.giai import bai_hai_an
from src.nhieu_an.giai import bai_nhieu_an

# các bộ test mẫu
# 1: 2 ẩn, nghiệm lẻ
# 2: 2 ẩn, nghiệm chẵn
# 3: 3 ẩn, nghiệm chẵn
# 4: 3 ẩn, nghiệm lẻ
# 5: 4 ẩn, nghiệm lẻ
# 6: 4 ẩn, nghiệm chẵn
# 7: manual
bo_test = 2

dulieu = nhap_du_lieu(bo_test)
print("")
print(
    "Để gây quỹ từ thiện, câu lạc bộ thiện nguyện của một trường THPT tổ chức hoạt động bán hàng với bốn mặt hàng là đùi gà rán, khoai tây chiên, nước chanh, nước coca."
)
print(f"Câu lạc bộ thiết kế {len(dulieu["thuc_don"])} thực đơn.")
for i in range(len(dulieu["thuc_don"])):
    # nếu = 0 thì ko in ra món đó
    print(
        f"Thực đơn {i + 1}: có giá {dulieu["thuc_don"][i]["gia"]} nghìn đồng, bao gồm ",
        end="",
    )
    if dulieu["thuc_don"][i]["dui_ga"] > 0:
        print(f"{dulieu["thuc_don"][i]["dui_ga"]} đùi gà rán", end="")
    if dulieu["thuc_don"][i]["tui_khoai_tay"] > 0:
        if dulieu["thuc_don"][i]["dui_ga"] > 0:
            print(" và ", end="")
        print(f"{dulieu["thuc_don"][i]["tui_khoai_tay"]} túi khoai tây chiên", end="")
    if dulieu["thuc_don"][i]["ly_nuoc_chanh"] > 0:
        if (
            dulieu["thuc_don"][i]["dui_ga"] > 0
            or dulieu["thuc_don"][i]["tui_khoai_tay"] > 0
        ):
            print(" và ", end="")
        print(f"{dulieu["thuc_don"][i]["ly_nuoc_chanh"]} ly nước chanh", end="")
    if dulieu["thuc_don"][i]["ly_coca"] > 0:
        if (
            dulieu["thuc_don"][i]["dui_ga"] > 0
            or dulieu["thuc_don"][i]["tui_khoai_tay"] > 0
            or dulieu["thuc_don"][i]["ly_nuoc_chanh"] > 0
        ):
            print(" và ", end="")
        print(f"{dulieu["thuc_don"][i]["ly_coca"]} ly coca", end="")
    print(".")

# nếu = 0 thì ko in ra món đó
if dulieu["so_dui_ga"] > 0:
    print(
        f"Biết rằng câu lạc bộ chỉ làm được không quá {dulieu["so_dui_ga"]} đùi gà rán",
        end="",
    )
if dulieu["so_tui_khoai_tay"] > 0:
    if dulieu["so_dui_ga"] > 0:
        print(", ", end="")
    print(f"{dulieu["so_tui_khoai_tay"]} túi khoai tây chiên", end="")
if dulieu["so_ly_nuoc_chanh"] > 0:
    if dulieu["so_dui_ga"] > 0 or dulieu["so_tui_khoai_tay"] > 0:
        print(", ", end="")
    print(f"{dulieu["so_ly_nuoc_chanh"]} ly nước chanh", end="")
if dulieu["so_ly_coca"] > 0:
    if (
        dulieu["so_dui_ga"] > 0
        or dulieu["so_tui_khoai_tay"] > 0
        or dulieu["so_ly_nuoc_chanh"] > 0
    ):
        print(", ", end="")
    print(f"{dulieu["so_ly_coca"]} ly coca", end="")
print(".")

print(
    "Số tiền lớn nhất mà câu lạc bộ có thể nhận được sau khi bán hết hàng bằng bao nhiêu nghìn đồng?"
)

print("-" * 60, end="\n\n")

# kiểm tra nếu có 2 ẩn hay không
if len(dulieu["thuc_don"]) == 2:
    bai_hai_an(dulieu)
else:
    bai_nhieu_an(dulieu)
