import pickle, sys

dups = pickle.load(open(sys.argv[1], "r"))

totalcount = 0
chroms = dups.keys()
chroms.sort()
for chrom in dups.keys():
	chromcount = 0
	chromcount += len(dups[chrom])
	totalcount += len(dups[chrom])
	print "%s: %d" % (chrom, chromcount)
print "======"
print "Total: %d" % totalcount