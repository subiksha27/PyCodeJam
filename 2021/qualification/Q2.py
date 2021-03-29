T = int(input())
for t in range(1, T+1):
    x, y, s = input().split()
    x = int(x)
    y = int(y)
    cur = s[0]
    ans = 0
    for c in s:
        if c == '?':
            continue
        elif c == 'C':
            if cur == 'J':
                ans += y
            cur = c
        elif c == 'J':
            if cur == 'C':
                ans += x
            cur = c
    print("Case #{}: {}".format(t, ans))