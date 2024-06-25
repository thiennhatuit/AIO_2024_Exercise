import random,math

def cal_MAE(target, predict):
    return abs(target - predict)

def cal_MSE(target, predict):
    return (target - predict)**2 

def cal_RMSE(target,predict):
    return (target - predict)**2

def exercise3():
    n = input("Input number of samples (integer number) which are generated: ")
    if not n.isnumeric():
        print("number of samples must be an integer number")
        return
    f_name = input("Input loss name: ")

    final_loss = 0
    n = int(n)
    
    for i in range(n):
        target = random.uniform(0,10)
        predict = random.uniform(0,10)
        if f_name == "MAE":
            loss = cal_MAE(target, predict)
        elif f_name == "MSE":
            loss = cal_MSE(target,predict)
        elif f_name == "RMSE":
            loss = cal_RMSE(target,predict)

        final_loss += loss
        print(f"loss name: {f_name}, sample: {i}, pred: {predict}, target: {target}, loss: {loss}")

    final_loss = final_loss/n
    if f_name == 'RMSE':
        final_loss = math.sqrt(final_loss)
    print(f"final {f_name}: {final_loss}")

if __name__ == "__main__":
    exercise3()


