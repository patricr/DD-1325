# LABB 3 BINÄRA SÖKTRÄD
#Christopher Dahlen, Patric Ridell


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


    def put(self,newValue):

        self.root = testputta(self.root,newValue)
        #print(self.root)


# def putta(root, newValue):
#     # print(root.value)
#     if root==None:
#         newNode=Node(newValue)
#         return newNode
#     else:
#         #print(root.value)
#         if newValue<root.value:
#             if root.left==None:
#                 root.left=Node(newValue)
#             else:
#                 putta(root.left,newValue)
#
#         elif newValue > root.value:
#             if root.right != None:
#                 print("stegar nedåt till höger")
#                 putta(root.right,newValue)
#             elif root.right == None:
#                 root=None
#                 return putta(root,newValue)
#         return root


def testputta(root, newValue):

    if root==None:
        newNode=Node(newValue)
        return newNode

    else:
        if newValue < root.value:
            if root.left == None:
                newNode = Node(newValue)# här ska stå nåt för att få loopen att kliva in i else nästa varv
                root.left=newNode
            else:
                testputta(root.left,newValue)

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

    # with open("engelska.txt", encoding="utf8") as sweFile:
    #     for row in sweFile:
    #         for word in row:
    #             sweWord=word.strip()
    #             print (sweWord)

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
