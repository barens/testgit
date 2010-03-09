import sys

infile = open(sys.argv[1], "r")
outfile = open(sys.argv[1].split(".")[0]+".gff", "w")

for line in infile:
	parts = line.split()
	chrom = parts[6].split(".")[0]
	startpos = int(parts[7])
	direction = parts[8]
	if direction == 'R':
		endpos = startpos
		startpos = endpos - 35
	else:
		endpos = startpos + 35
	outfile.write(chrom + "\tNagy\tSolexa\t" + str(startpos) + "\t" + str(endpos) + "\t0\t.\t.\ttcolor=003366;\n")
	
infile.close()
outfile.close()