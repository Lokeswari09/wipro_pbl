s = input()
n = len(s)
sub = s[:2] if n >= 2 else s
print(sub * n)