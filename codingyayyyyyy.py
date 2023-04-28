a=0
b=1
temp=0
while b<100000:
    if b%2==0:
       temp+=b
    a,b=b,a+b
    print(temp)


