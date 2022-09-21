N = int(input())
tree = {}

for i in range(N) :
    node, left, right = input().split()
    tree[node] = [left, right]

#root->left->right
def preorder(root) :
    if root != '.' :
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

#left->root->right
def inorder(root) :
    if root != '.' :
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

#left->right->root
def postorder(root) :
    if root != '.' :
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')