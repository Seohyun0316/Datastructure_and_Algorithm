def solve_1992():
    import sys
    input = sys.stdin.read
    n = int(input())
    video = [list(map(int, input().strip())) for _ in range(n)]

    result = []

    def divide_and_conquer(x, y, size):
        color = video[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if video[i][j] != color:
                    result.append('(')
                    half = size // 2
                    divide_and_conquer(x, y, half)
                    divide_and_conquer(x, y + half, half)
                    divide_and_conquer(x + half, y, half)
                    divide_and_conquer(x + half, y + half, half)
                    result.append(')')
                    return
        result.append(str(color))

    divide_and_conquer(0, 0, n)
    print(''.join(result))
