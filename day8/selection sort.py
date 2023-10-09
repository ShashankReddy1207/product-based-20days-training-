l=list(map(int,input().split()))
n=len(l)
for i in range(n-1):
    minn=i
    for j in range(i+1,n):
        if l[j]<l[minn]:
            minn=j
    l[i],l[minn]=l[minn],l[i]
print(l)
