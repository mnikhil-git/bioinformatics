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
