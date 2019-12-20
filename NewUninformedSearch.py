# Nick Weisberg


import time as time
import Frontier as Frontiers
import math as m


#########################################################################################
class SearchNode(object):
    """A data structure to store search information"""

    def __init__(self, state, parent_node, step_cost, exp):
        """A SearchNode stores
             a single Problem state,
             a parent node
             the node's depth
             the node's path cost
        """
        self.state = state
        self.parent = parent_node
        if parent_node is None:
            self.path_cost = 0
            self.depth = 0
        else:
            self.path_cost = m.pow(parent_node.path_cost,exp) + step_cost
            self.depth = parent_node.depth + 1

    def __str__(self):
        """ Create and return a string representation of the object"""
        return '<{}> {} ({})'.format(str(self.depth), str(self.state), str(self.path_cost))

    def display_steps(self):
        def disp(node):
            """ recursive function that displays actions
            """
            if node.parent is not None:
                disp(node.parent)
                print(str(node.state.action))

        print("Solution:")
        disp(self)


#########################################################################################
class SearchTerminationRecord(object):
    """A record to return information about how the search turned out.
       All the details are provided in a record, to avoid needing to print out the details
       at different parts of the code.
    """

    def __init__(self, success=False, result=None, time=0, nodes=0, space=0, cutoff=False):
        self.success = success  # Boolean: True if a solution was found
        self.result = result    # SearchNode: a node containing a goal state, or None if no solution found
        self.time = time        # float: time was spent searching.  Not scientifically accurate, but good enough for fun
        self.nodes = nodes      # integer: number of nodes expanded during the search
        self.space = space      # integer: maximum size of the frontier during search
        self.cutoff = cutoff    # Boolean: For IDS, True if depth limited search reach the depth limit before failing

    def __str__(self):
        """Create a string representation of the Result data
        """
        text = 'Search {} ({} sec, {} nodes, {} queue)'
        if self.success:
            textsuccess = 'successful'
        else:
            textsuccess = 'failed'
        return text.format(textsuccess, str(self.time), str(self.nodes), str(self.space))


#########################################################################################
class Search(object):
    """A class to contain uninformed search algorithms.
    """

    def __init__(self, problem, timelimit=10):
        self._problem = problem
        self._frontier = None
        self._time_limit = timelimit


    def _tree_search(self, initial_state, ad, far, step, exp):
        """Search through the State space starting from an initial State.
        """

        start_time = time.time()
        now = start_time
        self._frontier.add(SearchNode(initial_state, None, step, exp))
        node_counter = 0
        max_space = 0

        # keep searching if there are nodes in the Frontier, and time left before the limit
        while not self._frontier.is_empty() and now - start_time < self._time_limit:
            max_space = max(max_space, len(self._frontier))
            this_node = self._frontier.remove()
            node_counter += 1
            now = time.time()
            #print(this_node.state)
            if self._problem.is_goal(this_node.state):
                return SearchTerminationRecord(success=True, result=this_node,
                                    nodes=node_counter, space=max_space, time=now - start_time)
            else:
                for act in self._problem.actions(this_node.state):
                    #print(act)
                    child = self._problem.result(this_node.state, act, ad, far)
                    #print(child)
                    self._frontier.add(SearchNode(child, this_node, step, exp))

        now = time.time()
        return SearchTerminationRecord(success=False, result=None,
                            nodes=node_counter, space=max_space, time=now - start_time)


    def DepthFirstSearch(self, initial_state):
        """
        Perform depth-first search of the problem
        """
        # configure search: for DFS, we want the Frotnier with the LIFO Stack
        self._frontier = Frontiers.FrontierLIFO()

        # run search
        return self._tree_search(initial_state)

    def BreadthFirstSearch(self, initial_state):
        """
        Perform breadth-first search of the problem,
        starting at a given initial state.

        """
        # configure search: for BFS, we want the Frontier with the FIFO Queue
        self._frontier = Frontiers.FrontierFIFO()

        # run search
        return self._tree_search(initial_state)

    def DepthLimitedSearch(self, initial_state, limit):
        """
        Perform depth-limited search of the problem,
        starting at a given initial state.
        """
        # configure search: We want the FIFO Frontier with the depth limit
        self._frontier = Frontiers.FrontierLIFO_DL(limit)


        result = self._tree_search(initial_state)


        result.cutoff = self._frontier._cutoff
        return result

    def IDS(self, initial_state):
        """Iterative deepening Search successively increases the search depth
           the search depth until a solution is found."""
        limit = 0
        nodes = 0
        time = 0
        space = 0
        while time < self._time_limit:
            answer = self.DepthLimitedSearch(initial_state, limit)
            if answer.success:
                answer.time += time
                answer.nodes += nodes
                answer.space = max(answer.space, space)
                return answer
            elif not self._frontier._cutoff:
                return SearchTerminationRecord(success=False, result=None, nodes=nodes, space=space, time=time)
            else:
                nodes += answer.nodes
                time += answer.time    # this could result in search that is substantial longer than the limit
                limit += 1
                space = max(answer.space, space)

        return SearchTerminationRecord(success=False, result=None, nodes=nodes, space=space, time=time)

