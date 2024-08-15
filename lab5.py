# Python sequence class to store any biological sequence
class Sequences:
    # class variable
    sequence_count = 0

    # constructor to create the objects
    def __init__(self, gene_name, gene_id , species_name, subspecies_name,sequence):
        self.gene_name = gene_name
        self.gene_id = gene_id
        self.sequence_type = Sequences.get_Sequence_Type(Sequences,sequence)
        self.sequence_length = len(sequence)
        self.species_name = species_name
        self.subspecies_name = subspecies_name
        Sequences.sequence_count += 1

# a method to split the fasta file and create a dictionary
    @staticmethod
    def fasta_Split(file):
        # create an empty variable to store the dictionary
        dictionary = {}

        # open the file
        with open(file) as f:
            for line in f:
                if line != '\n':
                    line = line.strip()
        # if > in line split the lines using '-' symbol
                    if '>' in line:
                        newline = line.split('-')
                        # take headers as key in dictionary
                        name = newline[0]
                        # take rest of the values including header as values in dictionary
                        value = newline[0:6]
                        letters = ''
        # if > not in line take the sum of all lines as value in dictionary
                    if '>' not in line:
                        letters += line
                        # take the sum of values and create the dictionary. convert letter variable to list in order to add it to value
                        dictionary[name] = value + [letters]
        return dictionary

# method to get sequence type
    def get_Sequence_Type(self,sequence):
        # create a list containing all proteins except A,G,C and T
        proteinlist = ["M", "N", "R", "S", "I", "Q", "H", "P", "R", "L", "E", "D", "V", "O", "Y", "W", "L", "F", "W"]
        # for each protein in the list for each base in sequence if base equals protein it is a protein sequence
        # if U present in the sequence it is a mRNA sequence
        # else U is absent in the sequence take it as a DNA sequence
        for protein in proteinlist:
            for base in sequence:
                if base == protein:
                    self.sequence_type = 'Protein'
                    return self.sequence_type
                    break


            if "U" in sequence:
                self.sequence_type = 'mRNA'
                return self.sequence_type
                break

            else:
                self.sequence_type = 'DNA'
                return self.sequence_type


# a method to get count of each character in any sequence as a dictionary
    def get_Character_Count(self,sequence):
        # create an empty variable to store the dictionary
        CharacterCount = {}

        # check for each base in the sequence and take base as the key
        # everytime a base is found increase by one and take total count as value
        for base in sequence:
            key = base
            CharacterCount[key] = CharacterCount.get(key, 0) + 1
        return CharacterCount

# subclass to store DNA sequences
class DNAseq(Sequences):

    # constructor
    def __init__(self, gene_id, gene_name,species_name, subspecies_name, sequence):
        super().__init__(gene_id, gene_name,species_name, subspecies_name, sequence)

        self.AT_content = DNAseq.get_ATcontent(DNAseq,sequence)
        self.Transcribed_sequence = DNAseq.transcribe_Sequence(DNAseq,sequence)

    # a method to transcribe a DNA sequence in to mRNA sequence
    def transcribe_Sequence(self, sequence):
        Transcribed_sequence = ''
        # for each base inDNA sequence if T is present replace it with U. If not keep the exisiting base
        for base in sequence:
            if base == 'T':
                Transcribed_sequence += 'U'
            else:
                Transcribed_sequence += base
        self.Transcribed_sequence = Transcribed_sequence
        return self.Transcribed_sequence

    # a method to get the AT content of the DNA sequence
    def get_ATcontent(self, sequence):

        # initialize two variables to store adenine and thymine count and set them equal to zero initially
        adenineCount = 0
        thymineCount = 0

        # for each base in sequence if base equals A increase adenine count by one
        # if base equals T increase thymine count by one
        for base in sequence:
            if base == 'A':
                adenineCount += 1
            if base == 'T':
                thymineCount += 1
        # take total count of adenine and thymine
        count = adenineCount + thymineCount
        # take AT content by dividing total count from length of the sequence
        ATcontent = count/len(sequence)
        self.AT_content = ATcontent
        return self.AT_content

