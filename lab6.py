#importing needed packages from biopython and re

from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import re

#Loading the fasta file and printing sequence ID, description, Sequence and Sequence length
for seq_record in SeqIO.parse("ATdreb2a.fasta", "fasta"):
    print('Sequence ID:',seq_record.id)
    print('Description:',seq_record.description)
    print('Sequence:',seq_record.seq)
    print('Sequence length:' ,len(seq_record.seq), '\n')

#conducting a blast to the downloaded sequence
record = SeqIO.read("ATdreb2a.fasta", format="fasta")
result_handle = NCBIWWW.qblast("blastn", "nt", record.format("fasta"))
#saving the blast output in a xml file
with open("dreb2a_blast.xml", "w") as out_handle:
    out_handle.write(result_handle.read())

result_handle.close()

#opening the newly created xml file
result_handle = open("dreb2a_blast.xml")
blast_record = NCBIXML.read(result_handle)

E_VALUE_THRESH = 0.05
#count variable in order to calculate total number of hits with the respective pattern
count = 0
#parsing through the blast hits
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        #only the hits with a threshold value less than 0.05 is selected
        if hsp.expect < E_VALUE_THRESH:
            print("****Alignment****")
            #blast hit title
            print("sequence:", alignment.title)
            #blast hit length
            print("length:", alignment.length)
            #blast hit e value
            print("e value:", hsp.expect)
            #blast hit score
            print('Score is',hsp.score)
            #subject sequence
            print('Subject sequence',hsp.sbjct)
            #hit sequence length
            print('Hit sequence length',len(hsp.sbjct),'\n')
            elem = hsp.sbjct

            #pattern that needs to be identified is saved in to a variable
            pattern = '[CT]ACGT[GT]C'
            #finding the pattern in each blast hit
            mos = re.finditer(pattern, elem)

            for item in mos:
                #printing the element that is present
                print('element is:',item.group())
                #printing the location where element is found in the sequence
                print('span is:',item.span(),'\n')
                #if the element is found count is inceased by one
                count += 1

#total count is printed
print('Total count is',count)








