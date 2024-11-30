from collections import deque

def find_cycle_and_distances(n, edges):
    # 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # 순환선 찾기 (DFS)
    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                parent_map[neighbor] = node
                result = dfs(neighbor, node)
                if result:  # 순환선 확인 시 반환
                    if node in result:  # 순환선의 끝점이 아직 아님
                        return result
                    return result + [node]  # 순환선 끝점 포함
            elif neighbor != parent:  # 순환 발견
                return [neighbor, node]
        return None
    
    visited = [False] * (n + 1)
    parent_map = {}
    cycle = dfs(1, -1)  # 순환선 찾기
    
    # 순환선인지 여부 표시
    in_cycle = [False] * (n + 1)
    for node in cycle:
        in_cycle[node] = True
    
    # 거리 계산 (BFS)
    distances = [-1] * (n + 1)
    queue = deque()
    for node in cycle:
        distances[node] = 0  # 순환선의 거리 = 0
        queue.append(node)
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:  # 아직 방문하지 않은 정점
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    return distances[1:]

# 입력 처리
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n)]
distances = find_cycle_and_distances(n, edges)

# 출력
print(" ".join(map(str, distances)))
