import math

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def sigmoid(x):
    return 1. / (1+math.e**(-x))

def relu(x):
    return 0 if x <= 0 else x

def elu(x):
    return 0.01*(math.e**x - 1) if x <= 0 else x

def exercise2():
    x = input()
    if not is_number(x):
        print("X must be a number")
        return
    f_name = input()
    if f_name not in ('sigmoid', 'relu', 'elu'):
        print(f"{f_name} is not supported")
        return 
    x = float(x)
    print("Input x = ", x)
    if f_name == 'sigmoid':
        print(f"{f_name}: {f_name}({x}) =", sigmoid(x))
    elif f_name == 'relu':
        print(f"{f_name}: {f_name}({x}) =", relu(x))
    elif f_name == 'elu':
        print(f"{f_name}: {f_name}({x}) =", elu(x))

if __name__ == "__main__":
    exercise2()