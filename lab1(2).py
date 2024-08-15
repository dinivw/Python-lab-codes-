#length of a sequence (method 2)
file = 'sequence.fasta'
total_length = 0

with open(file) as f:
    for line in f:
        if line != '\n':
            line = line.strip()
            if '>' not in line:
                length = len(line)
                total_length = total_length + length

print('Length is', total_length)












