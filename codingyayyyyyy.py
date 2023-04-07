fib=1
fib2=2
temp=0
i=0

while temp <=4000000:
    temp = fib2
    if temp % 2 == 0:
        i += temp
    temp = fib + fib2
    fib = fib2
    fib2 = temp

print (i)
print("again, sorry for being late, i did use some online help to figure out how to get here, but can assure you there has been no copying, double checked the answer before uploading")

