A = [0,1]
i = 2
B = []
while True:
    nextElm = A[i-1] + A[i-2]
    A.append(nextElm)
    i +=1
    if A[i-1] > 4000000:
        print(A)
        for j in A:
            if j%2 == 0:
                B.append(j)
        print(sum(B))
        quit()
    
