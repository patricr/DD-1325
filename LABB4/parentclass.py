class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def writechain(self,child):

        if child.parent!=None:
            self.writechain(child.parent)

        print(child.word)
        #return (child.word)
