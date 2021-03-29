def swap(n, i: int, j: int):
    t = n[i]
    n[i] = n[j]
    n[j] = t

def reverse(n, i: int, j: int):
    while i < j:
        swap(n, i, j)
        i += 1
        j -= 1
        

num_case = int(input())
for t in range(num_case):
    n = int(input())
    l = [int(idx) for idx in input().split()]
    ans = 0
    for i in range(n-1):
        e = i
        for j in range(i, n):
            if l[j] < l[e]:
                e = j
        reverse(l, i, e)
        ans += e-i+1
    print("Case #{}: {}".format(t+1, ans))