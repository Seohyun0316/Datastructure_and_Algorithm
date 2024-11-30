from collections import deque

def bfs_tomato(graph, n, m):
    # 방향 벡터: 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()

    # 1. 익은 토마토의 위치를 큐에 추가
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:  # 익은 토마토
                queue.append((i, j))

    # 2. BFS 수행
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 범위 내에 있고, 안 익은 토마토(0)일 경우
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1  # 익히고 일수를 기록
                queue.append((nx, ny))  # 다음 탐색을 위해 큐에 추가

    # 3. 결과 계산
    max_days = 0
    for row in graph:
        for cell in row:
            if cell == 0:  # 익지 않은 토마토가 있으면 -1 반환
                return -1
            max_days = max(max_days, cell)

    # 시작이 1이므로 실제 일수는 max_days - 1
    return max_days - 1

# 입력 처리
m, n = map(int, input().split())  # 가로(m), 세로(n)
graph = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(bfs_tomato(graph, n, m))
