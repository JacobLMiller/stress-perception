import graph_tool.all as gt 
import numpy as np
from sklearn.manifold import MDS

def apsp(G,weights=None):
    d = np.array( [v for v in gt.shortest_distance(G,weights=weights)] ,dtype=float)
    if weights:
        d /= np.sum(d,axis=0)
    return d

for size in [10,25,50]:
    for stress in range(40,85,5):
        for gnum in range(1,6):
            for draw in 'abc':
                G,_ = gt.geometric_graph(np.random.uniform(0,1,size=(size,2)), 0.4)
                d = apsp(G)

                X = MDS(dissimilarity='precomputed').fit_transform(d)

                pos = G.new_vp("vector<float>")
                pos.set_2d_array(X.T)
                gt.graph_draw(G,pos, output=f"drawings/n{size}_g{gnum}_l{stress}_{draw}.png")    