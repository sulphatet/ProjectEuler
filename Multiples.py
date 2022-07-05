def three(n):
    if n % 3 == 0:
        return True
    return False
def five(n):
    if n%5 == 0:
        return True
    return False

sum = 0
for i in range(1000):
    if three(i) or five(i):
        sum+=i
print(sum)
