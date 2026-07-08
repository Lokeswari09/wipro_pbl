s = input()
idx = s.find('*')
if idx != -1:
    print(s[:max(0, idx-1)] + s[idx+2:])
else:
    print(s)