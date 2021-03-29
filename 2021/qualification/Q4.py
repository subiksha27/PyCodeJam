def swap(l, s, e):
    t = l[s]
    l[s] = l[e]
    l[e] = t

T, N, Q = [int(i) for i in input().split()]
for _t in range(T):
    ans = [1, 2, 3]
    print("1 2 3")
    m = int(input())
    swap(ans, 1, m-1)
    
    for cur in range(4, N+1):
        find = False
        s = 0
        e = len(ans)-1
        while s < e:
            m = (s+e) // 2
            print("{} {} {}".format(ans[m], ans[e], cur))
            res = int(input())
            if res == cur:
                if s+1 == e:
                    s += 1
                    break
                s = m
            elif res == ans[m]:
                e = m
            elif res == ans[e]:
                find = True
                ans.insert(e+1, cur)
                break
            elif res == -1:
                raise Exception("failed","number of qureys exceed limit")
        if not find:
            ans.insert(s, cur)
            
    print(" ".join(map(lambda x: str(x), ans)))
    res = int(input())
    if res == 1:
        continue
    else:
        raise Exception("failed","wrong answer")
