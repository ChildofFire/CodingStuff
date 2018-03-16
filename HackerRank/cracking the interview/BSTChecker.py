def BSTHelper(root, minn,maxx):
    if root==None:
        return True
    if root.data<minn or root.data>maxx:
        return False
    return BSTHelper(root.left,minn,root.data-1) and BSTHelper(root.right,root.data+1,maxx)

def checkBST(root):
    return BSTHelper(root,0,10000) #0<=data<=10000 is the problem constraint.