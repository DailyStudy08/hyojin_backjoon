import sys

N, K = map(int,sys.stdin.readline().split(' '))

num = list(map(int, sys.stdin.readline().split(' ')))

def selection_sort(A) :
    cnt = 0
    answer = -1

    for last in range(N-1, 0, -1) :
        max = last
        
        for i in range(0, last) :
            if A[max] < A[i] :
                max = i
                cnt += 1

        A[max], A[last] = A[last], A[max]
        print(f'K : {K}/cnt : {cnt}')
        print(A)
        
        if cnt == K :
            answer = f'{A[last]} {A[max]}'
    
    return answer

print(selection_sort(num))