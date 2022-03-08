import networkx as nx
import numpy as np


class Human_Solver:
    def __init__(self, costs, similarities):
        self.costs = costs
        self.graph = nx.Graph()
        self.similarities = similarities
        self.current = 'a'

    def path_planning(self):
        while self.current != 'j':
            self.one_step()

    def one_step(self):
        to_do = nx.shortest_path(G=self.graph,
                                 source=self.current,
                                 target='j',
                                 )[0]
        if self.attempt(to_do):
            self.decrease_cost(to_do)
            self.current = to_do[1]
        else:
            self.increase_cost(to_do)

    def attempt(self, edge) -> bool:
        """

        :param edge:
        :return: whether traversing edge is successful
        """
        pass

    def decrease_cost(self, edge):
        pass

    def increase_cost(self, edge):
        pass


# ..set up
costs = np.ones((N, N))*np.inf

similarities = dict(pairs)

solver = Human_Solver(costs, similarities)
