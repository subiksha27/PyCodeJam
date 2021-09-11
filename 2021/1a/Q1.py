def solve() -> int:
    n = int(input())
    arr = [int(i) for i in input().split()]
    ans = 0
    pre = None
    for v in arr:
        if pre == None:
            pre = v
            continue
        pre_str = str(pre)
        if v == pre:
            ans += 1
            pre *= 10
        elif v < pre:
            v_s = str(v)
            unit = 10**(len(pre_str) - len(v_s))
            remain = pre - v * unit

            if pre_str.startswith(v_s) and remain+1 < unit:
                ans += len(pre_str) - len(v_s)
                pre += 1
            else:
                while v <= pre:
                    v *= 10
                    ans += 1
                pre = v
        else:
            pre = v
    return ans

num_case = int(input())
for t in range(1, num_case+1):
    ans = solve()
    print("Case #{}: {}".format(t, ans))