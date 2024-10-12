#백준 11725번

import sys
from collections import defaultdict, deque

input = sys.stdin.read  # 빠른 입력 처리
sys.setrecursionlimit(200000)  # 재귀 깊이 설정

def find_parents(n, graph):
    parents = [0] * (n + 1)  # 각 노드의 부모 정보를 저장할 리스트
    visited = [False] * (n + 1)  # 방문 여부 체크
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:  # 아직 방문하지 않은 경우
                parents[neighbor] = node  # 부모 정보 기록
                dfs(neighbor)  # 재귀 호출로 탐색 진행

    dfs(1)  # 루트 노드 1부터 시작
    return parents

# 입력 받기
data = input().splitlines()
n = int(data[0])  # 노드 개수
graph = defaultdict(list)  # 인접 리스트

# 간선 정보 입력
for i in range(1, n):
    a, b = map(int, data[i].split())
    graph[a].append(b)
    graph[b].append(a)

# 부모 찾기 실행
parents = find_parents(n, graph)

# 결과 출력 (2번 노드부터 부모 정보 출력)
sys.stdout.write('\n'.join(map(str, parents[2:])) + '\n')
