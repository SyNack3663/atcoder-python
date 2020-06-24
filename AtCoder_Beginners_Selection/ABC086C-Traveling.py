n = int(input())
t = 0
x = 0
y = 0
result = "Yes"

for i in range(n):
    next_t, next_x, next_y = map(int, input().split(' '))
    diff_t = next_t - t
    diff_x = next_x - x
    diff_y = next_y - y
    diff = abs(diff_x) + abs(diff_y)
    if diff_t % 2 == 0 and diff % 2 == 1:
        result = "No"
    if diff_t % 2 == 1 and diff % 2 == 0:
        result = "No"
    if diff_t < diff:
        result = "No"
    t, x, y = diff_t, diff_x, diff_y

print(result)