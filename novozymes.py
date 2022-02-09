#coding challenge for novozymes

from typing import List
import requests
import json
import operator



"""	PRINT AND TAKE INTPUT FROM USER

print("welcome to novozyme api caller, please enter in the following: ")
chromo = input("Present desired chromosome of interest: ")
print(chromo)

start_sequence = input("Enter location on where to start on returned sequence: ")
print(start_sequence)

end_sequence = input("Enter location on where to end on returned sequence: ")
print(end_sequence)

params = {'chrom': 'chromo', 'start': 'start_sequence', 'end': 'end_sequence'}	

url = "https://api.genome.ucsc.edu/getData/sequence?genome=hg38;chrom={chromo};start={start_sequence};end={end_sequence}"
genome = {'genome': genome} #to be used if going off of user input rather than default{
	genome = input("Provided desired genome to use: ")
	#handling of blank entry
	if genome == " ":
		genome == "hg38"

}
chrom = {'chrom': chromo}
start = {'start': start_sequence}
end = {'end': end_sequence}

#filter ={'chrom': chromosome, 'start': start_sequence, 'end': end_sequence}

"""


	

url = "https://api.genome.ucsc.edu/getData/sequence?genome=hg38;chrom=chrM;start=0;end=20"
#print(url)
query_response = requests.get(url)
#print(query_response)
response = query_response.json()
dna_sequence = response.get('dna')


"""
split is used to take dict value and split into individual chars, gc_calculations is
used to find the GC Content value
"""
def split(dna_sequence):
	return [char for char in dna_sequence]

def gc_calculations(dna_base):
	count = 0
	gc_count = 0
	for i in dna_base:
		count += 1
		if i == "G" or i == "C":
			gc_count += 1
	gc_content = gc_count/count
	return gc_content

def reverse_sequence(dna_base):
	forward_base = dna_base
	reverse_values = {"T": "A", "A": "U", "G": "C", "C": "G", "N": "N"}
	reverse_base = []	

	#for loops to go through both the reverse alues and that of the dna sequence
	for base in forward_base:
		for rev in reverse_values:
			if base in rev:
				reverse_base.append(reverse_values[rev])
	#reverse the order of the dna sequence
	reverse_base = reverse_base[::-1]
	#concat the values into a single string
	revComplement_base = ''.join(map(str,reverse_base))
	#handling to deal with the U and T values
	revComplement_base = revComplement_base.replace("U", "T")

	return revComplement_base



dna_base = (split(dna_sequence))
sequence_length = (gc_calculations(dna_base))
reverse_complement = (reverse_sequence(dna_base))

values = {"GC Content": sequence_length, "DNA Sequence": dna_sequence, "Reverse Complement": reverse_complement}
print(values)


