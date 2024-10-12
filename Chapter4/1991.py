# 백준 1991번
# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 이진 트리 구성 함수
def build_tree(nodes):
    tree = {}  # 노드를 저장할 딕셔너리

    # 모든 노드를 미리 생성
    for value in nodes:
        tree[value] = Node(value)

    # 트리 구조 구성
    for parent, left, right in nodes.items():
        if left != '.':
            tree[parent].left = tree[left]
        if right != '.':
            tree[parent].right = tree[right]

    return tree['A']  # 항상 A가 루트 노드

# 전위 순회 (Preorder): 루트 -> 왼쪽 -> 오른쪽
def preorder_traversal(node):
    if node is not None:
        print(node.value, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# 중위 순회 (Inorder): 왼쪽 -> 루트 -> 오른쪽
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.value, end=' ')
        inorder_traversal(node.right)

# 후위 순회 (Postorder): 왼쪽 -> 오른쪽 -> 루트
def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=' ')

# 입력 받기
n = int(input("노드의 개수를 입력하세요: "))  # 첫 줄 입력
nodes = {}

print("각 노드와 자식 노드 정보를 입력하세요 (형식: 부모 왼쪽 오른쪽):")
for _ in range(n):
    parent, left, right = input().split()
    nodes[parent] = (left, right)

# 트리 구성
root = build_tree(nodes)

# 결과 출력
print("\nPreorder Traversal:")
preorder_traversal(root)

print("\nInorder Traversal:")
inorder_traversal(root)

print("\nPostorder Traversal:")
postorder_traversal(root)
