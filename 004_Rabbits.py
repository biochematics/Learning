F = open('Files/rosalind_fib.txt', 'r')
x = F.read()
F.close()
val = x.split()
n = int(val[0])
k = int(val[1])

j = 1
s = 0
for i in range(1, n):
    s, j = j+s, k*s
print(j+s)
