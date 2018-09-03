# Copy your PatternMatching function below this line.
# Step 1.4 https://stepik.org/lesson/23144/step/10?unit=6785
# The following lines will automatically read in the Vibrio cholerae genome for you and store it in a variable named v_cholerae
import sys                              # needed to read the genome
input = sys.stdin.read().splitlines()   #  read from 'Vibro_cholerae.txt'
v_cholerae = input[0]                   # store the genome as 'v_cholerae'

# Call PatternMatching with Pattern equal to "CTTGATCAT" and Genome equal to v_cholerae,
# and store the output as a variable called positions
def PatternMatching(Pattern, Genome):
  instance_match = []
  for i in range(len(Genome)):
    if Genome[i:(i+len(Pattern))] == Pattern:
      instance_match.append(i)
  return (instance_match)

# print the positions variable

if __name__ == "__main__":
    pattern = "CTTGATCAT"
    print(PatternMatching(pattern, v_cholerae))
