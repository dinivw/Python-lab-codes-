#step 1 - save the fasta file in a variable
file = "OSDREB1A.fasta"

#step 2 - create an empty dictionary to store the protein and mrna sequences
sequence = {}

#step 3 - open the file and strip each line
with open(file) as f:
    for line in f:
        if line != "\n":
            line = line.strip()
#step 4 - for each line in the file if > is present save it as a key in created dictionary
            if ">" in line:
                name = line
                sequence[name] = ""
                letters = ""

#Step 5 - if > is not present in each line save it as the value
            if ">" not in line:
                letters += line
                sequence[name] = letters

print(sequence)

#Step 6 - create a list with all proteins except for A, G, C and T
proteinlist = ["M", "N", "R", "S", "I", "Q", "H", "P", "R", "L", "E", "D", "V", "O", "Y", "W", "L", "F", "W"]

#Step 7 - create an empty string to store the output mrna sequence
newmrnaseq=""

#Step 8 - for each value in the dictionary store the values in a seperate variable
for value in sequence:
    newseq = sequence[value]

#Step 9 - check if the first letter of values in the previously created variable contains a protein in the protein list and if not save it as the mrna sequence

    for protein in proteinlist:
        if newseq[0] != protein:
            mrnaseq = newseq


#Step 10 - for each base in the mrna sequence if the base is T convert it to U and add it the empty string created to store output sequence
for base in mrnaseq:
    if base == "T":
        newmrnaseq += "U"
    else:
        newmrnaseq += base

print(newmrnaseq)

#Step 11 - create a new variable to store the accession number of the mrna sequence and store it seperately
accession = {i for i in sequence if sequence[i] == mrnaseq}

#Step 12 - pop the accession number out as a string
accession_no = accession.pop()


#step 13 - save the accession number and new mrna sequence in a new fasta file

out_file = open('OSDREB1A_mRNA.fasta', 'w')
out_file.write(accession_no + "transcribed" +  "\n" + newmrnaseq + "\n")






