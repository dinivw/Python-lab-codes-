
#method to get AT content of a sequence
def getAdenineThymineCount(sequence):

#initialize two variables to zero
    adenineCount = 0
    thymineCount = 0

#look for adenine or thymine in the sequence and increase the counts
    for Base in sequence:
        if Base == 'A':
            adenineCount += 1
        if Base == 'T':
            thymineCount += 1
#get total AT count
    count = adenineCount + thymineCount
#get AT content bt dividing the total count from length of the sequence
    ATcontent = count / len(sequence)
    return 'AT content is' + " " + str(ATcontent)


#method to split fasta file and return a dictionary
def createDictionary(file):

#create an empty dictionary to store the dictionary
    sequencedictionary = {}

#open the file and strip lines
    with open(file) as f:
        for line in f:
            if line != "\n":
                line = line.strip()
#if > is present in line take them as keys of the dictionary
                if ">" in line:
                    name = line
                    sequencedictionary[name] = ""
                    letters = ""
#if > is not present take the sum of each line as value in dictionary
                if ">" not in line:
                    letters += line
                    sequencedictionary[name] = letters
        return sequencedictionary


#method for finding the sequence type of a given sequence
def sequenceType(sequence):

#create a protein list without A, G, C and T
    proteinlist = ["M", "N", "R", "S", "I", "Q", "H", "P", "R", "L", "E", "D", "V", "O", "Y", "W", "L", "F", "W"]

#for each protein in the list if a protein is present take it as a protein sequence
#if no proteins present and U is absent in the sequence take it as a DNA sequence
#if no proteins present and U is also present in the sequence take is a mRNA sequence
    for eachprotein in proteinlist:
        if sequence[0] == eachprotein:
            return 'Protein'
        if sequence[0] != eachprotein and 'U' not in sequence:
            return 'DNA'
        if sequence[0] != eachprotein and 'U' in sequence:
            return 'mRNA'

#finding the AT content in sequences of fasta file

#save the fasta file in a variable
File = 'OSDREB_sequences.FASTA'

#call the method usedd to create a dictionary and save it in a variable
Dictionary = createDictionary(File)
print(Dictionary)

#Save all the dictionary values(sequences) in a variable
for value in Dictionary:
    sequence = Dictionary[value]

#call the method used to find the type of sequence and save it in a variable
    typeOfSequence = sequenceType(sequence)
    print(sequence)
    print(typeOfSequence)
#if type of sequence is DNA call the method created to find AT content
    if typeOfSequence == 'DNA':
        print((getAdenineThymineCount(sequence)), '\n')
    else:
        print('No AT content', '\n')








