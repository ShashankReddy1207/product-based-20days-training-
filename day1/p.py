number=int(input("enter a number"))
for i in range(0,number+1):
    sq=i*i
    sum=0
    while sq>0:
        sum=sum+sq%10
        sq=sq//10
    if i==sum:
        print(i)
   
