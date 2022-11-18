def kaliseratus(a):
    return a*100
def kurang(a,b):
    return a - b
def split(a):
    return a.split(" ")

case = int(input())
listutama = []
listakhir = []
profit = 0

for i in range(0, case):
    list=input()
    listutama.append(split(list))
    listakhir1 = split(list)[0]
    listakhir2 = split(list)[1]
    listakhir = kaliseratus(kurang(int(listakhir2),int(listakhir1)))
    profit+=listakhir
    i+=1

print(profit)
