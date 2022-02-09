import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])

def home():
	return "<h1>Novozyme Full Stack Assesment</h1><p>API for getting data from https://genome.ucsc.edu/goldenPath/help/api.html#Endpoint/api.genome.ucsc.edu/getData/sequence</p>"

@app.route('/api.genome.ucsc.edu/getData/sequence?genome=hg38;chrom=chrM;start=0;end=20', methods=['GET'])

def api_call():
	response = query_response.json()
	dna_sequence = response.get('dna')
	dna_base = (split(dna_sequence))
	sequence_length = (gc_calculations(dna_base))
	reverse_complement = (reverse_sequence(dna_base))
	values = {"GC Content": sequence_length, "DNA Sequence": dna_sequence, "Reverse Complement": reverse_complement}
	return jsonify(values)


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




app.run()