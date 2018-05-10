F = open('Files/rosalind_fib.txt', 'r')
x = F.read()
F.close()
val = x.split()
n = int(val[0])
k = int(val[1])
# rabbitsN = 1
# for month in range(1, n+1):
#     # if month == 1:
#     #     rabbitsN = 1
#     if month == 2:
#         rabbitsN = 1
#         rabbitsP = 1
#     if month > 2:
#         rabbitsN = rabbitsN + rabbitsP*k
#         rabbitsP = rabbitsN - rabbitsP*k
# print(rabbitsN)
# jauni, seni = seni*k,seni+jauni

j = 1
s = 0
for i in range(1, n):
    s, j = j+s, k*s
print(j+s)
