# s -> genome
# k -> k-mer length
# L -> window in genome string
# t -> number of instances of occurences
# len(s) = 9918, k = 9, L = 586, t = 20
# Example Inputs
# s = CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA
# k = 5
# L = 50
# t = 4
def ClumpFind( s, k, L, t ):
    out = []
    print(len(s))
    for start in range(len(s)-L+1):
        window = s[start:start+L]
        counts = {}
        for i in range(len(window)-k+1):
            if window[i:i+k] not in counts:
                counts[window[i:i+k]] = 0
            counts[window[i:i+k]] += 1
        for kmer in counts:
            if counts[kmer] >= t and kmer not in out:
                out.append(kmer)
    return out



import sys                              # needed to read the genome
input = sys.stdin.read().splitlines()   #  read from 'E_coli.txt'
e_coli = input[0]                   # store the genome as 'e_coli'

s = e_coli
k = 9
L = 500
t = 3

print(ClumpFind(s, k, L, t))
