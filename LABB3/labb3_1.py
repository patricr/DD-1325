# LABB 3 BINÄRA SÖKTRÄD
#Christopher Dahlen, Patrinc Ridell

# för att kolla i hela sökträdet vill vi söka igenom alla sökvägar och noder.
# vilket görs med rekursion
# preorder används till att stoppa in saker i trädet.
# postorder används när man villstäda i trädet. skräpträd.
#
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


def main():



    svenska=BinTree() # skapar trädobjekt
    with open("word3.txt", encoding="utf8") as sweFile:
        for word in sweFile:
            sweWord=word.strip()
            if sweWord in svenska:
                print (sweWord, end = " ")
            else:
                svenska.put(sweWord)


    engelska=BinTree()
    with open("engelska.txt", encoding="utf8") as engFile:
        for x in engFile:
            row=x.split()
            for i in row:
                engWord=i
                if engWord in engelska:
                    pass
                else:
                    if engWord in svenska:
                        engelska.put(engWord)
                        print(engWord, end = " ")
                    else:
                        pass

    #svenska.put(banan)

    #svenska.contains(gurka)
    #svenska.write()

if __name__ == '__main__':
    main()
