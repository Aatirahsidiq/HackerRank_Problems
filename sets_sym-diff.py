m=int(input())
first_set=set(input().split())
n=int(input())
sec_set=set(input().split())
l=first_set.symmetric_difference(sec_set)
z=sorted(l, key=int)
for x in z:
    print(x)