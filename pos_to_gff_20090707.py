import os, os.path, pickle, re, sys

directory = sys.argv[1]
label = sys.argv[2]

reg = re.compile(".*(chr..?)_scores.pickle")

files = os.listdir(directory)
for file in [file for file in files if reg.match(file)]:
	scores = pickle.load(open(directory + "/" + file, "r"))
	thematch = reg.match(file)
	chrom = thematch.group(1)
	print chrom
	outfile = open(os.path.join(directory, label + "_" + chrom + ".gff"), "w")
	out = {}
	start = 0
	lastpos = 0
	lastscore = 0
	keys = scores.keys()
	keys.sort()

	for start in keys:
		if start < 0:
			continue
		endpos = scores[start][0]
		score = scores[start][1]
		outfile.write(chrom + "\tNagy\t" + label + "\t" + str(start) + \
		"\t" + str(endpos) + "\t" + str(score) + "\t.\t.\ttcolor=003366;\n")
	outfile.close()
