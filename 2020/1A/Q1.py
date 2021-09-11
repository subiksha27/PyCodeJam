def solve() -> str:
    n = int(input())
    patterns = []
    for i in range(n):
        patterns.append(input().split("*"))

    
    



T = int(input())
for t in range(1, T+1):
    print("Case #{}: {}".format(t, solve()))