import sys, pickle

infile = open(sys.argv[1], "r")
data = {}
dups = {}
for line in infile:
	parts = line.split()
	if len(parts) < 9:
		continue
	if not parts[6].endswith(".fa"):
		continue
	chrom = parts[6].split(".")[0]
	if chrom not in data:
		data[chrom] = {}
	start = int(parts[7])
	start_back = start
	direction = parts[8]
	if direction == "F":
		end = start + 35
	else:
		end = start + 35
	if start in data[chrom]:
		if chrom not in dups: dups[chrom] = {}
		if start_back not in dups[chrom]: dups[chrom][start_back] = 0
		dups[chrom][start_back] += 1
	data[chrom][start] = end
	
infile.close()
outname = sys.argv[1].split(".")[0] + "_pairs.pickle"
dupsname = sys.argv[1].split(".")[0] + "_dups.pickle"
pickle.dump(data, open(outname, "w"))
pickle.dump(dups, open(dupsname, "w"))