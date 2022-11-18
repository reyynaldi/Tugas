a = list(map(int, input().split(" ")))
i = 0

b=[]
c=[]
 
for i in range(len(a)):
    if a[i] % 2 != 0:
        b.append(a[i])
    i += 1

for i in range(len(a)):
    if a[i]%2==0:
        c.append(a[i])
    i+=1

b.sort(reverse=True)
c.sort(reverse=True)

d = b + c

print(d)
