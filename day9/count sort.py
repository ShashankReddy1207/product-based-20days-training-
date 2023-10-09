l=list(map(int,input().split()))
c=[0 for i in range(max(l)+1)]
r=[0]*len(l)
for i in range(len(l)):
    c[l[i]]+=1
for i in range(1,len(c)):
    c[i]+=c[i-1]
for i in range(len(l)):
    r[c[l[i]]-1]=l[i]
    c[l[i]]-=1
print(r)
    
