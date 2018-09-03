import operator

def PatternCount(Genome, Pattern):
    count = 0
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            count += 1
    return count

def PatternMatch(Pattern, Genome):
  instance_match = []
  for i in range(len(Genome)):
    if Genome[i:(i+len(Pattern))] == Pattern:
      instance_match.append(i)
  return (instance_match)


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
"""

def E_Coli_ClumpFind( s, k, L, t ):
    print(PatternMatch("AAAAACCAT", s))
"""


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
    pattern_frequency = {}
    n = len(Genome)
    k = Length_of_Pattern
    for i in range(n-k+1):
        Pattern = Genome[i:i+k]
        if Pattern not in pattern_frequency:
            pattern_frequency[Pattern] = 0
        pattern_frequency[Pattern] += 1
    return pattern_frequency

"""
# find the instances of pattern in a text of genome
def PatternMatch(Pattern, Genome):
  instance_match = []
  for i in range(len(Genome)):
    if Genome[i:(i+len(Pattern))] == Pattern:
      instance_match.append(i)
  return (instance_match)
  """

def E_Coli_ClumpFind( s, k, L, t ):
    out = {}
    pattern_frequency = {}
    pattern_instances = {}
    for i in range(len(s)-L-k+1):
        Pattern = s[i:i+k]
        if Pattern not in pattern_frequency:
            pattern_frequency[Pattern] = 1
            pattern_instances[Pattern] = []
        pattern_instances[Pattern].append(i)
        pattern_frequency[Pattern] += 1

    for pattern in pattern_frequency.keys():
        if pattern_frequency[pattern] >= t and pattern not in out:
            out[pattern] = pattern_instances[pattern]
    print(len(out.keys()))

import sys                              # needed to read the genome
input = sys.stdin.read().splitlines()   #  read from 'E_coli.txt'
e_coli = input[0]                   # store the genome as 'e_coli'

s = e_coli
k = 9
L = 500
t = 3

print(E_Coli_ClumpFind(s, k, L, t))
