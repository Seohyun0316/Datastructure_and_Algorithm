def solve_2630():
    import sys
    input = sys.stdin.read
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]

    white, blue = 0, 0

    def divide_and_conquer(x, y, size):
        nonlocal white, blue
        color = paper[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if paper[i][j] != color:
                    half = size // 2
                    divide_and_conquer(x, y, half)
                    divide_and_conquer(x, y + half, half)
                    divide_and_conquer(x + half, y, half)
                    divide_and_conquer(x + half, y + half, half)
                    return
        if color == 0:
            white += 1
        else:
            blue += 1

    divide_and_conquer(0, 0, n)
    print(white)
    print(blue)
