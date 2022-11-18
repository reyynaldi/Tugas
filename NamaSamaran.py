a = list(map(str, input().split(" ")))

b1 = a[0]
b2 = a[1]

c = str(a[0]).replace(b1[0],b2[0]) 
d = str(a[1]).replace(b2[0],b1[0])

c1 = c+" "
print(c1+d)
