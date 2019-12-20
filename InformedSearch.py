# Nick Weisberg

import InformedFrontier as Frontiers
import NewUninformedSearch as BlindSearch


#########################################################################################
class InformedSearch(BlindSearch.Search):

    def __init__(self, problem, timelimit=10):
        BlindSearch.Search.__init__(self, problem, timelimit=timelimit)

    def BestFirstSearch(self, initialState, ad, far, step, exp):
        self._frontier = Frontiers.FrontierGBFS()
        return self._tree_search(initialState, ad, far, step, exp)

    def UCSSearch(self, initialState, ad, far, step, exp):
        self._frontier = Frontiers.FrontierUCS()
        return self._tree_search(initialState, ad, far, step, exp)

    def AStarSearch(self, initialState, ad, far, step, exp):
        self._frontier = Frontiers.FrontierAStar()
        return self._tree_search(initialState, ad, far, step, exp)
