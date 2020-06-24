n = int(input())
a_arr = list(map(int, input().split()))

count = 0
while all(a % 2 == 0 for a in a_arr):
    count += 1
    a_arr = [a/2 for a in a_arr]

print(count)
