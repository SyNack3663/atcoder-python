n = input()[-1]
result = 'hon'
if n == '3':
    result = 'bon'
elif n == '0' or n == '1' or n == '6' or n == '8':
    result = "pon"
print(result)