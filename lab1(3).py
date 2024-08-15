#ATCG counts
#Step 1: First store the fasta file in a variable

file = 'sequence.fasta'

#step 2: Define four variables for each base and set them equal to zero initially
adenine = 0
guanine = 0
thymine = 0
cytosine = 0


#step 3:Remove unnecessary characters in the fasta file and save the cleaned sequence in a newly defined variable
with open(file) as f:
    for line in f:
        if line != '\n':
            line = line.strip()
            if '>' not in line:
                sequence = repr(line).upper()

#step 4:for each base in the saved sequence increment the adenine base count if base equals 'A'
#step 5:repeat the previous step for all other bases
                for base in sequence:
                    if 'A' in base:
                        adenine += 1
                    if 'G' in base:
                        guanine += 1
                    if 'T' in base:
                        thymine += 1
                    if 'C' in base:
                        cytosine += 1

#step 6 :print the count of each base

print("Adenine count is", adenine)
print("Guanine count is", guanine)
print("Thymine count is", thymine)
print("Cytosine count is", cytosine)
