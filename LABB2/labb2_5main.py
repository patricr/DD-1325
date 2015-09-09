#from arrayQFile import ArrayQ
from linkedQFile import LinkedQ

def main():

    q=LinkedQ() #skapar kö-objekt

    print("fyller på bakifrån 0->5")
    for i in range(0,6):
        q.enqueue(i)
        # print(q.first)
        print(q.last.value)
    print("tömmer kön framifrån")
    for i in range(0,6):
        print(q.dequeue())

if __name__ == '__main__':
    main()
