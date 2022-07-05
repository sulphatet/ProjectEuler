n = 600851475143
A = []
for i in range(1,n):
    if n % i == 0:
        A.append(i)
    print(A)
