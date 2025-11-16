# main
from src.nhap_du_lieu import nhap_du_lieu
from src.giai import bai_hai_an, bai_nhieu_an

# các bộ test mẫu
# 1: 2 ẩn, nghiệm lẻ
# 2: 2 ẩn, nghiệm chẵn
# 3: 3 ẩn, nghiệm chẵn
# 4: 3 ẩn, nghiệm lẻ
# 5: 4 ẩn, nghiệm lẻ
# 6: 4 ẩn, nghiệm chẵn
# 7: manual
bo_test = 1

dulieu = nhap_du_lieu(bo_test)
# kiểm tra nếu có 2 ẩn hay không
if len(dulieu["thuc_don"]) == 2:
    bai_hai_an(dulieu)
else:
    bai_nhieu_an(dulieu)
