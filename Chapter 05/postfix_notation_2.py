n = int(input())
expression = input()
values = [int(input()) for _ in range(n)]
stack = []

for ch in expression:
    if 'A' <= ch <= 'Z':  # 피연산자인 경우
        stack.append(values[ord(ch) - ord('A')])  # 해당 알파벳에 대응하는 값을 스택에 추가
    else:  # 연산자인 경우
        b = stack.pop()
        a = stack.pop()
        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        elif ch == '/':
            stack.append(a / b)

print(f"{stack[0]:.2f}")  # 결과를 소수점 둘째 자리까지 출력