# subclass to store mRNA sequences
class MRNAseq(Sequences):
    # class variable
    # a dictionary which is private
    __Amino_acid_codons = {}

    # a constructor
    def __init__(self, gene_id, gene_name, species_name, subspecies_name, sequence):
        super().__init__(gene_id, gene_name, species_name, subspecies_name, sequence)

        self.AT_content = MRNAseq.get_ATcontent(MRNAseq, sequence)
        self.Translated_sequence = MRNAseq.translate_Sequence(MRNAseq, sequence,codonDiction)

    # a method to get the AT content of mRNA sequence
    def get_ATcontent(self, sequence):

        # initialize two variables to store adenine and thymine count and set them equal to zero initially
        adenineCount = 0
        thymineCount = 0
        # a empty string variable to store the mRNA sequence after converting U letters to T
        newSequence = ''

        # for each base in sequence if U is present convert to T. else keep the existing base and add it to empty string variable created.
        for base in sequence:
            if base == 'U':
                newSequence += 'T'
            else:
                newSequence += base
        # for each base new sequence if A is present increase adenine count by one. If T is present increase thymine count by one
        for base in newSequence:
            if base == 'A':
                adenineCount += 1
            if base == 'T':
                thymineCount += 1
        # take total count
        count = adenineCount + thymineCount
        # divide total count by length of sequence to get AT content
        ATcontent = count / len(newSequence)
        self.AT_content = ATcontent
        return self.AT_content

    # a method to get amino acids and codons pairs from a text file and store it in the empty dictionary created
    @classmethod
    def upload_Codons(cls, file):
        # open the file with codon table and strip each line and then split from where tab space present
        with open(file) as f:
            for line in f:
                if "#" not in line and line != "\t":
                    newline = line.strip().split("\t")
                    # save the codons as the key and relevant amino acid as value in the dictionary
                    codons = newline[0]
                    aminoacid = newline[2]
                    cls.__Amino_acid_codons[codons] = aminoacid
        return cls.__Amino_acid_codons

    # a method to translate the mRNA sequence to amino acid sequence
    def translate_Sequence(self, sequence, codonDiction):
        # empty string variable to save the translated sequence
        outseq = ''
        # for index in the range of length of the sequence starting from zero go through the sequence three by three bases to get the codons
        for i in range(0, len(sequence), 3):
            codon = sequence[i:i + 3]
            # For each codon get the relevant amino acid from the dictionary of amino acids and add it the empty string variable
            outseq += codonDiction[codon]
            # if a stop codon is reached break the for loop
            if codon == 'UAA':
                break
            if codon == 'UGA':
                break
            if codon == 'UAG':
                break
        self.Translated_sequence = outseq
        return self.Translated_sequence

# subclass for storing amino acid sequences
class ProteinSeq(Sequences):
    # constructor
    def __init__(self, gene_id, gene_name, species_name, subspecies_name, uniprot_id, reviewed_status,
                 sequence):
        super().__init__(gene_id, gene_name, species_name, subspecies_name, sequence)

        self.uniprot_id = uniprot_id
        self.reviewed_status = reviewed_status
        self.hydrophobicity = ProteinSeq.get_Hydrophobicity(ProteinSeq, sequence)

    # a method to get the hydrophobicity percentage of sequence
    def get_Hydrophobicity(self, sequence):
        count = 0
        aminoacidlist = ['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']
        for protein in aminoacidlist:
            for base in sequence:
                if base == protein:
                    count += 1

        self.hydrphobicity = count / len(sequence)
        return self.hydrphobicity





# main method

if __name__ == '__main__':

    # fasta file containing the sequences
    file = 'OSDREB_sequences.FASTA'
    # saving the data in fasta file to a dictionary using fasta split method
    Dictionary = Sequences.fasta_Split(file)
    print(Dictionary)

    # take each value from the dictionary and create lists
    for values in Dictionary:
        value = Dictionary[values]
        # sequence is equal to the last index of value list
        sequence = value[-1]

        # object from main class
        gene = Sequences(value[0], value[1], value[2], value[3], sequence)


        # if the type is DNA create DNA object
        if gene.sequence_type == 'DNA':
            DNA = DNAseq(value[0], value[1], value[2], value[3], sequence)

            # gene id, sequence type, sequence length and AT content of DREB1A DNA sequence
            if DNA.gene_name == '>DREB1A_CDS':
                print('For DREB1A DNA sequence','\n','gene id is: ',DNA.gene_id)
                print('sequence type is: ', DNA.sequence_type)
                print('sequence length is: ', DNA.sequence_length)
                print('AT content is: ', DNA.get_ATcontent(sequence), '\n')

            # transcribing the DREB2B DNA sequence
            if DNA.gene_name == '>DREB2B_CDS':
                # transcribed sequence
                seq = DNA.transcribe_Sequence(sequence)
                print('DREB2B mRNA sequence:','\n',seq)

                # creating a mRNA object for the transcribed sequence
                file = 'codon_table.txt'
                codonDiction = MRNAseq.upload_Codons(file)
                mRNA = MRNAseq(value[0], value[1], value[2], value[3], seq)

                # printing the sequence type, length, AT content of transcribed sequence

                print('For DREB2B mRNA sequence' , '\n', 'sequence type is: ', mRNA.sequence_type)
                print('sequence length is: ',mRNA.sequence_length)
                print('AT content is: ', mRNA.AT_content)

                # transcribing the DREB2B mRNA sequence
                translated_seq = (mRNA.translate_Sequence(seq, codonDiction))
                print('Translated sequence of DREB2B: ','\n',translated_seq)
                print('Length of translated sequence: ', len(translated_seq), '\n')


        # if the type is protein create a protein object
        if gene.sequence_type == 'Protein':
            protein = ProteinSeq(value[0], value[1], value[2], value[3], value[4], value[5], sequence)

            # printing uniprot id, reviewed status, type amino acid composition and hydrophobicity for DREB2A protein
            if protein.gene_name == '>DREB2A_P':
                print('For DREB2A amino acid sequence','\n','uniprot id is: ', protein.uniprot_id)
                print('reviewed status is: ', protein.reviewed_status)
                print('sequence type is: ', protein.sequence_type)
                print('amino acid compositon is: ', protein.get_Character_Count(sequence))
                print('hydrophobicity is: ',protein.get_Hydrophobicity(sequence),'\n')


# number of sequences created using sequence class variable
print('Number of sequences created: ', Sequences.sequence_count)




