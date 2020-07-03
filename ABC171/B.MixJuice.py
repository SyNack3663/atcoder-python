N, K = map(int, input().split())
p = map(int, input().split())
sorted = sorted(p)
print(sum(sorted[:K]))
