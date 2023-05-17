
def even():
    a=0
    temp=0
    while a<=100000:
        if a%2==0:
            temp+=a
        a=a+1

    print("the sum of all even numbers to 10000 are",temp)

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



def odd():
    b=0
    tempA=0
    while b<=100000:
       if b%2!=0:
           tempA+=b
       b=b+1

    print("the sum of all odd numbers to 100000 are",tempA)

def main():
    triangle_numbers()
    evenfib()
    odd()
    even()

if __name__=="__main__":
    main()
