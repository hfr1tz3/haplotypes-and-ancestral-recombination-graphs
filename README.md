# A forest is more than its trees: haplotypes and ancestral recombination graphs

Repository for the paper: [A forest is more than its trees: haplotypes and ancestral recombination graphs](https://www.biorxiv.org/content/10.1101/2024.11.30.626138v1) by
Halley Fritze, Nathaniel Pope, Jereome Kelleher, and Peter Ralph.

This repository contains jupyter notebooks and pyfiles used to generate the data and figures used in this paper. 

Our methods `extend_haplotypes` and `ARF`, `TPR` can be found in the [`tskit`](https://tskit.dev/software/tskit.html) and [`tscompare`](https://tskit.dev/software/tscompare.html) libraries respectively.

Additionally we provide the file `edgewise_tally_unary_spans.py` which can be used to find what percentage of spans in a tree sequence are coalescent vs strictly unary.

## Simulations and Figures

If you wish to run simulations for yourself and generate figures, you can do so using the files in each subfolder of the folder `figures/`.

Clone this repository with

`$ git clone https://github.com/hfr1tz3/haplotypes-and-ancestral-recombination-graphs.git`

### Runtime and Compression

For simulations related to the runtime and edge compression of `extend_haplotypes`, see `figures/figure4-runtime`.

To generate data run:

`$ bash do_experiments.sh`

which simulates ARGs, see `constant_pop.py` and `one_pop.py`, on chromosome 1 of *Canis familiaris*. Edge counts and runtimes are computed with `run_experiment.py` and stored as a `.json` file.

To plot results (figure and supplements), run:

`$ bash plot_experiments.sh`

This will create figures from the previous `.json` file from running files `jsons-to-csv.py` and `plot_results.py`.

### Accuracy with True Tree Sequences

For simulations related to the accuracy of the `extend_haplotypes` method, see `figures/figure5-accuracy`.

To generate data run:

`$ python create-data.py`

This will generate a simulated tree sequence using `msprime`, remove portions isolated unary nodes using `remove_isolated_unary.py`, run `extend_haplotypes` and then compute totals of added spans and their proportion of correctness using `get_span_stats`. The data is saved as `nodespans.csv`.

To generate figures run (both figure 5 and the its supplement):

`$ python plot_figure.py`

### Comparison with ARF and TPR

For simulations related to the comparison of inferred ARGs from simulated ARGs, see `figures/figure6-compare`.

To generate data run:

`$ python create-data.py`

This will generate simulated tree sequences using `msprime`, create an inferred tree sequence using `tsinfer` and `tsdate`, and removes their isolated unary nodes using `remove_isolated_unary.py`. With various parameters, `create_data.py` compares the original simulated tree sequence with variants tree sequences using `tscompare.compare`.
Data is stored as four seperate csv files. **Warning** using the default parameters will some time to compute (up to 24 hrs).

To plot data run:

`$ python plot_figure.py`
