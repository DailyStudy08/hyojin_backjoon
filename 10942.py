import sys

words = []
i = 0

while True :
    words.append(sys.stdin.readline().strip())
    i+=1
    
    if int(words[i-1])<=0 :
        break

words = words[:len(words)-1]
for i in words :
    print('yes' if i[:]== i[::-1] else 'no')