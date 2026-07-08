s1 = input()
s2 = input()
if s1 and s2 and s1[-1].lower() == s2[0].lower():
    res = s1 + s2[1:]
else:
    res = s1 + s2
print(res.lower())