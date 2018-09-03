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


import sys                              # needed to read the genome
input = sys.stdin.read().splitlines()   #  read from 'E_coli.txt'
e_coli = input[0]                   # store the genome as 'e_coli'

print(MinimumSkew(e_coli))
