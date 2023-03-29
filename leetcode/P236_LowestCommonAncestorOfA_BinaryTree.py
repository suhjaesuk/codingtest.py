def LCA(root, p, q):
    if root == None:
        return None

    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    if root == p or root == q:
        return root
    elif left and right:
        return root
    return left or right


root = [3,5,1,6,2,0,8,None, None, 7,4]
p = 6
q = 4
print(LCA(root, p, q))