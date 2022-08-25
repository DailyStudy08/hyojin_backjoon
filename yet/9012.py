def is_VPS(str) :
    stack = []
    L, R = '({[', ')}]'

    for i in str:
        if i in L:
            stack.append(i)
        elif i in R:
            try:
                tmp = stack.pop()

                if L.find(tmp) != R.find(i) :
                    return False
            except: return False
        else:
            continue
    else :
        return True

while True:
    VPS = list(input())

    if VPS == ['.'] : break
    else : print("yes" if is_VPS(VPS) else "no")