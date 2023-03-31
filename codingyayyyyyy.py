#comment number1
temp=0
for i in range(10):
    temp=temp+i
    print("hi sage", i)
    if i%2==0:
        print("hi elliot", i)
    if i%3==0:
        print("cry elliot")
    else:
        print("hi aurora", i)
print(temp)
