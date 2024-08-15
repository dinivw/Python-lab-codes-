#import necessary packages
import networkx as nx
from collections import OrderedDict

#importing the tsv file
tsv_file = 'DTIsubset.tsv'

#emptylists
drug_list = []
target_list = []

#creating the network
G = nx.Graph()
with open(tsv_file) as file:
    for line in file:
        if 'Drug_name' not in line:
            line = line.strip().split('\t')
            drug_list.append(line[0])
            #list of drugs
            drugs = list(set(drug_list))
            target_list.append(line[1])
            #list of targets
            targets = list(set(target_list))
            G.add_edge(line[0],line[1])


#empty dictionary to store the CN scores
predicted_drug_target_interactions = {}

#getting the neighbours of each drug
for drug in drugs:
    neighbors_of_drugs = [n for n in G.neighbors(drug)]

    #going through the target list and remove
    #the drug-protein interactions that already exist
    for protein in targets:
        if protein not in neighbors_of_drugs:
            #get the drugs interacted with the targets which
            #don't have interactions with the specific drug
            target_neighbour = [n for n in G.neighbors(protein)]
            #empty list to add all proteins relevant to drugs of
            #non interacting targets
            neighbours_of_targets = []
            #for those drugs get the interacting neighbours
            for t in target_neighbour:
                protein_set = [n for n in G.neighbors(t)]

                #get the union of all proteins relevant to the
                #drugs of non interacting targets and add to a separate list
                neighbours_of_targets += protein_set

                #get the intersection of neighbours of drugs and proteins relevant to drugs of
                #non interacting targets
                intersection = set(neighbours_of_targets).intersection(set(neighbors_of_drugs))

                #calculate the common neighbor score
                cnscore = len(intersection)

                #create the dictionary
                key = drug,protein
                value = cnscore
                predicted_drug_target_interactions[key] = value

#print(predicted_drug_target_interactions)

#sort the dictionary from highest to lowest
sorted_dict = OrderedDict(sorted(predicted_drug_target_interactions.items(),key = lambda x:x[1], reverse = True))

#print the sorted dictionary
print(sorted_dict)

















