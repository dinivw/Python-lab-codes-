#Step 1 : Save the fasta file and cododn table in two new variables
file = "OSDREB1A_mRNA.fasta"
file_2 = "codon_table.txt"

#Step 2 : Create a dictionary to save the codons
codontable = {}

#Step 3 : create an empty string to save the mrna sequence to be translated
mrnaseq = ""

#Step 4 : open the file with codon table and strip each line and then split from where tab space present
with open(file_2) as f2:
    for line in f2:
        if "#" not in line and line != "\t":
            newline = line.strip().split("\t")
#Step 5: Save the codons as the key and relevant amino acid as value in the dictionary
            codons = newline[0]
            aminoacid = newline[2]
            codontable[codons] = aminoacid

print(codontable)

#Step 6 : Open the file with mrna sequence
with open(file) as f1:
    for line in f1:
#Step 7 : for each line in file if > is not present add it to the empty string variable created to store the mrna sequence
        if ">" not in line:
            line = line.strip()
            mrnaseq += line;

print(mrnaseq)
print(len(mrnaseq))

#Step 8 : Create a new variable to save the output amino acid sequence
outseq = ""

#step 9 : Using a while loop go through the mrna sequence in three by three bases to get the codons
start = -3
while start < len(mrnaseq):
    start = start + 3
    codon = mrnaseq[start: start + 3]
#Step 10 : For each codon get the relevant amino acid from the dictionary of amino acids and add it the empty string
    outseq += codontable[codon]

    # print(codon)
#Step 11: If a stop codon is reached break the while loop
    if codon == "UAA":
        break
    elif codon == "UGA":
        break
    elif codon == "UAG":
        break



print(outseq)
#Step 12 : get the length of the output amino acid sequence
print(len(outseq))

#Step 13 : Save the amino acid sequence in a new fasta file
out_file = open('protein.fasta', 'w')
out_file.write(outseq + "\n")




