import networkx as nx
import numpy as np


class Human_Solver:
    def __init__(self, real_connections, perceived_connections, costs, similarities):
        self.costs = costs
        self.graph = nx.Graph(real_connections)
        self.perception_graph = nx.Graph(perceived_connections)
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
        # TODO: check whether in self.graph these are really two connected nodes, maybe we should add a source of
        #  randomness as well
        pass

    def decrease_cost(self, edge):
        # TODO: how to decrease the cost
        pass

    def increase_cost(self, edge):
        # TODO: how to increase the cost
        pass


if __name__ == '__main__':
    # TODO: Data structure, that can be given to nx.Graph()
    real_connections = None
    perceived_connections = None

    # TODO: Define initial costs.
    costs = np.ones((N, N))*np.inf

    # TODO: define dictionary with similar pairs (like in README.txt)
    similarities = dict(pairs)

    solver = Human_Solver(real_connections, perceived_connections, costs, similarities)
    solver.path_planning()
