# Nick Weisberg


#########################################################################################
class Frontier(object):
    """
    A base class for Frontiers
    """

    def __init__(self):
        self._nodes = []

    def __len__(self):
        return len(self._nodes)

    def is_empty(self):
        return len(self._nodes) == 0

    def add(self, aNode):
        self._nodes.append(aNode)



#########################################################################################
class FrontierFIFO(Frontier):
    """ This Frontier uses a typical FIFO queue.
        This class inherits the Frontier methods.
    """

    def __init__(self):
        Frontier.__init__(self)

    def remove(self):
        val = self._nodes.pop(0)
        return val



#########################################################################################
class FrontierLIFO(Frontier):
    """ This Frontier uses a typical LIFO stack.
    This class inherits the Frontier methods.
    """

    def __init__(self):
        Frontier.__init__(self)

    def remove(self):
        val = self._nodes.pop()
        return val



#########################################################################################
class FrontierLIFO_DL(FrontierLIFO):
    """ This is a LIFO queue, but nodes that exceed a limit are discarded.
    """

    def __init__(self, dlimit):
        """ initialize the Frontier
            dlimit: an integer representing the depth limit to be used.
            Any Node whose depth is greater than dlimit is not added to the Frontier.
        """
        FrontierLIFO.__init__(self)
        self.__dlimit = dlimit
        self._cutoff = False

    def add(self, aNode):
        if aNode.depth <= self.__dlimit:
            self._nodes.append(aNode)
        elif not self._cutoff:
            self._cutoff = True


