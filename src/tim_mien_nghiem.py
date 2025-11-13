from typing import Dict
import sympy as sp
from math import floor


def nghiem(nghiemm):
    temp = str(nghiemm).split("{(")[1].split(")}")[0].split(", ")
    if temp[0] == "0":
        try:
            return {
                "x": float(temp[0]),
                "y": float(temp[1]),
            }
        except:
            try:
                a = int(temp[1].split("/")[0])
                b = int(temp[1].split("/")[1])
                return {
                    "x": float(a / b),
                    "y": 0,
                }
            except:
                return {
                    "x": 0,
                    "y": 0,
                }
    else:
        try:
            return {
                "x": float(temp[0]),
                "y": float(temp[1]),
            }
        except:
            try:
                a = int(temp[0].split("/")[0])
                b = int(temp[0].split("/")[1])
                return {
                    "x": float(a / b),
                    "y": 0,
                }
            except:
                return {
                    "x": 0,
                    "y": 0,
                }


def tim_x_va_y(phuong_trinh):
    x, y = sp.symbols("x y")
    x_max = 0
    y_max = 0
    for i in range(len(phuong_trinh["phuong_trinh"])):
        pt1 = sp.Eq(
            phuong_trinh["phuong_trinh"][i]["ve_trai"],
            phuong_trinh["phuong_trinh"][i]["ve_phai"],
        )
        pt2 = sp.Eq(x, 0)
        pt3 = sp.Eq(y, 0)
        solution1 = sp.nonlinsolve([pt1, pt2], [x, y])
        solution2 = sp.nonlinsolve([pt1, pt3], [x, y])
        x_res = nghiem(solution1)["y"]
        y_res = nghiem(solution2)["x"]

        x_max = max(x_max, floor(x_res))
        y_max = max(y_max, floor(y_res))
    return {
        "x_max": x_max,
        "y_max": y_max,
    }


def tim_mien_nghiem(phuong_trinh: Dict):
    results = []
    maxx = tim_x_va_y(phuong_trinh)

    x_max = maxx["x_max"]
    y_max = maxx["y_max"]

    for i in range(x_max + 1):
        for j in range(y_max + 1):
            results.append({"x": i, "y": j})
    return results
