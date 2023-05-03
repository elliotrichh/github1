def triangle_numbers():
    temp=0
    for i in range(100000):
        t=i*(i+1)//2
        if t <100000:
            temp+=t
    print("the sum of all triangle numbers below 100k is", temp)

def evenfib():
    a=1
    b=2
    temp=0
    while b<=1:
        if b%2==0:
            temp+=b
        a=a+1
    print("the sum of all even fibonacci numbers below 100k is", temp)






def main():
    triangle_numbers()
    evenfib()

if __name__=="__main__":
    main()
