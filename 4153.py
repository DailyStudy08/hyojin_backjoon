N = []
while True :
    element = list(map(int, input().split()))
    
    if element == [0,0,0] :
        break
    else :    
        N.append(element)
        continue
     

for i in N :
    tmp = sorted(i)

    if tmp[2]**2 == tmp[1]**2+tmp[0]**2 :
        print("right")
    else : print("wrong")