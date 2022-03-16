from itertools import combinations
import time  # to wait a while in the solver
from copy import deepcopy
import networkx as nx
import numpy as np


class HumanSolver:
    def __init__(self, graph, actual_edges, similar_edges, rand_gen):
        self._graph = deepcopy(graph)  # the perceived connection+cost graph (cost = 'weight')
        self._actual_edges = actual_edges  # actual edges for attempts
        self._similar_edges = similar_edges
        self._current_state = 'c'  # not 'a'
        self._gen = rand_gen
        self._attempts = []

    def solve_maze(self):
        statelis = [self._current_state]
        while self._current_state != 'j':
            # print(f"\nI'm at {self._current_state}")
            self.one_step()
            statelis.append(self._current_state)
            # time.sleep(3)
        # print("\nDone! States visited:", "->".join(statelis))
        print(",".join(self._attempts))

    def one_step(self):
        if self._current_state == 'j': raise Exception("Already at Target!")

        to_do = nx.shortest_path(G=self._graph,
                                 source=self._current_state,
                                 target='j',
                                 weight='weight'
                                 # method?
                                 )[:2]  # returns list of nodes - not edges
        if self.attempt(to_do):
            self.decrease_cost(to_do)
            self._current_state = to_do[1]
        else:
            self.increase_cost(to_do)

    def attempt(self, edge) -> bool:
        """
        :param edge:
        :return: whether traversing edge is successful
        """
        self._attempts.append("-".join(edge))
        # TODO: add randomness?
        r = sorted(edge) in self._actual_edges
        # print("attempted to move from {} to {}.".format(*edge), "Succeeded!" if r else "Failed!")
        return r

    def decrease_cost(self, edge):
        # TODO: how to decrease the cost
        edge = "".join(sorted(edge))

        self._graph[edge[0]][edge[1]]['weight'] /= 2**self._gen.normal(1, 2)
        # print("Decreased weight of edge {} to {}".format(edge, self._graph[edge[0]][edge[1]]['weight']))
        for sim in self._similar_edges.get(edge, []):
            self._graph[sim[0]][sim[1]]['weight'] /= 1.5**self._gen.normal(1, 2)
            # print("Decreased weight of edge {} to {}".format(sim, self._graph[sim[0]][sim[1]]['weight']))

    def increase_cost(self, edge):
        # TODO: how to increase the cost
        # TODO: also increase/decrease similarity measure if it was correct/false?
        edge = "".join(sorted(edge))

        self._graph[edge[0]][edge[1]]['weight'] *= 2**self._gen.normal(1, 2)
        # print("Increased weight of edge {} to {}".format(edge, self._graph[edge[0]][edge[1]]['weight']))
        for sim in self._similar_edges.get(edge, []):
            self._graph[sim[0]][sim[1]]['weight'] *= 1.5**self._gen.normal(1, 2)
            # print("Increased weight of edge {} to {}".format(sim, self._graph[sim[0]][sim[1]]['weight']))


# refactor to have the graph construction in a function

if __name__ == '__main__':
    site_lis = list('abcdefghijk')
    site_to_num = dict((j, i) for i, j in enumerate(site_lis))

    # TODO: Define initial costs.
    N = len(site_lis)
    edge_lis = [sorted(e) for e in 'ac, ad, cb, de, df, eg, fg, gh, hj, ji'.split(", ")]  # sorted for comparisons
    perceived_edge_lis = edge_lis + [sorted(e) for e in 'fi, ei, bg'.split(", ")]  # add di? It's more extreme though

    # temporary costs
    # thick connection - .5
    # thin connection - 1.5
    # h and j are "the same" in sense of solving the maze - so their cost is 0
    edge_costs = (.5, 1.5, .5, 1.5, 1.5, 1.5, 1.5, 1.5, 0, .5,
                  1.5, 1.5, 1.5)  # "fake" edges are about as hard as the hardest "real" edges

    perceived_graph = nx.Graph()
    for edge, cost in zip(perceived_edge_lis, edge_costs):
        perceived_graph.add_edge(edge[0], edge[1], weight=cost)

    """
    print(perceived_graph.edges(data=True))
    res = nx.shortest_path(G=perceived_graph, source='a', target='j', weight='weight')
    print(f"{res=}")
    #"""

    # Also add mirror similarities? i.e cb-gh
    similarities = "bg-gh, ad-fi-ei, df-ij-de, fg-cb, ac-jh".split(", ")
    # df/de - ij?? Seems weird..
    similar_edges = dict()
    for similarity_set in similarities:
        for a, b in combinations(similarity_set.split("-"), 2):
            similar_edges[a] = similar_edges.get(a, []) + [b]
            similar_edges[b] = similar_edges.get(b, []) + [a]

    # print(nx.shortest_path(perceived_graph, source='c', target='j', weight='weight'))
    # print(nx.shortest_path(perceived_graph, source='a', target='j', weight='weight'))

    rand_gen = np.random.default_rng(43)
    for _ in range(500):
        solver = HumanSolver(perceived_graph, edge_lis, similar_edges, rand_gen)
        solver.solve_maze()
