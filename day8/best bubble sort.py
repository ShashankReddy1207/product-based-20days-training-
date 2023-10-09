l=list(map(int,input().split()))
n=len(l)
flag=0
for i in range(1,n):
    for j in range(n-i):
        if l[j]>l[j+1]:
            flag=1
            l[j],l[j+1]=l[j+1],l[j]
    if flag==0:
        break
    flag=0
print(l)
