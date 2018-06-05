import sys
import os
import time

def poly_A(seq):
	if(len(seq)>=36):
		count = seq.count("A")
		return ((count/len(seq))*100)
	return 0.0


def calculate(inputFileName, outputFileName):

	C_G = 0
	total_letters = 0
	per_C_G = []
	per_TAG = []
	per_A_36 = []

	with open(inputFileName, 'r') as file:
		data = file.readlines()
		for seq in data:
			stop_codon = 0
			C_G = 0
			letters = 0
			for line in seq:
				# print(c)
				if ">" not in line and "unavailable" not in line:
					for letter in line:

						if letter.lower() == "c" or letter.lower() == "g" :
							C_G += 1
						letters += 1


			percent_C_G = float(C_G)/letters * 100
			stop_codon += seq.count("TAG")
			stop_codon += seq.count("TAA")
			stop_codon ++ seq.count("TGA")

			per_TAG.append((stop_codon/float(letters))*100)#Calculate and store percent TAG
			per_C_G.append(percent_C_G)
			per_A_36.append(poly_A(seq))



	with open(outputFileName, "w") as out:
		out.write("Seq_id\tC_G\tTAG\tper_A_36\n")
		for i in range(0, len(data)):
				out.write("Seq%d\t"% i)
				out.write("%s\t%s\t%s"%(per_C_G[i], per_TAG[i], per_A_36[i]))
				out.write("\n")



def usage():
	'''Informs how to use the file'''
	print("usage: python3 compute.py input_file_name  output_file_name")


if len(sys.argv) < 3:
	usage()

else:
	inputFileName = sys.argv[1]
	
	outputFileName = sys.argv[2]

	# if(os.path.isfile(outputFileName)):
	# 	print("This output file already exists, please supply a non-existant file name")
	calculate(inputFileName, outputFileName)
