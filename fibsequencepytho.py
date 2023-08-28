def fibseq2(bounds):
    fib1=0
    fib2=1
    temp=0




def bubblesort(lists):
    temp=0
    temp1=0
    for i in range( len(lists)-1):
        for j in range(0,len(lists)-1-i):
            if lists[j]> lists[j+1]:
                temp=lists[j]
                temp1=lists[j+1]
                lists[j]=temp1
                lists[j+1]=temp





def triangle(size):
    i=0
    temp=0
    for i in range(size):
        temp=(i*(i+1))//2
        print(temp, "triangle")

def test(size):
    temp = 0
    for i in range(size):
        temp = temp + i
        print(temp,"test")
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
    testlist= [4,1,2,5,3]
    bubblesort(testlist)
    print(testlist)
    triangle(10)
    square(13)
    fibseq(8)
    test(12)
    fibseq2(1)
if __name__=='__main__':
    main()

