import os, os.path, pickle, re, sys

files = []
directory = "."
fname = sys.argv[1]
if os.path.isdir(fname):
	directory = sys.argv[1]
	tempfiles = os.listdir(directory)
	for f in tempfiles:
		files.append(os.path.join(directory ,f))
else:
	files.append(fname)

label = sys.argv[2]

for f in files:
	if not f.endswith(".pickle"):
		continue
	scores = pickle.load(open(f, "r"))
	for chrom in scores:
		print chrom
		c_scores = scores[chrom] # compensating for stupid data storage here...
		outfile = open(os.path.join(directory, "s_" + label + "_" + chrom + ".gff"), "w")
		directions = ["R", "F"]
		for d in directions:
			c_d_scores = c_scores[d]
			out = {}
			start = 0
			lastpos = 0
			lastscore = 0
			keys = c_d_scores.keys()
			keys.sort()

			for pos in keys:
				pos = int(pos)
				if pos-lastpos != 1 or c_d_scores[pos] != lastscore:
					out[start] = [lastpos, lastscore]
					start = pos
					lastscore = c_d_scores[pos]
				lastpos = pos

			keys = out.keys()
			keys.sort()
			for start in keys:
				endpos = out[start][0]
				if endpos-start != 1:
					endpos += 1
				score = out[start][1]
				outfile.write(chrom + "\tNagy\ts_" + label + "_dist_Solexa\t" + str(start) + \
				"\t" + str(endpos) + "\t" + str(score) + "\t.\t.\ttcolor=003366;\n")
		outfile.close()