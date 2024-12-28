MAX_SIZE = 100

N, M = map(int, input().split())
if N > MAX_SIZE or M > MAX_SIZE:
    exit()

A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
if M > MAX_SIZE or K > MAX_SIZE:
    exit()

B = [list(map(int, input().split())) for _ in range(M)]

C = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for l in range(M):
            C[i][j] += A[i][l] * B[l][j]

for row in C:
    print(" ".join(map(str, row)))
