import datetime, sys

def usage():
	print "Usage: python pair_distribution_counter.py \
/path/to/eland_or_export.txt /path/to/outfile.gff"

def datestamp():
	d = datetime.date.today()
	year = str(d.year)
	month = "0" + str(d.month)
	if d.month > 9:
		month = str(d.month)
	day = str(d.day)
	if d.day < 10:
		day = "0" + str(d.day)
	return year+month+day

if len(sys.argv) < 3:
	usage()
	sys.exit(0)
fname = sys.argv[1]
outname = sys.argv[2]
outfile = open(sys.argv[2], "w")
data = {}
f = open(fname, "r")
if fname.find("export") > 0: # export.txt file
	for line in f:
		parts = line.split("\t")
		if not parts[10].endswith(".fa"):
			continue
		chrom = parts[10].split(".")[0]
		if chrom not in data:
			data[chrom] = {}
			data[chrom]["R"] = []
			data[chrom]["F"] = []
		start = int(parts[12])
		direction = parts[13]
		data[chrom][direction].append(start)
elif fname.find("eland") > 0:
	for line in f:
		parts = line.split()
		if len(parts) < 9:
			continue
		if not parts[6].endswith(".fa"):
			continue
		chrom = parts[6].split(".")[0]
		if chrom not in data:
			data[chrom] = {}
			data[chrom]["R"] = []
			data[chrom]["F"] = []
		start = int(parts[7])
		direction = parts[8]
		data[chrom][direction].append(start)
else:
	print "File isn't labeled as eland or export - please change filename to indicate data type"
	usage()
	sys.exit(0)

source = datestamp() + "_" + fname.split("/")[-1].split(".")[0]
feature = "start_distribution"
for chrom in data:
	rset = set(data[chrom]["R"])
	fset = set(data[chrom]["F"])
	for pos in rset:
		outfile.write("%s\t%s\t%s\t%d\t%d\t-1\t.\t.\t;color=0000FF;\n" % \
			(chrom, source, feature, pos, pos))
	for pos in fset:
		outfile.write("%s\t%s\t%s\t%d\t%d\t1\t.\t.\t;color=FF0000;\n" % \
			(chrom, source, feature, pos, pos))

outfile.close()

