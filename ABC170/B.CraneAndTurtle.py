X, Y = map(int, input().split())

result = "No"
for i in range(X + 1):
    if 2 * i + (X - i) * 4 == Y:
        result = "Yes"

print(result)