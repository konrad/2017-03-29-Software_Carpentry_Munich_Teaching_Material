import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

gene_lengths = []
for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
    split_line = line.split()
    if split_line[2] == "gene":
        cur_gene_length = int(split_line[4]) - int(split_line[3])
        gene_lengths.append(cur_gene_length)

plt.hist(gene_lengths, bins=100, color="gray")
plt.savefig("{}_gene_length_distribution.pdf".format(sys.argv[1]))
