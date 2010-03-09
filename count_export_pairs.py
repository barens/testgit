import pickle, sys
pairs = pickle.load(open(sys.argv[1], "r"))

totalcount = 0
chroms = pairs.keys()
chroms.sort()
for chrom in chroms:
	chromcount = 0
	chromcount += len(pairs[chrom])
	totalcount += len(pairs[chrom])
	print "%s: %d" % (chrom, chromcount)
print "======"
print "Total: %d" % totalcount