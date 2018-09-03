# Find the frequency for a given length of Pattern (K-mer) in a given genome sequence
# Inputs: Genome, Length of a pattern
# Example Output: AAC: 2, AAA: 3, ATC: 4
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


def MostFrequentPatterns(Text, Length_of_Pattern):
    MostFrequentPatterns = []
    pattern_frequency = PatternFrequency(Text, Length_of_Pattern)
    highest_repetition_count = max(pattern_frequency.values())
    for pattern in pattern_frequency.keys():
        if pattern_frequency[pattern] == highest_repetition_count:
            MostFrequentPatterns.append(pattern)
    return MostFrequentPatterns
