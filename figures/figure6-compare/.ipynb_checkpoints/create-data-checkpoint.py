import tskit
import pandas as pd
from remove_isolated_unary import remove_isolated_unary
import tscompare
import tsdate
import msprime
import tsinfer

# Data with varying sample
samplelist = [10, 50, 100, 500, 1000]
sample_arf = pd.DataFrame(columns = samplelist, index=['S', 'SE', 'I', 'IE', 'IS', 'ISE'])
sample_tpr = pd.DataFrame(columns = samplelist, index=['S', 'SE', 'I', 'IE', 'IS', 'ISE'])

for sample in samplelist:
    # generate true tree seqeunce ts and inferred tree sequence infer_ts
    ts = msprime.sim_ancestry(sample, population_size=10000, sequence_length=5e7,
                            recombination_rate=1e-8, coalescing_segments_only=False)
    mu = 1.29e-8  # mutation rate for the inferred tree sequences
    ts = msprime.sim_mutations(ts, mu)
    infer_ts = tsinfer.infer(tsinfer.SampleData.from_tree_sequence(ts))
    t = infer_ts.tables
    t.compute_mutation_times()
    infer_ts = t.tree_sequence()
    infer_dated = tsdate.date(tsdate.util.split_disjoint_nodes(infer_ts), 
                      mutation_rate=mu,
                      allow_unary=True,
                      rescaling_intervals=100
                     )
    iid = remove_isolated_unary(infer_dated)
    ts = remove_isolated_unary(ts)
    ts.dump(f'trees/ts_{sample}s_5e7')
    iid.dump(f'trees/infer_dated_ts_{sample}s_5e7')

    # compare
    ID = tscompare.compare(iid, ts)
    sample_arf.loc['I', sample], sample_tpr.loc['I', sample] = ID.arf, ID.tpr

    iide = iid.extend_haplotypes()
    IDE = tscompare.compare(iide, ts)
    sample_arf.loc['IE', sample], sample_tpr.loc['IE', sample] = IDE.arf, IDE.tpr
    
    iids = iid.simplify()
    IDS = tscompare.compare(iids, ts)
    sample_arf.loc['IS', sample], sample_tpr.loc['IS', sample] = IDS.arf, IDS.tpr

    iidse = iids.extend_haplotypes()
    IDSE = tscompare.compare(iidse, ts)
    sample_arf.loc['ISE', sample], sample_tpr.loc['ISE', sample] = IDSE.arf, IDSE.tpr
    
    ss = ts.simplify()
    S = tscompare.compare(ss,ts)
    sample_arf.loc['S', sample], sample_tpr.loc['S', sample] = S.arf, S.tpr
    
    sse = ss.extend_haplotypes()
    SE = tscompare.compare(sse,ts)
    sample_arf.loc['SE', sample],  sample_tpr.loc['SE', sample] = SE.arf, SE.tpr
    
sample_arf.to_csv('figure6-arf-over-sample.csv')
sample_tpr.to_csv('figure6-tpr-over-sample.csv')

# Data with varying sequence length
lengthlist = [1e6, 5e6, 1e7, 3e7, 5e7]
names = ['1e6', '5e6', '1e7', '3e7', '5e7']
length_arf = pd.DataFrame(columns = names, index=['S', 'SE', 'I', 'IE', 'IS', 'ISE'])
length_tpr = pd.DataFrame(columns = names, index=['S', 'SE', 'I', 'IE', 'IS', 'ISE'])

for (length, name) in zip(lengthlist, names):
    # generate true tree seqeunce ts and inferred tree sequence infer_ts
    ts = msprime.sim_ancestry(1000, population_size=10000,
                              sequence_length=length,
                              recombination_rate=1e-8,
                              coalescing_segments_only=False
                             )
    mu = 1.29e-8  # mutation rate for the inferred tree sequences
    ts = msprime.sim_mutations(ts, mu)
    infer_ts = tsinfer.infer(tsinfer.SampleData.from_tree_sequence(ts))
    t = infer_ts.tables
    t.compute_mutation_times()
    infer_ts = t.tree_sequence()
    infer_dated = tsdate.date(tsdate.util.split_disjoint_nodes(infer_ts), 
                      mutation_rate=mu,
                      allow_unary=True,
                      rescaling_intervals=100
                     )
    iid = remove_isolated_unary(infer_dated)
    ts = remove_isolated_unary(ts)
    ts.dump(f'trees/length_ts_1000s_{name}')
    iid.dump(f'trees/infer_dated_length_ts_1000s_{name}')

    # compare
    ID = tscompare.compare(iid, ts)
    length_arf.loc['I', name], length_tpr.loc['I', name] = ID.arf, ID.tpr

    iide = iid.extend_haplotypes()
    IDE = tscompare.compare(iide, ts)
    length_arf.loc['IE', name], length_tpr.loc['IE', name] = IDE.arf, IDE.tpr

    iids = iid.simplify()
    IDS = tscompare.compare(iids, ts)
    length_arf.loc['IS', name], length_tpr.loc['IS', name] = IDS.arf, IDS.tpr

    iidse = iids.extend_haplotypes()
    IDSE = tscompare.compare(iidse, ts)
    length_arf.loc['ISE', name], length_tpr.loc['ISE', name] = IDSE.arf, IDSE.tpr
    
    ss = ts.simplify()
    S = tscompare.compare(ss,ts)
    length_arf.loc['S', name], length_tpr.loc['S', name] = S.arf, S.tpr
    
    sse = ss.extend_haplotypes()
    SE = tscompare.compare(sse, ts)
    length_arf.loc['SE',name],  length_tpr.loc['SE', name] = SE.arf, SE.tpr
    
length_arf.to_csv('figure6-arf-over-length.csv')
length_tpr.to_csv('figure6-tpr-over-length.csv')