from collections import deque

def bfs(n, k):
    # 방문 체크 배열: 한 번 방문한 위치를 다시 방문하지 않도록 함
    visited = [0] * 100001  # 0~100000까지의 위치를 표시 (초기값은 0)

    # BFS를 위한 큐 생성 및 초기값 추가
    queue = deque([n])  # 시작 위치를 큐에 추가

    while queue:
        current = queue.popleft()  # 현재 위치를 큐에서 꺼냄
        
        # 목표 위치에 도달한 경우, 걸린 시간을 반환
        if current == k:
            return visited[current]
        
        # 다음으로 이동 가능한 세 가지 경우를 큐에 추가
        for next_pos in (current - 1, current + 1, current * 2):
            # 이동 가능한 범위는 0~100000, 방문하지 않은 위치만 탐색
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = visited[current] + 1  # 현재까지 걸린 시간 +1
                queue.append(next_pos)  # 이동한 위치를 큐에 추가

# 입력 받기
n, k = map(int, input().split())  # 수빈이 위치 n, 동생 위치 k

# BFS 실행 후 결과 출력
print(bfs(n, k))
