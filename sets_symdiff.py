n=int(input())
french=set(input().split())
m=int(input())
eng=set(input().split())
R = french.symmetric_difference(eng)
print(len(R))