import sys

T = int(sys.stdin.readline())

arr_zero = [1,0,1]
arr_one = [0,1,1]

def cal(num) :
    if len(arr_zero) <= num :
        for j in range(len(arr_zero), num+1) :
            arr_zero.append(arr_zero[j-1]+arr_zero[j-2])
            arr_one.append(arr_one[j-1]+arr_one[j-2])

    print(f"{arr_zero[num]} {arr_one[num]}")

for i in range(0, T) :
    num = int(sys.stdin.readline())
    cal(num)
