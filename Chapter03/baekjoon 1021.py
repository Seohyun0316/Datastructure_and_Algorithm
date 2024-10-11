
#백준 리스트 1021 : 회전하는 큐 문제 풀이

def min_operations(N, M, positions):
    # 큐를 1부터 N까지의 원소로 초기화 (리스트 사용)
    queue = list(range(1, N+1))
    total_operations = 0

    for pos in positions:
        # 현재 큐에서 뽑아내려는 원소의 위치 인덱스를 찾음
        idx = queue.index(pos)

        # 왼쪽으로 이동하는 경우와 오른쪽으로 이동하는 경우의 이동 횟수를 계산
        # 원소까지 왼쪽으로 이동한 수 
        # 오른쪽으로 이동한 수는 큐의 길이에서 왼쪽으로 이동한 수를 빼서 구한다
        left_moves = idx
        right_moves = len(queue) - idx

        # 둘 중, 더 적은 이동 횟수를 선택하고 총 이동 횟수에 더함
        total_operations += min(left_moves, right_moves)

        # 실제로 큐를 이동시키고 첫 번째 원소를 제거
        if left_moves <= right_moves:
            # 왼쪽 이동: 리스트를 idx만큼 pop(0)으로 왼쪽 이동
            for _ in range(left_moves):
                queue.append(queue.pop(0))  # 왼쪽으로 한 칸씩 이동
        else:
            # 오른쪽 이동: 리스트를 idx만큼 pop()으로 오른쪽 이동
            for _ in range(right_moves):
                queue.insert(0, queue.pop())  # 오른쪽으로 한 칸씩 이동
        
        # 첫 번째 원소를 제거 (뽑아냄)
        queue.pop(0)

    return total_operations

# 입력 받기
N, M = map(int, input().split())
positions = list(map(int, input().split()))

# 결과 출력
print(min_operations(N, M, positions))
