import sys

class Queue:
    queue = []

    def push(cls, X) :
        cls.queue.append(X)

    def pop(cls) :
        return cls.queue.pop(0) if cls.queue else -1

    def size(cls) :
        return len(cls.queue)
    
    def empty(cls) :
        return 0 if cls.queue else 1
    
    def front(cls) :
        return cls.queue[0] if cls.queue else -1

    def back(cls) :
        return cls.queue[cls.size()-1] if cls.queue else -1

N = int(sys.stdin.readline())

commend = []

for i in range(0,N) :
    commend.append(sys.stdin.readline().split('\n')[0].split(' '))

queue = Queue()

for j in commend :
    if j[0] == 'front' :
        print(queue.front())
    elif j[0] == 'back' :
        print(queue.back())
    elif j[0] == 'size' :
        print(queue.size())
    elif j[0] == 'empty' :
        print(queue.empty())
    elif j[0] == 'pop' :
        print(queue.pop())
    else :
        queue.push(j[1])
