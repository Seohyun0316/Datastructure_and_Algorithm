from collections import deque  # deque를 사용하여 BFS 구현하는 풀이

def max_distance(grid, n, m):
    queue = deque()  
    # BFS 탐색을 위한 큐 생성 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]  
    # 문제에서 주어진대로 8개의 방향 이동을 설정해준다

    # 모든 아기 상어(1)의 위치를 큐에 삽입해준다
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:  # 격자에서 아기 상어가 있는 경우
                queue.append((i, j))  # 아기 상어의 위치를 큐에 추가

    max_dist = 0  # 최대 거리를 저장할 변수 초기화

    # BFS 탐색을 시작한다, 큐에서 하나씩 아기상어 위치를 꺼내고 8개 방향으로 이동한다.
    while queue:
        x, y = queue.popleft()  # 큐에서 현재 위치를 꺼내준다
        for dx, dy in directions:  # 8방향으로 이동
            nx, ny = x + dx, y + dy  # 새로운 위치 계산
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                # 새로운 위치가 격자 범위 내에 있고, 빈칸(0)인 경우
                grid[nx][ny] = grid[x][y] + 1  # 이전 위치의 거리에서 1 증가
                max_dist = max(max_dist, grid[nx][ny])  # 최대 거리 갱신
                queue.append((nx, ny))  # 새 위치를 큐에 추가

    return max_dist - 1  # 초기값이 1이므로 최종 결과에서는 1을 빼준다

# 입력 받기
n, m = map(int, input().split())  # n: 행 수, m: 열 수 입력
grid = [list(map(int, input().split())) for _ in range(n)]  # 격자(grid) 입력
print(max_distance(grid, n, m))  # 최대 거리를 출력
