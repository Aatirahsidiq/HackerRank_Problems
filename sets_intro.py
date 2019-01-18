def average(array):
    myset=set(array)
    newset=sum(myset)/len(myset)
    return newset
    
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)