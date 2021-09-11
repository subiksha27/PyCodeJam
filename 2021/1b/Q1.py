def solve() -> list:
    hands = [int(i) for i in input().split()]
    re_12 = [i%12 for i in hands]
    re_12.sort()
    

    
    

num_case = int(input())
for t in range(1, num_case+1):
    ans = solve()
    print("Case #{}: {}  {}  {}  {}".format(t, ans[0], ans[1], ans[2], ans[3]))