def swap(l, s, e):
    t = l[s]
    l[s] = l[e]
    l[e] = t

def reverse(l, s, e):
    while s < e:
        swap(l, s, e) 
        s += 1
        e -= 1

T = int(input())
for t in range(1, T+1):
    n, c = [int(i) for i in input().split()]
    if c > (n*(n-1)//2) or c < n-1:
        print("Case #{}: {}".format(t, "IMPOSSIBLE"))
        continue
    l = [i for i in range(1, n+1)]
    c -= n-1
    s = 0
    e = n-1

    x = n-1

    to_left = True
    while c > 0:
        cur = min(c, x)
        c -= cur
        x -= 1
        if to_left:
            reverse(l, s, s + cur)
            e = s + cur - 1
        else:
            reverse(l, e - cur, e)
            s = e - cur + 1
        to_left = not to_left

    

    ans = " ".join(map(lambda x: str(x), l))
    
    print("Case #{}: {}".format(t, ans))
