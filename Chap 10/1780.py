def solve_1780():
    import sys
    input = sys.stdin.read
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]

    counts = {-1: 0, 0: 0, 1: 0}

    def divide_and_conquer(x, y, size):
        color = paper[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if paper[i][j] != color:
                    third = size // 3
                    for dx in range(3):
                        for dy in range(3):
                            divide_and_conquer(x + dx * third, y + dy * third, third)
                    return
        counts[color] += 1

    divide_and_conquer(0, 0, n)
    print(counts[-1])
    print(counts[0])
    print(counts[1])
