# 행렬 크기 제한
MAX_SIZE = 100

# 행렬 곱셈을 위한 스트라센 알고리즘 구현
def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    # 행렬 크기 절반으로 나누기
    mid = n // 2
    
    # 행렬 A의 4개의 부분 행렬
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    
    # 행렬 B의 4개의 부분 행렬
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]
    
    # 7개의 곱셈을 수행
    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, subtract(B12, B22))
    M4 = strassen(A22, subtract(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(subtract(A21, A11), add(B11, B12))
    M7 = strassen(subtract(A12, A22), add(B21, B22))
    
    # 결과 행렬 C를 계산
    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)
    
    # C11, C12, C21, C22 합쳐서 최종 행렬 C 반환
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])
        
    return C

# 행렬 덧셈
def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

# 행렬 뺄셈
def subtract(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

# 행렬 크기 입력 및 제한
N, M = map(int, input().split())
if N > MAX_SIZE or M > MAX_SIZE:
    exit()

A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
if M > MAX_SIZE or K > MAX_SIZE:
    exit()

B = [list(map(int, input().split())) for _ in range(M)]

# 행렬 크기 맞추기 (패딩 추가)
max_size = 1
while max_size < max(N, M, K):
    max_size *= 2

# A와 B를 max_size x max_size로 패딩
def pad_matrix(A, size):
    return [row + [0] * (size - len(row)) for row in A] + [[0] * size for _ in range(size - len(A))]

A_padded = pad_matrix(A, max_size)
B_padded = pad_matrix(B, max_size)

# 스트라센 알고리즘으로 곱셈
C_padded = strassen(A_padded, B_padded)

# 결과 행렬 C 출력
for i in range(N):
    print(" ".join(map(str, C_padded[i][:K])))
