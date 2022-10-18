N = int(input())

arr = [list(map(int, list(input()))) for _ in range(N)]

def quadTree(arr) :
    print(arr)
    # tmp = list()

    # for i in arr :
    #     tmp.extend(set(i))
    
    # tmp = set(tmp)

    # if len(tmp) == 1 :
    #     print(tmp)
    # else :
    idx = N//2-1
    print(idx)
    arr1, arr2, arr3, arr4 = [], [], [], []
    for i in range(0, N//2):
        tmp1, tmp2, tmp3, tmp4 = [], [], [], []
        for j in range(0, N//2):
            print(arr[i][j], arr[idx+i][j], arr[i][idx+j], arr[idx+i][idx+j])
            tmp1.append(arr[i][j])
            tmp2.append(arr[idx+i][j])
            tmp3.append(arr[i][idx+j])
            tmp4.append(arr[idx+i][idx+j])
        arr1.append(tmp1)
        arr2.append(tmp2)
        arr3.append(tmp3)
        arr4.append(tmp4)

    quadTree(arr1)

        
quadTree(arr)