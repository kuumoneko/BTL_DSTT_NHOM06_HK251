from typing import Dict
import sympy as sp

def giai_phuong_trinh(phuong_trinh: Dict):
    x, y = sp.symbols("x y") # tạo biến x và y
    results = []
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
            results.append(solution)
    return results
