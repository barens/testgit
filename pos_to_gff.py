import os, pickle, re, sys

directory = sys.argv[1]
pat_num = directory[0]

reg = re.compile("s_" + pat_num + "_scores_(chr..?).pickle")

outfile = open("s_" + pat_num + "_scores.gff", "w")
outfile.close()
outfile = open("s_" + pat_num + "_scores.gff", "a")

files = os.listdir(directory)
for file in [file for file in files if reg.match(file)]:
	scores = pickle.load(open(directory + "/" + file, "r"))
	thematch = reg.match(file)
	chrom = thematch.group(1)
	print chrom
	out = {}
	start = 0
	lastpos = 0
	lastscore = 0
	keys = scores.keys()
	keys.sort()

	for pos in keys:
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
		outfile.write(chrom + "\tNagy\ts_" + pat_num + "_Solexa\t" + str(start) + \
		"\t" + str(endpos) + "\t" + str(score) + "\t.\t.\ttcolor=003366;\n")

outfile.close()
