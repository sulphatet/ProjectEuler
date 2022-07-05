A = {}
B = []
for i in range(100,1000):
    for j in range(100,1000):
        
        B.append(i*j)
C = []
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            num = i + 10*j + 100*k + 1000*k + 10000*j + 100000*i
            if num in B:
                C.append(num)
print(sorted(C))


