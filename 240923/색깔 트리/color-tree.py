import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

class Node:
    __slots__ = ['value','children','color','max_depth','have_color','parent']
    def __init__(self, value):
        self.value = value
        self.children = []
        self.color = None
        self.max_depth = None
        self.have_color = set()
        self.parent = None  # 부모 노드를 기록

nodes = {}
root_nodes = {}

def insert_node(m_id, p_id, color, max_depth):
    if p_id == -1:
        root = Node(m_id)
        root.color = color
        root.max_depth = max_depth
        root_nodes[m_id] = root
        nodes[m_id] = root
    else:
        parent = nodes.get(p_id)
        if parent is None or len(parent.children) >= parent.max_depth - 1:
            return
        child = Node(m_id)
        child.color = color
        child.max_depth = max_depth
        child.parent = parent  # 부모 노드 기록
        nodes[m_id] = child
        parent.children.append(child)

def change_color(node, color):
    node.color = color
    for child in node.children:
        change_color(child, color)

def cal_have_color(node):
    if not node.children:  # 리프 노드인 경우
        node.have_color = {node.color}
    else:
        node.have_color = {node.color}
        for child in node.children:
            cal_have_color(child)
            node.have_color.update(child.have_color)

def cal_value(node):
    global total_value
    total_value += len(node.have_color) ** 2
    for child in node.children:
        cal_value(child)

Q = int(input())
for _ in range(Q):
    oper_input = list(map(int, input().split()))
    oper = oper_input[0]
    if oper == 100:
        m_id, p_id, color, max_depth = oper_input[1:]
        insert_node(m_id, p_id, color, max_depth)
    elif oper == 200:
        m_id, color = oper_input[1:]
        node = nodes.get(m_id)
        if node:
            change_color(node, color)
    elif oper == 300:
        m_id = oper_input[1]
        node = nodes.get(m_id)
        if node:
            print(node.color)
        else:
            print("노드가 없습니다")
    else:
        sum_total = 0
        for root in root_nodes.values():
            cal_have_color(root)
            total_value = 0
            cal_value(root)
            sum_total += total_value
        print(sum_total)