import pickle, sys

directory = sys.argv[1]
scores = pickle.load(open("scores_by_position.pickle", "r"))

total = 0
covered = 0
uncovered = {}
for chrom in exons.keys():
	uncovered[chrom] = []
	print chrom
	for span in exons[chrom]:
		for locus in range(span[0], span[1]+1):
			total += 1
			if locus in scores[chrom] and scores[chrom][locus] >= 2:
					covered += 1
			else:
				uncovered[chrom].append(locus)

print covered*1.0/total
pickle.dump(uncovered, open("uncovered_loci.pickle", "w"))