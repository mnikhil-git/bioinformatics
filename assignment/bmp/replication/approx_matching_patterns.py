import sys                              # needed to read the genome
input = sys.stdin.read().splitlines()   #  read from 'E_coli.txt'



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


def MostRepeatingPatterns(Text, k):
    pattern_frequency = PatternFrequency(Text, k)
    MostRepeatingPatterns = {}
    most_repetitions = max(pattern_frequency.values())
    for pattern in pattern_frequency.keys():
        if pattern_frequency[pattern] == most_repetitions:
            MostRepeatingPatterns[pattern] = most_repetitions
    return MostRepeatingPatterns



def HammingDistance(p, q):
    mismatch = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            mismatch += 1
    return mismatch

def ApproximatePatternMatchingPositions(Text, Pattern, d):
    positions = [] # initializing list of positions
    # your code here
    pattern_length = len(Pattern)
    for i in range(len(Text)-len(Pattern)+1):
        K_mer=Text[i:i+pattern_length]
        if HammingDistance(Pattern, K_mer) <= d:
            positions.append(i)
    return positions


def ApproximatePatternMatches(Text, Pattern, d):
    approx_patterns = {} # initializing list of positions
    # your code here
    pattern_length = len(Pattern)
    for i in range(len(Text)-len(Pattern)+1):
        K_mer=Text[i:i+pattern_length]
        if HammingDistance(Pattern, K_mer) <= d:
            approx_patterns[K_mer] = 0
    return approx_patterns.keys()



def ApproximatePatternCount(Text, Pattern, d):
    count =0  # initializing count
    # your code here
    pattern_length = len(Pattern)
    for i in range(len(Text)-len(Pattern)+1):
        K_mer=Text[i:i+pattern_length]
        if HammingDistance(Pattern, K_mer) <= d:
            count +=1
    return count


genome = input[0]
pattern_length = 4
hammingdistance_threshold = 1
most_frequent_k_mers = MostRepeatingPatterns(genome, pattern_length)

print("Most Frequent K-mers are" + str(most_frequent_k_mers))

most_frequent_approx_match_kmers = []

approx_matching_k_mers = {}
for k_mer in most_frequent_k_mers:
    print(ApproximatePatternMatches(genome, "CATG", hammingdistance_threshold))
