# Nick Weisberg

import heapq as heapq
from Frontier import Frontier


#########################################################################################
class FrontierPQ(Frontier):

    def __init__(self):
        Frontier.__init__(self)
        self._counter = 0

    def remove(self):
        val = heapq.heappop(self._nodes)
        # return the state only
        return val[2]


#########################################################################################
class FrontierUCS(FrontierPQ):

    def __init__(self):
        FrontierPQ.__init__(self)

    def add(self, aNode):
        self._counter += 1
        heapq.heappush(self._nodes, (aNode.path_cost, self._counter, aNode))


#########################################################################################
class FrontierGBFS(FrontierPQ):

    def __init__(self):
        FrontierPQ.__init__(self)

    def add(self, aNode):
        self._counter += 1
        heapq.heappush(self._nodes, (aNode.state.hval, self._counter, aNode))


#########################################################################################
class FrontierAStar(FrontierPQ):

    def __init__(self):
        FrontierPQ.__init__(self)

    def add(self, aNode):
        self._counter += 1
        heapq.heappush(self._nodes, (aNode.path_cost + aNode.state.hval, self._counter, aNode))


