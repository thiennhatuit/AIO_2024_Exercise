import math

giaithua = []

def init_giaithua(n = 40):
    giaithua.append(1)
    for i in range(1,41):
        print(f"giai thua {i-1}: ", giaithua[i-1])
        giaithua.append(giaithua[i-1]*i)

def cal_sin(x,n):
    result = 0
    for i in range(n):
        a = (-1)**i
        b = x**(2*i+1)
        c = giaithua[2*i+1]
        result += a*(b/c)
        print(f"{2*i+1} : {giaithua[2*i+1]} : {result}\n")
    return result

def cal_cos(x,n):
    result = 0
    for i in range(n):
        result += (-1)**n*x**(2*i)/giaithua[2*i]
    return result

def cal_sinh(x,n):
    result = 0
    for i in range(n):
        result += x**(2*i+1)/giaithua[2*i+1]
    return result

def cal_cosh(x,n):
    result = 0
    for i in range(n):
        result += x**(2*i)/giaithua[2*i]
    return result

def exercise4():

    x = input("Nhap x: ")
    x = float(x)

    print("X in rad = ", x)

    n = int(input("Nhap so lan n: "))
    
    f_name = input("Chon ham muon tinh: ")
    if f_name == 'sin(x)':
        result = cal_sin(x,n)
    elif f_name == 'cos(x)':
        result = cal_cos(x,n)
    elif f_name == 'sinh(x)':
        result = cal_sinh(x,n)
    elif f_name == 'cosh(x)':
        result = cal_cosh(x,n)

    print(f"{f_name} = {result}")

if __name__ == "__main__":
    init_giaithua()
    exercise4()
    