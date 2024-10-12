#1167번

import sys
from collections import defaultdict, deque

input = sys.stdin.read  # 빠른 입력 처리

def bfs(start, graph):
    """BFS를 사용해 가장 먼 노드와 그 거리를 찾습니다."""
    distances = [-1] * (len(graph) + 1)  # 각 노드까지의 거리 저장 (-1은 미방문 표시)
    distances[start] = 0  # 시작 노드의 거리는 0
    queue = deque([start])

    max_distance = 0
    farthest_node = start

    while queue:
        node = queue.popleft()
        # 인접한 노드 탐색
        for neighbor, weight in graph[node]:
            if distances[neighbor] == -1:  # 미방문 노드
                distances[neighbor] = distances[node] + weight
                queue.append(neighbor)

                # 최대 거리 갱신
                if distances[neighbor] > max_distance:
                    max_distance = distances[neighbor]
                    farthest_node = neighbor

    return farthest_node, max_distance

def find_tree_diameter(v, graph):
    # 1단계: 임의의 노드(1번)에서 가장 먼 노드를 찾음
    farthest_node, _ = bfs(1, graph)
    # 2단계: 해당 노드에서 가장 먼 노드까지의 거리를 구함 (트리의 지름)
    _, diameter = bfs(farthest_node, graph)
    return diameter

# 입력 받기
data = input().splitlines()
v = int(data[0])  # 정점 개수
graph = defaultdict(list)

# 간선 정보 입력 처리
for line in data[1:]:
    info = list(map(int, line.split()))
    node = info[0]
    for i in range(1, len(info) - 1, 2):
        neighbor = info[i]
        weight = info[i + 1]
        graph[node].append((neighbor, weight))

# 트리의 지름 구하기
diameter = find_tree_diameter(v, graph)
print(diameter)
