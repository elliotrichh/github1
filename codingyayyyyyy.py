
def even():
    a=0
    temp=0
    while a<=100000:
        if a%2==0:
            temp+=a
        a=a+1

    print("the sum of all even numbers to 10000 are",temp)


def odd():
    b=0
    tempA=0
    while b<=100000:
       if b%2!=0:
           tempA+=b
       b=b+1

    print("the sum of all odd numbers to 100000 are",tempA)

if __name__ == '__main__':
    even()
    odd()

