t = int(input())

for _ in range(t):
    s = input()

    n = len(s)
    a, b = -1, -1
    found = False

    for i in range(1, n):
        if s[i] != '0':
            a = int(s[:i])
            b = int(s[i:])
            if b > a:
                print(a, b)
                found = True
                break

    if not found:
        print(-1)

