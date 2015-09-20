# Labb _1 breddenförst.
#Christopher dahlen, Patric Ridell
import sys
from parentclass import ParentNode
from linkedQFile import LinkedQ

class Node(object):
    """docstring for Node"""
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinTree(object):
    """docstring for BinTree"""
    def __init__(self,):
        self.root = None

    def __contains__(self,value):
        return finns(self.root,value)

    def write(self):
        inorder(self.root)
        print("\n")

    def __contains__(self,value):
        return finns(self.root,value)

    def __str__(self):
        return str(self.root)

    def put(self,newValue):

        self.root = testputta(self.root,newValue)
        #print(self.root)

def testputta(root, newValue):

    if root==None: # första gången vi lägger till nåt.
        newNode=Node(newValue)
        return newNode

    else:
        if newValue < root.value: # sen kollar vi och jämför med tidigare nods värde
            if root.left == None: # om det inte finns nån nod under så lägger vi till en ny nod.
                newNode = Node(newValue)# här ska stå nåt för att få loopen att kliva in i else nästa varv
                root.left=newNode # sätt pekaren på den nya noden
            else:
                testputta(root.left,newValue) # annars gör rekursivrt anrop för att komm längre ned i trädet.

        elif newValue > root.value:
            if root.right == None:
                newNode = Node(newValue)
                root.right = newNode
            else:
                testputta(root.right,newValue)

        return root


def inorder(p):
    if p != None:
        inorder(p.left)
        print(p.value)
        inorder(p.right)

def finns(p,value): #
    if p == None: # kollar om rooten är none
        return False
    if value == p.value:
        return True
    if value < p.value:
        return finns(p.left,value) # nu kollar vi alla sökvägar med rekursion
    if value > p.value:
        return finns(p.right,value)


def makeChildren(startNode):

    alphabet="abcdefghijklmnopqrstuvxyzåäö"
    for x in startNode.word:
        for y in alphabet:
            newWord=startNode.word
            newWord=newWord.replace(x,y)
            #print (newWord)
            if newWord in svenska and newWord not in gamla and newWord!=startNode.word:
                gamla.put(newWord)
                newNode=parentNode(newWord)
                newWord.parent=startNode # föräldren pekar nedåt
                q.enqueue(newWord)


def main():

    with open("word3.txt", encoding="utf8") as ordlista:

        for word in ordlista:
            ordet=word.strip()
            #print (ordet)
            if ordet in svenska:
                gamla.put(ordet) # dumträdet
            else:
                svenska.put(ordet)

    startord= input("startord ")
    slutord= input ("slutord ")

    startNode=ParantNode(startord)
    q.enqueue(startord)

    try:
        while not q.isEmpty():
            nod = q.dequeue()
            if nod == slutord:
                writechain(child).
                #print("det finns en väg till",slutord)
                #raise Klar(kejda)
            else:
                makeChildren(nod)
    except: # ändra här.. den vill inte hoppa in här
        sys.exit("some error message")
        #print("Det finns ABSOLUT INGEN väg till", slutord)






# måste skapa en raise för när det inte finns någon väg.

def Klar(Exception):
    """docstring for felmeddelnade"""
    pass

svenska=BinTree() # skapar trädobjekt GLOBALA HAHA
gamla = BinTree() #dumbarn
q=LinkedQ() ## skapar kön


if __name__ == '__main__':
    main()
