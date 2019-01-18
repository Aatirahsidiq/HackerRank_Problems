if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N) :
        inputs = input().split()
        if len(inputs) == 3 :
            list.insert(int(inputs[1]),int(inputs[2]))
        elif len(inputs) == 2 :
            if inputs[0] == "append" :
                list.append(int(inputs[1]))
            else :
                list.remove(int(inputs[1]))
        else :
            if inputs[0] == "print" :
                print(list)
            elif inputs[0] == "sort" :
                list.sort()
            elif inputs[0] == "pop" :
                list.pop()
            else :
                list.reverse()