def find_kth_number(n, k):
    left, right = 1, n * n  # 가능한 수의 범위 (1부터 N*N까지)

    while left <= right:
        mid = (left + right) // 2  # 중간 값을 선택
        count = 0  # 중간 값보다 작거나 같은 수의 개수
        
        # 각 행에서 mid 이하의 원소 수를 세기
        for i in range(1, n + 1):
            count += min(mid // i, n)  # i행에서 mid보다 작은 원소 개수
        
        if count >= k:  # 중간 값보다 작거나 같은 수의 개수가 K 이상이면
            right = mid - 1  # 더 작은 범위에서 탐색
        else:
            left = mid + 1  # 더 큰 범위에서 탐색
    
    return left  # K번째 수 반환

# 입력 받기
n = int(input())  # N값 (배열의 크기)
k = int(input())  # K값 (K번째 작은 수를 찾음)
print(find_kth_number(n, k))  # 결과 출력
