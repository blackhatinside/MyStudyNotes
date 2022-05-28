
def is_valid_state(state):
    # check if it is a valid solution
    return True

def get_candidates(state):
    return []

def search(state, solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
        # return

    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)

def solve():
    solutions = []
    state = set()
    search(state, solutions)
    return solutions

'''---------- https://leetcode.com/problems/n-queens/ ----------'''

class Solution:
    '''
        example on the left : [1, 3, 0, 2]
        example on the right : [2, 0, 3, 1]
        problem type : backtracking + recursion
    '''
    
    # def solve():
    #     solutions = []
    #     state = set()
    #     search(state, solutions)
    #     return 
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        # initialize state & solutions to empty list i.e. no queen is placed
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions
        
    def is_valid_state(self, state, n):
        # check if it is a valid solution
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:   # if no queen is placed on the board
            return range(n)
        # find the next position in the state to populate
        position = len(state)
        candidates = set(range(n))
        # prune down candidates that place the queen into attacks
        for row, col in enumerate(state):
            # discard the column index if it's occupied by a queen
            candidates.discard(col)
            dist = position - row
            # discard diagonals
            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return candidates
        
    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            state_string = self.state_to_string(state, n)
            solutions.append(state_string)
            return
            # return

        for candidate in self.get_candidates(state, n):
            # recurse
            state.append(candidate)
            self.search(state, solutions, n)
            # restore modified state back to original
            state.pop()
        
    def state_to_string(self, state, n):
        # helper function to format the output as per the question
        # ex. [1, 3, 0, 2]
        # output = [".Q..","...Q","Q...","..Q."]
        ret = []
        for i in state:
            string = "." * i + 'Q' + "." * (n - i - 1)
            ret.append(string)
        return ret
