n=int(input())
if n>=1 and n<=100:
    if n%2==0:
        if n>=2 and n<=4:
            print('Not Weird')
        elif n>4 and n<=20:
            print('Weird')
        elif n>20:
            print('Not Weird')
    else:
        print('Weird') 