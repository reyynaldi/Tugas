c = []
d = input()
for i in range(0, int(d)):
    e = (input())
    f = input()
    c.append(e)

a1 = c[0].split(" ")[0]
a2 = c[0].split(" ")[1]
a3 = c[1].split(" ")[0]
a4 = c[1].split(" ")[1]
a5 = c[2].split(" ")[0]
a6 = c[2].split(" ")[1]

b = (int(a2)-int(a1))+(int(a4)-int(a3))+(int(a6)-int(a5))

print(b*100)

