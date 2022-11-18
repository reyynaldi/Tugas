a = int(input())
b = []

if a<=50 and a>1:
    for i in range(0,a):
        c = input()
        b.append(c)
    print(b)
elif a>50:
    print("Tobi tidak bisa bekerja terlalu keras")
else:
    print("Tobi tidak mau bermalas-malasan")
