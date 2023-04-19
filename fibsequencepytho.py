def square(size):
    i=0
    for i in range(size):
        print(i**2, "square")


def fibseq(bounds):
    o=1
    t=2
    temp=0
    i=0
    for i in range(bounds):
        if i%2==0:
            temp=+temp
        temp=o+t
        o=t
        t=temp
        i=i+o
        print(temp, "fibseq")
def main():
    number=input("Enter a number for the Range")
    number=int(number)
    square(number)
    fibseq(8)
if __name__=='__main__':
    main()

