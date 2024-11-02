T = int(input())
for _ in range(T):
    sentence = input()
    print(' '.join(word[::-1] for word in sentence.split()))
