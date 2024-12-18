# A forest is more than its trees: haplotypes and ancestral recombination graphs

Repository for the paper: [A forest is more than its trees: haplotypes and ancestral recombination graphs](https://www.biorxiv.org/content/10.1101/2024.11.30.626138v1) by
Halley Fritze, Nathaniel Pope, Jereome Kelleher, and Peter Ralph.

This repository contains jupyter notebooks and pyfiles used to generate the data and figures used in this paper. 

Our methods `extend_haplotypes` and `ARF` can be found in the [`tskit`](https://tskit.dev/software/tskit.html) and [`tscompare`](https://tskit.dev/software/tscompare.html) libraries respectively.

Additionally we provide the file `edgewise_tally_unary_spans.py` which can be used to find what percentage of spans in a tree sequence are coalescent.