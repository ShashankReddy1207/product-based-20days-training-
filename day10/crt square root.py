def s(n,e=1e-6):
    if n<0:
        raise ValueError("cannot compute square")
    if n<1:
        left,right=n,1
    else:
        left,right=0,n
    while abs(left-right)>e:
        mid=(left+right)/2
        mids=mid*mid
        if mids<num:
            left=mid
        else:
            right=mid
    return(left+right)/2
num=int(input())
res=s(num)
print(res)