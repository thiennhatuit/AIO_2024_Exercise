import math

def md_nre_single_sample():
    target = float(input("Nhap target: "))
    predict = float(input("Nhap predict: "))
    n = int(input("Nhap n: "))
    p = int(input("Nhap p: "))

    return (target**(1/n) - predict**(1/n))**p
if __name__ == "__main__":
    print("result: ",md_nre_single_sample())