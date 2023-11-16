import sys
input = sys.stdin.readline

class Node():
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

def preorder(node):
    print(node.item, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end='')
    if node.right != '.':
        inorder(tree[node.right])
    
def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end='')

N = int(input())
tree = {}
for i in range(N):
    node, left, right = input().split()
    tree[node] = Node(node, left, right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])