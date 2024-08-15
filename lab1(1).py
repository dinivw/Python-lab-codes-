#length of a sequence
#Step 1: First store the fasta file in a variable

file = 'sequence.fasta'

#Step 2: Introduce another variable (length) and set it equal to 0 initially

length = 0

#Step3: Remove unnecessary characters from the sequence
with open(file) as f:
    for line in f:
        if line != '\n':
            line = line.strip()
        #print(line)
            if '>' not in line:
                print(repr(line))
# Step4:For each line in the DNA sequence go through each letter and increment length by one
                for letter in line:
                    length = length +1

#Step 5: Print the length

print('length is', length)
