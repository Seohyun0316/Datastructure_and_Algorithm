brackets = input()
stack = []
pieces = 0

for i in range(len(brackets)):
    if brackets[i] == '(':  # 여는 괄호일 때 스택에 추가
        stack.append('(')
    else:  # 닫는 괄호일 때
        stack.pop()  # 쇠막대기 하나 끝났으므로 스택에서 하나 제거
        if brackets[i - 1] == '(':  # 레이저인 경우
            pieces += len(stack)  # 현재 스택에 있는 쇠막대기 수만큼 조각 추가
        else:  # 쇠막대기의 끝인 경우
            pieces += 1  # 조각 하나 추가

print(pieces)
