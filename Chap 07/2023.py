import math

def is_prime(number):
    # 소수 판별 함수
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def generate_super_primes(current, n):
    # 신기한 소수를 찾는 백트래킹 함수
    if len(str(current)) == n:
        print(current)  # n자리 신기한 소수를 찾으면 출력
        return
    
    for digit in range(1, 10):  # 다음 자리에 1부터 9까지의 숫자 추가 시도
        next_number = current * 10 + digit  # 다음 숫자 생성
        if is_prime(next_number):  # 새로운 숫자가 소수인지 확인
            generate_super_primes(next_number, n)  # 재귀적으로 탐색

def main():
    n = int(input())  # N값 입력 받기
    # 1자리 소수로 시작
    for start in [2, 3, 5, 7]:  # 1자리 소수
        generate_super_primes(start, n)

main()
