s = input()
t = input()

while len(t) > len(s):
    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[:-1][::-1]  # 마지막 문자 제거 후 뒤집기

print(1 if s == t else 0)
