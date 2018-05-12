with open('F/test.txt') as file:
    seq = file.read().split()
N = int(seq.pop(0))
seqInt = []
for g in seq:
    seqInt.append(int(g))
print(seqInt)

Dseq = {}
for n in range (0, N):
    Dseq[seqInt[n]] = n
print(Dseq)
s