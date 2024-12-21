n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
b = [list(map(int, input())) for _ in range(n)]

def flip(x, y):
    for i in range(3):
        for j in range(3):
            a[x + i][y + j] ^= 1  # 0을 1로, 1을 0으로 뒤집기

def is_same():
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True

if n < 3 or m < 3:
    # 3x3 연산이 불가능한 경우
    print(-1 if a != b else 0)
else:
    count = 0
    for i in range(n - 2):
        for j in range(m - 2):
            if a[i][j] != b[i][j]:
                flip(i, j)
                count += 1

    print(count if is_same() else -1)
