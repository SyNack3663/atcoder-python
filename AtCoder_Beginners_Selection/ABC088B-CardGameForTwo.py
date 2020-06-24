n = int(input())
a = list(map(int, input().split(' ')))

alice = 0
bob = 0
ordered = sorted(a)
for i, num in enumerate(ordered):
    if i % 2 == 0:
        alice += num
    else:
        bob += num

print(abs(alice - bob))
