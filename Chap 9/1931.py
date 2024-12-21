n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# 끝나는 시간을 기준으로 정렬, 끝나는 시간이 같다면 시작 시간 기준으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

print(count)
