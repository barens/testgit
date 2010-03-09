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
	#scores = scores[chrom] # compensating for stupid data storage here...
	outfile = open(os.path.join(directory, "s_" + label + "_" + chrom + ".gff"), "w")
	out = {}
	start = 0
	lastpos = 0
	lastscore = 0
	keys = scores.keys()
	keys.sort()

	for pos in keys:
		pos = int(pos)
		if pos-lastpos != 1 or scores[pos] != lastscore:
			out[start] = [lastpos, lastscore]
			start = pos
			lastscore = scores[pos]
		lastpos = pos

	keys = out.keys()
	keys.sort()
	for start in keys:
		endpos = out[start][0]
		score = out[start][1]
		outfile.write(chrom + "\tNagy\ts_" + label + "_Solexa\t" + str(start) + \
		"\t" + str(endpos) + "\t" + str(score) + "\t.\t.\ttcolor=003366;\n")
	outfile.close()