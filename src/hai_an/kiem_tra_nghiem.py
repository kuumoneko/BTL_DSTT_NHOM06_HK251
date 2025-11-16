# kiểm tra tính hợp lệ của nghiệm
def kiem_tra_nghiem(nghiem):
    results = []
    for i in range(len(nghiem)):
        if str(nghiem[i]).count("/") > 0:
            return "co nghiem le"
        if str(nghiem[i]).count("-") > 0:
            continue
        if str(nghiem[i]).count("x") > 0:
            continue
        if str(nghiem[i]).count("y") > 0:
            continue
        if results.count(nghiem[i]) > 0:
            continue
        results.append(nghiem[i])
    if len(results) == 0:
        return "vo nghiem"
    return results
