def solve() -> int:
    n = int(input())
    ps = []
    s = 0
    for i in range(n):
        input_strs = input().split()
        ps.append([int(input_strs[0]), int(input_strs[1])])
        s += ps[-1][0] * ps[-1][1]
    
    for a in range(s, 0, -1):
        t = a
        cnt = {}
        for p in ps:
            while t % p[0] == 0:
                cnt[p[0]] = cnt.get(p[0], 0) + 1
                if cnt[p[0]] > p[1]:
                    break
                t /= p[0]

        if t == 1:
            p_sum = 0
            for p in ps:
                p_sum += p[0] * (p[1] - cnt.get(p[0], 0))
            if p_sum == a:
                return a
    return 0

def solve1() -> int:
    n = int(input())
    arr = []
    for i in range(n):
        input_strs = input().split()
        p, p_num = int(input_strs[0]), int(input_strs[1])
        arr += [p] * p_num
    return dfs(arr, 0, 0, 1)
    
def dfs(arr, idx, s, m) -> int:
    if idx == len(arr):
        if s == m:
            return s
        else:
            return 0
    return max(dfs(arr, idx+1, s+arr[idx], m), dfs(arr, idx+1, s, m*arr[idx]))

num_case = int(input())
for t in range(1, num_case+1):
    ans = solve()
    print("Case #{}: {}".format(t, ans))