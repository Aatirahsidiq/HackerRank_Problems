if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    res2=set(arr)
    res3=sorted(res2,reverse=True)
    print(list(res3)[1])
