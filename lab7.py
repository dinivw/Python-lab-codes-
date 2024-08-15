#importing needed packages
import networkx as nx
from collections import OrderedDict

#saving the known proteins list file in a variable
file = "AT_stress_proteins.txt"

#creating an empty list to add known proteins
known = []

#taking the names of the known proteins in the file and appending it to the empty list of known proteins
with open(file) as file:
    for line in file:
        if line != '\n':
            line = line.strip().split("\t")
            name = line[1].upper()
            known.append(name)

#removing duplicates from the known protein list
known_proteins = list(set(known))

#print(len(known_proteins))

#saving the file with network proteins in a variable
tsv_file = "string_interactions_short2.tsv"

#creating the network
G = nx.Graph()

with open(tsv_file) as file:
    for line in file:
        if "#" not in line:
            line = line.strip().split('\t')
            G.add_edge(line[0].upper(), line[1].upper())

#printing the degree of DREB2A protein
print("Degree of DREB2A is",(G.degree('DREB2A')))

#creating the list with all the proteins in the network
network = G.nodes()

#removing duplicates from the network
network_proteins = list(set(network))

#create a list of unknown proteins by finding the network proteins which are not in the known protein list
unknown_protein = set(network_proteins).difference(set(known_proteins))

#printing the number of unknown proteins
print('Number of unknown proteins :',len(unknown_protein))

#creating an empty dictionary
dictionary = {}

#go thorugh each unknown protein
for p in unknown_protein:
    #set initial count to zero
    count = 0
    #taking the neighbours of each unknown protein
    neighbors = G.neighbors(p)
    #for each unknown protein if neighbour is a known protein increase the count by one
    for neighbor in neighbors:
        for pro in known_proteins:
            if neighbor == pro:
                #print(p,neighbor,pro)
                count += 1
    #add the  protein and respective score to the empty dictionary
    protein = p
    Majority_score = count
    dictionary[protein] = Majority_score

#sort the dictionary in descending order
sorted_dict = OrderedDict(sorted(dictionary.items(),key = lambda x:x[1], reverse = True))

print(sorted_dict)

#create a new file to save the output
outfile = open('Output.txt', 'w')

#save the proteins and thir majority scores as list in the output file
for key,value in sorted_dict.items():
    outfile.write(str(key) + '-' + str(value) + '\n')


outfile.close()
