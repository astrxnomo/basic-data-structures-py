def Bintree(r): return [r, [], []]

def insertLeft(root, newBranch):
    t = root[1] # get current left
    root[1] = [newBranch, t, []]
    return root

def insertRight(root,newBranch):
    t = root[2] # get current right
    root[2] = [newBranch, [], t]
    return root

def getRootVal(root): return root[0]

def setRootVal(root,newVal): root[0] = newVal

def getLeftChild(root): return root[1]

def getRightChild(root): return root[2]

# Programa principal

t = Bintree(1)
insertLeft(t,5)
insertRight(t,2)
insertLeft(getRightChild(t),9)
