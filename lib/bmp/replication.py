# Cell Replication
# Helper Functions to help identify the origin of replication or simply 'ori' for a given genome

# find the instances of pattern in a text of genome
def PatternMatch(Pattern, Genome):
  instance_match = []
  for i in range(len(Genome)):
    if Genome[i:(i+len(Pattern))] == Pattern:
      instance_match.append(i)
  return (instance_match)

# find the n occurences of pattern instances in a text of genome
def CountPatternMatch(Pattern, Genome):
  return len(PatternMatch(Pattern, Genome))

# similar implemmentation of counting patterns in genome string
# Reference: 1.2 https://stepik.org/lesson/23143/step/12?unit=6783
# 'a final' k-mer of a string of length n, begins at position n-K of string Genome
def PatternCount(Genome, Pattern):
    count = 0
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            count += 1
    return count

def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = CountPatternMatch(Pattern, Text)
    return Count

# Remove duplicated items from list
def remove_duplicates(Items):
    ItemsNoDuplicates = [] # output variable
    for i in Items:
        if not i in ItemsNoDuplicates:
            ItemsNoDuplicates.append(i)
    return ItemsNoDuplicates
#

def MostFrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates


# Find the frequency for a given length of Pattern (K-mer) in a given genome sequence
# Inputs: (CGATATATCCATAG, 3)
# Output: {'CGA': 1, 'GAT': 1, 'ATA': 3, 'TAT': 2, 'ATC': 1, 'TCC': 1, 'CCA': 1, 'CAT': 1, 'TAG': 1}
#
def PatternFrequency(Genome, Length_of_Pattern):
    patterns = {}
    pattern_frequency = {}
    n = len(Genome)
    k = Length_of_Pattern
    for i in range(n-k+1):
        Pattern = Genome[i:i+k]
        patterns[Pattern] = 0
    for pattern in patterns.keys():
      pattern_frequency[pattern] = PatternCount(Genome, pattern)
    return pattern_frequency



# Identify all the possible K-mers in a genome string.
# K-mer, is simply a pattern of length N.
def Find_K_mers(Text, maxN):
  dict = {}
  for i in range(1, maxN+1):
    print (i,  ":" , MostFrequentWords(Text, i))


def ReversePattern(Pattern):
    return Pattern[::-1]

def PatternComplement(Pattern):
    Complementaries = { 'A' : 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    Complement = ""
    for char in Pattern:
        Complement += Complementaries[char]
    return Complement

def PatternReverseComplement(Pattern):
    return (PatternComplement(ReversePattern(Pattern)))

# Find out the reverse complment of a genome string or K-mer string.
# Reverse complement, completes the attachment and replication for a given K-mer or genome sequence.
def ReverseComplement(Text):
  reverse_string = Text[::-1]
  complementaries = { "A": "T", "G": "C", "T": "A", "C": "G"}
  reverse_complement = []
  for char in (reverse_string):
    reverse_complement.append(complementaries[char])
  print(''.join(reverse_complement))


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


# https://stepik.org/lesson/23059/step/8?unit=6791
# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(ExtendedGenome[i:i+(n//2)], symbol)
    return array


# https://stepik.org/lesson/23060/step/3?unit=6792
def SkewArray(Genome):
  n = len(Genome)
  Skew={}
  Skew[0] = 0
  for i in range(1,n+1):
    symbol = Genome[i-1]
    if symbol == 'A' or symbol == 'T':
      Skew[i] = Skew[i-1]
    elif symbol == 'C':
      Skew[i] = Skew[i-1]-1
    elif symbol == 'G':
      Skew[i] = Skew[i-1]+1
  return Skew

def SkewArray(genome):
    values = {'A':0, 'T':0, 'C':-1, 'G':1}
    skew = [0]
    for i, n in enumerate(genome):
        skew.append(skew[i] + values[n])
    return skew



# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    skewarray = SkewArray(Genome)
    skewarray_min = min(skewarray.values())
    for position in skewarray.keys():
      skew = skewarray[position]
      if skew == skewarray_min:
        positions.append(position)
    return positions

def HammingDistance(p, q):
    mismatch = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            mismatch += 1
    return mismatch

# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    # your code here
    pattern_length = len(Pattern)
    for i in range(len(Text)-len(Pattern)+1):
        K_mer=Text[i:i+pattern_length]
        if HammingDistance(Pattern, K_mer) <= d:
            positions.append(i)
    return positions


def ApproximatePatternCount(Pattern, Text, d):
    count =0  # initializing count
    # your code here
    pattern_length = len(Pattern)
    for i in range(len(Text)-len(Pattern)+1):
        K_mer=Text[i:i+pattern_length]
        if HammingDistance(Pattern, K_mer) <= d:
            count +=1
    return count
