def s(l,si,li):
    if si==li:
        return l[si]
    if si>li:
        return -1
    mid=(si+li)//2
    return s(l,si,mid)+s(l,mid+1,li)
l=list(map(int,input().split()))
si=0
li=len(l)-1
print(s(l,si,li))
