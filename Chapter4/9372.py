#9372번

import sys
input = sys.stdin.read

def solve():
    data = input().splitlines()
    index = 0
    T = int(data[index])  # 테스트 케이스 개수
    index += 1
    results = []

    for _ in range(T):
        N, M = map(int, data[index].split())  # 국가 수 N, 비행기 종류 M
        index += 1

        # 비행 스케줄 입력 (사실상 사용하지 않음, N-1이 정답이므로)
        for _ in range(M):
            a, b = map(int, data[index].split())
            index += 1

        # 최소 스패닝 트리의 간선 수는 항상 N - 1
        results.append(str(N - 1))

    # 출력
    sys.stdout.write('\n'.join(results) + '\n')

# 실행
solve()
