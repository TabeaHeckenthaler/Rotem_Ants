Input
Configuration space 
split into 10 different areas (graph nodes).
Nodes are connected by edges based on adjacency. 
Not all edges are traversable.
We find similarities between edges.

Similarities
bg(x) = gh(v)
ad(v) = fi(x) = ei(x)
df(v) = ij(v) = de(x)
fg(v) = cb(v)
ac(v) = jh(v)

start = c
end = j, h
Edges carry an initial cost (extract these from experimental data)

Algorithm:
While not at goal:
Find lowest-cost path, and attempt to traverse first edge. 
Edge traversal: local algorithm, that succeeds or doesn’t. 
In case of success: Decrease the cost of this edge, and its similar edges. Walk to the respective node. 
In case of failure: Increase the cost of this edge, and its similar edges. Remain in your node. 

NOTES: 
Randomness of initial cost, or randomness per long term decision.
