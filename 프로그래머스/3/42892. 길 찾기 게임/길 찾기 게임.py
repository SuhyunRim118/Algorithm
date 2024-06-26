class Node: # Node class
    def __init__(self, xy, n, left=None, right=None):
        self.xy = xy
        self.n = n
        self.left = left
        self.right = right

    def has_left(self):
        return self.left

    def has_right(self):
        return self.right

def make_BT(nodeinfo): # 이진 트리 만들기
    nodes = [i for i in range(1, len(nodeinfo)+1)]
    nodes.sort(key=lambda x: (-nodeinfo[x-1][1], nodeinfo[x-1][0]))
    
    root = None
    
    for i in range(len(nodes)):
        if root is None:
            root = Node(nodeinfo[nodes[0]-1], nodes[0]) # 초기 root 설정
        else:
            parent = root
            node = Node(nodeinfo[nodes[i]-1], nodes[i])
            
            while True: # node가 자리를 찾을 때까지
                # parent보다 작은 x 값 -> 왼쪽
                if node.xy[0]<parent.xy[0]:
                    if parent.has_left() is not None:
                        parent = parent.left
                        continue
                    parent.left = node
                    break
                # parent보다 큰 x 값 -> 오른쪽
                else:
                    if parent.has_right() is not None:
                        parent = parent.right
                        continue
                    parent.right = node
                    break
            
    return root       
    
def pre_order(root, answer): # 전위 순회
    stack = [root]
    
    while stack:
        node = stack.pop()
        
        if node is None:
            continue
            
        answer[0].append(node.n)
        stack.append(node.right)
        stack.append(node.left)
    
def post_order(root, answer): # 후위 순회
    stack = [(root, False)]
    
    while stack:
        node, visit = stack.pop()
        
        if node is None:
            continue
        if visit:
            answer[1].append(node.n)
        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
        
def solution(nodeinfo):
    answer = [[], []]

    root = make_BT(nodeinfo)
    pre_order(root, answer)
    post_order(root, answer)
        
    return answer