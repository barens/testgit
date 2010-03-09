import os, pickle, re, sys

in_dir = sys.argv[1]
out_name = sys.argv[2]
reg = re.compile(".*(chr[MXY\d]\d?).*\.pickle")
outfile = open(out_name, "w")
outfile.close()
outfile = open(out_name, "a")

files = os.listdir(in_dir)
for f in [f for f in files if reg.match(f)]:
	scores = pickle.load(open(in_dir + "/" + f, "r"))
	thematch = reg.match(f)
	chrom = thematch.group(1)
	print chrom
	out = {}
	start = 0
	lastpos = 0
	lastscore = 0
	keys = scores.keys()
	keys.sort()
	for start in keys:
		if start < 1:
			continue
		endpos = scores[start][0]
		score = scores[start][1]
		if score < 5: continue
		outfile.write(chrom + "\tNagy\tsequencing\t" + str(start) + \
		"\t" + str(endpos) + "\t" + str(score) + "\t.\t.\tcolor=003366;\n")

outfile.close()
