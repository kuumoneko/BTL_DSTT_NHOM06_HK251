import matplotlib.pyplot as plt
import numpy as np


def ve_do_thi(phuong_trinh, x_range, y_range, do_phan_giai=800):
    """
    Vẽ đồ thị các phương trình và tô màu vùng thỏa mãn ve_trai <= ve_phai, x>=0, y>=0.

    Args:
        phuong_trinh (list): Danh sách các phương trình, mỗi phương trình là một dict
                                      có dạng {"ve_trai": "...", "ve_phai": "..."}.
        x_range (tuple): Phạm vi cho trục x, ví dụ: (0, 10).
        y_range (tuple): Phạm vi cho trục y, ví dụ: (0, 10).
        do_phan_giai (int): Độ phân giải của lưới đồ thị.
    """
    # Tạo lưới tọa độ
    x = np.linspace(x_range[0], x_range[1], do_phan_giai)
    y = np.linspace(y_range[0], y_range[1], do_phan_giai)
    X, Y = np.meshgrid(x, y)

    fig, ax = plt.subplots(figsize=(8, 8))

    # Khởi tạo vùng thỏa mãn điều kiện là toàn bộ lưới
    # np.ones_like(X, dtype=bool) tạo ra một mảng có cùng kích thước với X và chứa toàn giá trị True
    vung_thoa_man = np.ones_like(X, dtype=bool)

    # Lặp qua từng phương trình để vẽ đường và cập nhật vùng thỏa mãn
    for i, pt in enumerate(phuong_trinh):
        ve_trai_str = pt["ve_trai"]
        ve_phai_str = pt["ve_phai"]

        # Sử dụng eval() để tính giá trị của biểu thức tại mỗi điểm trên lưới
        # Cảnh báo: eval() có thể không an toàn nếu chuỗi đầu vào không đáng tin cậy.
        # Ở đây chúng ta giả định các phương trình được định nghĩa an toàn trong code.
        if ve_phai_str == 0 or ve_trai_str == 0:
            continue
        ve_trai_val = eval(str(ve_trai_str), {"x": X, "y": Y, "np": np})
        ve_phai_val = eval(str(ve_phai_str), {"x": X, "y": Y, "np": np})

        # 1. Vẽ đường phương trình (vế trái = vế phải)
        ax.contour(X, Y, ve_trai_val - ve_phai_val, levels=[0], colors=f"C{i}")

        # 2. Cập nhật vùng thỏa mãn bất đẳng thức (vế trái <= vế phải)
        vung_thoa_man = np.logical_and(vung_thoa_man, ve_trai_val <= ve_phai_val)

    # Thêm điều kiện x >= 0 và y >= 0
    vung_thoa_man = np.logical_and(vung_thoa_man, X >= 0)
    vung_thoa_man = np.logical_and(vung_thoa_man, Y >= 0)

    # 3. Tô màu vùng thỏa mãn tất cả các điều kiện
    # ax.imshow() sẽ hiển thị mảng boolean dưới dạng hình ảnh
    ax.imshow(
        vung_thoa_man,
        origin="lower",
        extent=(x_range[0], x_range[1], y_range[0], y_range[1]),
        cmap="Greens",
        alpha=0.5,
    )
    ax.legend("lmao")
    # Cấu hình đồ thị
    ax.set_xlabel("Trục X")
    ax.set_ylabel("Trục Y")
    ax.set_title("Đồ thị các phương trình và vùng thỏa mãn bất đẳng thức")
    ax.grid(True, which="both", linestyle="--", linewidth=0.5)
    ax.axhline(y=0, color="k")
    ax.axvline(x=0, color="k")
    ax.set_xlim(x_range)
    ax.set_ylim(y_range)
    ax.set_aspect("equal", adjustable="box")

    plt.show()
