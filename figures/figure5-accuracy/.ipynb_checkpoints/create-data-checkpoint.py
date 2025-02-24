import tskit, msprime
import numpy as np
import pandas as pd
from remove_isolated_unary import remove_isolated_unary

def node_spans(ts):
    """
    Returns the array of "node spans", i.e., the `j`th entry gives
    the total span over which node `j` is in the tree sequence
    (i.e., does not have 'missing data' there).

    """
    child_spans = np.bincount(
        ts.edges_child,
        weights=ts.edges_right - ts.edges_left,
        minlength=ts.num_nodes,
    )
    for t in ts.trees():
        span = t.span
        for r in t.roots:
            # do this check to exempt 'missing data'
            if t.num_children(r) > 0:
                child_spans[r] += span
    return child_spans

def get_span_stats(ts, ets):
    time_map = {}
    added_span = np.zeros(ets.num_nodes)
    wrong_added_span = np.zeros(ets.num_nodes)
    for n in ts.nodes():
        # check times are unique except for samples
        assert n.time == 0.0 or n.time not in time_map
        time_map[n.time] = n.id

    for interval, t, et in ts.coiterate(ets):
        interval_length = interval[1] - interval[0]
        t_nodes = list(t.nodes())
        for n in et.nodes():
            if et.num_children(n) == 1:
                added_span[n] += interval_length
                # total_added_span += interval_length
            on = time_map[et.time(n)]
            if on not in t_nodes:
                assert et.num_children(n) == 1
                wrong_added_span[n] += interval_length
    return added_span, wrong_added_span

node_span_data = pd.DataFrame(columns=['T-node-span','S-node-span','SE-node-span', 'SE-added-span','SE-added-wrong'])

ts = msprime.sim_ancestry(1e5, sequence_length=1e8, recombination_rate=1e-8, population_size=1e5, coalescing_segments_only=False, random_seed=1)
# Remove the isolated unary spans from our tree sequence
t = remove_isolated_unary(ts)
s = t.simplify()
e = s.extend_haplotypes()

# Find node spans (for subplots C,D)
node_span_data['T-node-span'] = node_spans(t)
node_span_data['S-node-span'] = node_spans(s)
node_span_data['SE-node-span'] = node_spans(e)
node_span_data['SE-added-span'], node_span_data['SE-added-wrong'] = get_span_stats(ts, ets)

node_span_data.to_csv('nodespans.csv')