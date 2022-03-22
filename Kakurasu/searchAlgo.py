from kakurasu import *
import math

class SearchAlgorithm:
    def solve(self, kakurasu):
        pass
    def let_me_sove(self, kakurasu):
        return kakurasu.accept(self)

class TrackNode:
    def dots_at(self, row_idx, col_idx):
        self.state[row_idx][col_idx] = kakurasu.DOT

    def nothing_at(self, row_idx, col_idx):
        self.state[row_idx][col_idx] = kakurasu.NOTHING

    def expandnode(self):
        size = len(self.state) if self.state else 0
        for row_idx in range(size):
            for col_idx in range(size):
                if selfstate[row_idx][col_idx] == kakurasu.UNSET:
                    res = []
                    first_child = type(self)(self.state) #not enough
                    first_child.dots_at(row_idx, col_idx)
                    res += [first_child]

                    second_child = type(self)(self.state) #not enough
                    second_child.nothing_at(row_idx, col_idx)
                    
                    res += [second_child]

                    return res
        return []

class AStarSearch(SearchAlgorithm):
    class Node(TrackNode):
        def __init__(self,state):
            self.state = Util.deep_copy(state)
            self.size = len(self.state)
            self.g_value = self.cal_g_value() #total value of used dots
            self.h_value = self.cal_h_value() #a rest value that we think later???
            self.total_cost = self.g_value + self.h_value

        
        def get_total_cost(self):
            return self.g_value + self.h_value

        def cal_g_value(self):
            countTotal = 0
            count = 0

            for row in self.state:
                for number in row:
                    count += 1
                    if number == kakurasu.DOT:
                        countTotal += count

            return countTotal

        #HAVE TO DO WITH H VALUE
        def cal_h_value(self):
            return 0

        def compare(self, node_a, node_b):
            return node_a.total_cost <= node_b.total_cost

        def solve(self, dots):
            #NEED TO IMPLEMENT
            return 0

    class BreadthFirstSearch(SearchAlgorithm):
        class Node(TrackNode):
            def __init__(self, state):
                self.state = Util.deep_copy(state)

    #ONG LAM THU PHAN BFS NHA?