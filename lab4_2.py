#Python sequence class to store any biological sequence

class Sequences:
    #class variable
    sequence_count = 0

    #constructo to create the objects
    def __init__(self, gene_name, gene_id , species_name, subspecies_name,sequence):
        self.gene_name = gene_name
        self.gene_id = gene_id
        self.sequence_type = Sequences.get_Sequence_Type(Sequences,sequence)
        self.sequence_length = len(sequence)
        self.species_name = species_name
        self.subspecies_name = subspecies_name
        Sequences.sequence_count += 1

#a method to split the fasta file and create a dictionary
    @staticmethod
    def fasta_Split(file):
        #create an empty variable to store the dictionary
        dictionary = {}

        #open the file
        with open(file) as f:
            for line in f:
                if line != '\n':
                    line = line.strip()
        #if > in line split the lines using '-' symbol
                    if '>' in line:
                        newline = line.split('-')
                        #take headers as key in dictionary
                        name = newline[0]
                        #take rest of the values including header as values in dictionary
                        value = newline[0:6]
                        letters = ''
        #if > not in line take the sum of all lines as value in dictionary
                    if '>' not in line:
                        letters += line
                        #take the sum of values and create the dictionary. Convert letter variable to list in order to add it to value
                        dictionary[name] = value + [letters]
        return dictionary

#method to get sequence type
    def get_Sequence_Type(self,sequence):
        #create a list containing all proteins except A,G,C and T
        proteinlist = ["M", "N", "R", "S", "I", "Q", "H", "P", "R", "L", "E", "D", "V", "O", "Y", "W", "L", "F", "W"]
        # for each protein in the list if a protein is present take it as a protein sequence
        # if no proteins present and U is absent in the sequence take it as a DNA sequence
        # if no proteins present and U is also present in the sequence take is a mRNA sequence
        for eachprotein in proteinlist:
            if sequence[0] == eachprotein:
                self.sequence_type = 'Protein'
                return self.sequence_type

            if sequence[0] != eachprotein and 'U' not in sequence:
                self.sequence_type = 'DNA'
                return self.sequence_type

            if sequence[0] != eachprotein and 'U' in sequence:
                self.sequence_type = 'mRNA'
                return self.sequence_type

#a method to get count of each character in any sequence as a dictionary
    def get_Character_Count(self,sequence):
        #create an empty variable to store the dictionary
        CharacterCount = {}

        #check for each base in the sequence and take base as the key
        #everytime a base is found increase by one and take total count as value
        for base in sequence:
            key = base
            CharacterCount[key] = CharacterCount.get(key, 0) + 1
        return CharacterCount


if __name__ == '__main__':

    #creating objects

    #save the fasta file in a variable
    file = 'OSDREB_sequences_mRNA.FASTA'
    #use the method created to split fasta file and save the output dictionary in a variable
    Dictionary = Sequences.fasta_Split(file)
    print(Dictionary)

    #take each value in the dictionary
    for values in Dictionary:
        value = Dictionary[values]
        #sequence is the last index of list value
        sequence = value[-1]
        #create object by giving respect indexes of the list 'value'
        gene = Sequences(value[0], value[1], value[2], value[3], sequence)



        if gene.gene_name == '>DREB1A_CDS':
            print(gene.gene_id)
            print(gene.sequence_length)
            print(gene.sequence_type)
            print(gene.get_Character_Count(sequence))


