s = input()
replaced = s.replace('eraser', '').replace('erase', '').replace('dreamer', '').replace('dream', '')
result = "YES" if len(replaced) == 0 else "NO"
print(result)
