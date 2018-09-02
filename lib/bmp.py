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


def Find_K_mers(Text, maxN):
  dict = {}
  for i in range(1, maxN+1):
    print (i,  ":" , MostFrequentWords(Text, i))


def ReverseComplement(Text):
  reverse_string = Text[::-1]
  complementaries = { "A": "T", "G": "C", "T": "A", "C": "G"}
  reverse_complement = []
  for char in (reverse_string):
    reverse_complement.append(complementaries[char])
  print(''.join(reverse_complement))

# PatternMatch("TCT", "ATGACTTCGCTGTTACGCGC")
# CountPatternMatch("TCT", "ATGACTTCGCTGTTACGCGC")
"""
def ReverseComplementSuperPro(Pattern):
  return ("".join([{"A":"T", "T":"A", "C":"G", "G":"C"}[x] for x in Pattern][::-1]))


def PatternMatchingPro(Pattern, Genome):
  return (" ".join([str(i) for i in range(len(Genome)) if Genome[i:(i+len(Pattern))] == Pattern]))
print ("The pattern %s appears in positions %s in the genome of Vibrio Colerae" % ("ATGACTTCGCTGTTACGCGC ", PatternMatchingPro("CGC ", "ATGACTTCGCTGTTACGCGC ")))
"""
