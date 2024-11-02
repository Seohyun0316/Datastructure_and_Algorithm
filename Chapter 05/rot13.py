text = input()
result = []

for ch in text:
    if 'A' <= ch <= 'Z':  # 대문자일 경우
        result.append(chr((ord(ch) - ord('A') + 13) % 26 + ord('A')))
    elif 'a' <= ch <= 'z':  # 소문자일 경우
        result.append(chr((ord(ch) - ord('a') + 13) % 26 + ord('a')))
    else:  # 알파벳이 아닌 경우
        result.append(ch)

print("".join(result))
