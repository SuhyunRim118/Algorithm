class Node:
    def __init__(self, n, info, left=None, right=None):
        self.n = n
        self.info = info
        self.left = left
        self.right = right
        
    def has_left(self):
        return self.left
    
    def has_right(self):
        return self.right
    
def makeBT(nodeinfo):
    
    nodes = [i for i in range(1, len(nodeinfo)+1)]
    nodes.sort(key=lambda x: (-nodeinfo[x-1][1], nodeinfo[x-1][0]))
    
    root = None
    
    for i in range(len(nodes)):
        if root is None:
            root = Node(nodes[0], nodeinfo[nodes[0]-1])
        else:
            parent = root
            node = Node(nodes[i], nodeinfo[nodes[i]-1])
        
            while True:
                if node.info[0] < parent.info[0]:
                    if parent.has_left() is not None:
                        parent = parent.left
                        continue
                    parent.left = node
                    break
                else:
                    if parent.has_right() is not None:
                        parent = parent.right
                        continue
                    parent.right = node
                    break
    
    return root

def preorder(root, answer):
    stk = [root]
    
    while stk:
        node = stk.pop()
        
        if node is None:
            continue
        
        answer[0].append(node.n)
        stk.append(node.right)
        stk.append(node.left)
    
def postorder(root, answer):
    stk = [(root, False)]
    
    while stk:
        node, visit = stk.pop()
        
        if node is None:
            continue
            
        if visit:
            answer[1].append(node.n)
        else:
            stk.append((node, True))
            stk.append((node.right, False))
            stk.append((node.left, False))
        
def solution(nodeinfo):
    answer = [[], []]
    
    root = makeBT(nodeinfo)
    preorder(root, answer)
    postorder(root, answer)

    return answer