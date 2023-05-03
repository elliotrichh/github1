
def even():
    a=0
    temp=0
    while a<=10:
        if a%2==0:
            temp+=a
        a=a+1

        print(temp, "even")


def odd():
    b=0
    tempA=0
    while b<=10:
       if b%3==0:
           tempA+=b
    b=b+1

    print(tempA, "oddd")

if __name__ == '__main__':
    even()
    odd()

