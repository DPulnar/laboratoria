zdanie = input("podaj zdanie")


nowezdanie = ""
for v in zdanie:
    if nowezdanie.count(v)==1:
        nowezdanie += "@"
    else:
        nowezdanie += v
print(nowezdanie)
