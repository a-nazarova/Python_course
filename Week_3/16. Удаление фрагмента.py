s = input()
a = s.find('h')
b = s.rfind('h')
s1 = str(s[0:a])
s2 = str(s[b+1:])
print(s1 + s2)
