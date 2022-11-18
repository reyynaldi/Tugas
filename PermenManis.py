n=int(input())
budi = list(map(int, input().split()))[:n]
anto = list(map(int, input().split()))[:n]

a = 0
b = 0
i = 0
while i < len(anto):
    if anto[a] > budi[a]:
        b+=1
    i+=1
    a+=1

print(b)
