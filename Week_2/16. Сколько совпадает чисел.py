a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b != c or a == c != b or c == b != a:
    print(2)
else:
    print(0)
