import os, os.path, pickle, sys

#thedir = sys.argv[1]
#if not os.path.isdir(thedir):
#	print sys.argv[1], "is not a directory. Please specify the directory containing export files"
#	sys.exit(0)

#files = os.listdir(thedir)
#for fname in files:
fname = sys.argv[1]
# indent the below for directory mode
data = {}
dups = {}
if not fname.endswith(".txt"):
	#continue
	sys.exit(0)
f = open(fname, "r")
for line in f:
	parts = line.split("\t")
	if not parts[10].endswith(".fa"):
		continue
	chrom = parts[10].split(".")[0]
	if chrom not in data:
		data[chrom] = {}
	start = int(parts[12])
	direction = parts[13]
	if direction == "F":
		end = start + 200
	else:
		end = start + 35
		start = start - 165
	if start in data[chrom]:
		thestart = int(start)
		if chrom not in dups: dups[chrom] = {}
		if thestart not in dups[chrom]: dups[chrom][thestart] = 0
		dups[chrom][thestart] += 1
	data[chrom][start] = end

f.close()
outname = fname.split(".")[0] + "_pairs.pickle"
dupsname = fname.split(".")[0] + "_dups.pickle"
pickle.dump(data, open(outname, "w"))
pickle.dump(dups, open(dupsname, "w"))