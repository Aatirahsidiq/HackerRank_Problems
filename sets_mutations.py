n=int(input())
s=set(map(int,input().split()))
N= int(input())
for i in range(N):
    (command,length)=input().split()
    other_set=set(map(int,input().split()))
    if command=="update":
        s.update(other_set)
    elif command=="intersection_update":
        s.intersection_update(other_set)
    elif command=="difference_update":
        s.difference_update(other_set)
    elif command=="symmetric_difference_update":
        s.symmetric_difference_update(other_set)
print(sum(s))