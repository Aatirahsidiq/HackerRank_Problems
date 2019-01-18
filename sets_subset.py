N=int(input())
for i in range(N):
    a=int(input())
    A=set(input().split())
    b=int(input())
    B=set(input().split())
    print(A.issubset(B))