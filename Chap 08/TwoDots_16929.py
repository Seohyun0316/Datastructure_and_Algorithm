import sys
sys.setrecursionlimit(10000)

def dfs(x, y, px, py, color):
    # 현재 노드를 방문 처리
    visited[x][y] = True

    # 상하좌우 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 범위 내에 있는 경우만 탐색
        if 0 <= nx < n and 0 <= ny < m:
            # 다음 노드가 같은 색상인 경우
            if graph[nx][ny] == color:
                # 부모 노드가 아니라면
                if not visited[nx][ny]:
                    if dfs(nx, ny, x, y, color):  # 재귀 호출
                        return True
                # 부모 노드가 아니고 방문한 노드라면 사이클
                elif (nx, ny) != (px, py):
                    return True
    return False

# 입력 처리
n, m = map(int, input().split())
graph = [input().strip() for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# DFS 시작
for i in range(n):
    for j in range(m):
        if not visited[i][j]:  # 방문하지 않은 점에 대해
            if dfs(i, j, -1, -1, graph[i][j]):  # 부모 노드는 없으므로 (-1, -1)
                print("Yes")
                sys.exit()

print("No")
