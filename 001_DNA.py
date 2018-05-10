F = open('Files/rosalind_dna.txt', 'r')
x = F.read()
F.close()
d = {'A':0, 'C':0, 'G':0, 'T':0}
for word in x:
    if word in d.keys():
        d[word] = d[word]+1
print (d['A'], d['C'], d['G'], d['T'])
