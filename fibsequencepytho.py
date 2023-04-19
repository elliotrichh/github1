o=1
t=2
temp=0
i=0
for i in range(8):
    if i%2==0:
        temp=+temp
    temp=o+t
    o=t
    t=temp
    i=i+o
    print (temp)
