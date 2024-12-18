import tskit, msprime, tscompare
import pandas as pd

# Data with varying sample
samplelist = [10, 50, 100, 500, 1000]
sample_arf = pd.DataFrame(columns = samplelist, index=['S', 'SE', 'I', 'IE', 'IS', 'ISE'])
sample_tpr = pd.DataFrame(columns = samplelist, index=['S', 'SE', 'I', 'IE', 'IS', 'ISE'])

for sample in samplelist:
    # generate true tree seqeunce ts and inferred tree sequence infer_ts
    ts = msprime.sim_ancestry(sample, population_size=1000, sequence_length=5e7,
                            recombination_rate=1e-8, coalescing_segments_only=False)
    ts.dump(f'trees/ts_{sample}s_5e7')
    mutation_rate = 1e-7  # mutation rate for the inferred tree sequences
    ts = msprime.sim_mutations(ts, mutation_rate)
    infer_ts = tsinfer.infer(tsinfer.SampleData.from_tree_sequence(ts))
    t = infer_ts.tables
    t.compute_mutation_times()
    infer_ts = t.tree_sequence()
    infer_ts.dump(f'trees/infer_ts_{sample}s_5e7')

    # compare
    sample_arf.loc['I', name], sample_tpr.loc['I', name], _, _, _, _ = tscompare.compare(infer_ts,ts)

    ie = infer_ts.extend_haplotypes()
    sample_arf.loc['IE', name], sample_tpr.loc['IE', name], _, _, _, _ = tscompare.compare(ie,ts)
    
    ss = ts.simplify()
    sample_arf.loc['S', name], sample_tpr.loc['S', name], _, _, _, _ = tscompare.compare(ss,ts)
    
    sse = ss.extend_haplotypes()
    sample_arf.loc['SE',name],  sample_tpr.loc['SE', name], _, _, _, _ = tscompare.compare(sse,ts)

    iis = infer_ts.simplify()
    sample_arf.loc['IS', name], sample_tpr.loc['IS', name], _, _, _, _ = tscompare.compare(iis,ts)

    ise = iis.extend_haplotypes()
    sample_arf.loc['ISE', name], sample_tpr.loc['ISE', name], _, _, _, _ = tscompare.compare(ise,ts)
    
sample_arf.to_csv('figure6-arf-over-sample.csv')
sample_tpr.to_csv('figure6-tpr-over-sample.csv')

# Data with varying sequence length
lengthlist = [1e6, 5e6, 1e7, 3e7, 5e7]
names = ['1e6', '5e6', '1e7', '3e7', '5e7']
length_arf = pd.DataFrame(columns = names, index=['S', 'SE', 'I', 'IE', 'IS', 'ISE'])
length_tpr = pd.DataFrame(columns = names, index=['S', 'SE', 'I', 'IE', 'IS', 'ISE'])

for (length, name) in zip(lengthlist, names):
    # generate true tree seqeunce ts and inferred tree sequence infer_ts
    ts = msprime.sim_ancestry(1000, population_size=1000, sequence_length=length,
                            recombination_rate=1e-8, coalescing_segments_only=False)
    ts.dump(f'trees/ts_1000s_{name}')
    mutation_rate = 1e-7  # mutation rate for the inferred tree sequences
    ts = msprime.sim_mutations(ts, mutation_rate)
    infer_ts = tsinfer.infer(tsinfer.SampleData.from_tree_sequence(ts))
    t = infer_ts.tables
    t.compute_mutation_times()
    infer_ts = t.tree_sequence()
    infer_ts.dump(f'trees/infer_ts_1000s_{name}')

    # compare
    length_arf.loc['I', name], length_tpr.loc['I', name], _, _, _, _ = tscompare.compare(infer_ts,ts)

    ie = infer_ts.extend_haplotypes()
    length_arf.loc['IE', name], length_tpr.loc['IE', name], _, _, _, _ = tscompare.compare(ie,ts)
    
    ss = ts.simplify()
    length_arf.loc['S', name], length_tpr.loc['S', name], _, _, _, _ = tscompare.compare(ss,ts)
    
    sse = ss.extend_haplotypes()
    length_arf.loc['SE',name],  length_tpr.loc['SE', name], _, _, _, _ = tscompare.compare(sse,ts)

    iis = infer_ts.simplify()
    length_arf.loc['IS', name], length_tpr.loc['IS', name], _, _, _, _ = tscompare.compare(iis,ts)

    ise = iis.extend_haplotypes()
    length_arf.loc['ISE', name], length_tpr.loc['ISE', name], _, _, _, _ = tscompare.compare(ise,ts)
    
length_arf.to_csv('figure6-arf-over-length.csv')
length_tpr.to_csv('figure6-tpr-over-length.csv')