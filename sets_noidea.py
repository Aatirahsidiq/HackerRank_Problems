n, m = list(input().split())
sc_ar = list(input().split())
A = set(input().split())
B = set(input().split())
happiness=0
for i in sc_ar:
    if i in A:
        happiness+=1
    elif i in B:
        happiness-=1
print(happiness)