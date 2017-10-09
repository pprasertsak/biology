import matplotlib.pyplot as plt

def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    array[0] = Genome[0:n//2].count(symbol)
    for i in range(1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

Genome = "AAAAGGGG"
symbol = "A"

print(FasterSymbolArray(Genome, symbol))

def Skew(Genome):
    skew = {}    
    skew[0] = 0
    for i in range(len(Genome)):
        if Genome[i] == 'C':
            skew[i+1] = skew[i]-1
        elif Genome[i] == 'G':
            skew[i+1] = skew[i]+1
        else:
            skew[i+1] = skew[i]
    return skew

def MinimumSkew(Genome):
    positions = []
    skew = Skew(Genome)
    min_val = min(skew.values())
    positions = [k for k in skew if skew[k] == min_val]
    return positions
    
skew = Skew("CATGGGCATCGGCCATACGCC")
print(' '.join([str(skew[i]) for i in sorted(skew.keys())]))

print(MinimumSkew("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"))

def ApproximatePatternCount(Pattern, Text, d):
    count = 0
    positions = []
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Pattern, Text[i:i+len(Pattern)]) <= d:
            count += 1
            positions.append[i]            
    return count, positions

def HammingDistance(p, q):
    if not len(p) == len(q):
        return None
    
    hd = 0 # hamming distance
    for i in range(len(p)):
        if not p[i] == q[i]:
            hd += 1
    
    return hd

p = "CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG"
q = "ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"
print(HammingDistance(p, q))

Genome = "GATACACTTCCCGAGTAGGTACTG"
skew = Skew(Genome)
print(max(skew, key=skew.get))
print(skew)

###

Genome = open("E_coli.txt").read()

array = FasterSymbolArray(Genome, 'C')
skew = Skew(Genome)

x1, y1 = zip(*sorted(array.items()))
x2, y2 = zip(*sorted(skew.items()))

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(x1, y1)
axarr[1].plot(x2, y2)

plt.show()
