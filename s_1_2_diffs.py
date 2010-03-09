# Alteration: instead of location by location, get diff of 20 bp averages
import pickle

#therange = range(1,22)
therange = []
therange.append("X")
therange.append("Y")

for i in therange:
	chrom = "chr"+str(i)
	pre = chrom + "\tNagy\ts_1_2_diff\t"
	post = "\t.\t.\ttcolor=FF0000;\n"
	s1 = pickle.load(open("1_25_2_3158B_18/scores/s_1_scores_" +\
				       chrom + ".pickle", "r"))
	print chrom + " 1 loaded"
	s2 = pickle.load(open("2_27_4_3158B_18/scores/s_2_scores_" +\
				       chrom + ".pickle", "r"))
	print chrom + " 2 loaded"

	outfile = open("diffs/s_1_2_diffs_" + chrom + ".gff", "w")

	the_min = min(min(s1.keys()), min(s2.keys()))
	the_max = max(max(s1.keys()), max(s2.keys()))+1

	print "Got bounds"

	last_start = 0
	last_j = the_min-1
	last_diff = 0
	s1_avgs = {}
	s2_avgs = {}
	
	for j in xrange(the_min+19, the_max+1, 20):
		s1_run = 0
		s2_run = 0
		for k in range(j-19, j+1):
			if k in s1:
				s1_run += s1[k]
			if k in s2:
				s2_run += s2[k]
		s1_avgs[j] = s1_run/20.0
		s2_avgs[j] = s2_run/20.0

	for j in xrange(the_min+19, the_max+1, 20):
		diff = abs(s1_avgs[j]-s2_avgs[j])
		if diff != last_diff:
			outfile.write(pre + str(last_start) + "\t" +
				      str(last_j) + "\t" +
				      str(last_diff) + post)
			last_start = j
			last_diff = diff
		last_j = j

	outfile.close()
