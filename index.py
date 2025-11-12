# setup
import sys

sys.dont_write_bytecode = True

# main
from src.nhap_du_lieu import nhap_du_lieu
from src.tim_phuong_trinh import tim_phuong_trinh
from src.giai_phuong_trinh import giai_phuong_trinh
from src.kiem_tra_nghiem import kiem_tra_nghiem
from src.tim_mien_nghiem import tim_mien_nghiem, nghiem


dulieu = nhap_du_lieu()
phuong_trinh = tim_phuong_trinh(dulieu)
# chèn đoạn code để vẽ đồ thị

# giải phương trình
nghiemm = giai_phuong_trinh(phuong_trinh["phuong_trinh"])
kiem_tra = kiem_tra_nghiem(nghiemm)

result = 0
if kiem_tra == "vo nghiem":
    print("Không có nghiệm hợp lệ")
    exit(0)

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
        result = max(
            result,
            x_val * dulieu["thuc_don_1"]["gia"] + y_val * dulieu["thuc_don_2"]["gia"],
        )

print(f"Số tiền lớn nhất có thể nhận được là: {result} nghìn đồng")
