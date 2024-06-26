

def exercise1(numlist):
    k = int(input("Nhap k"))
    sub_list = []
    result = []

    start_index_list = list(range(0, len(numlist) - k + 1))
    end_index_list = list(range(k,len(numlist)+1))

    for startindex, endindex in zip(start_index_list, end_index_list):
        sub_list = numlist[startindex:endindex]
        result.append(max(sub_list))

    return result

if __name__ == "__main__":
    num_list = []
    print("Nhap num_list: ")
    n = int(input("Nhap so phan tu n: "))
    for i in range(n):
        x = int(input(f"Phan tu thu {i}: "))
        num_list.append(x)

    print(exercise1(num_list))
