class kakurasu:
  UNSET = 0
  DOT = 1
  NOTHING = 2

  def __init__(self, state, row_const, col_const, size):
        self.state = state
        self.row_const = row_const
        self.col_const = col_const
        self.size = size
        self.trees = self.generate_list_tree()
        
  def accept(self, solver):
      return solver.solve(self)
  
#   def generate_list_tree(self):
#       self.trees = []

#       for row_idx in range(self.size):
#           for col_idx in range(self.size):
#               number = self.state[row_idx][col_idx]
#               if number == Tents.TREE:
#                   self.trees += [[row_idx, col_idx]]
        
#         return self.trees

  def can_have_dot_at(self, state, row_idx, col_idx):
      if row_idx < 0 or row_idx >= self.size or col_idx < 0 or col_idx >= self.size:
          return False
      
      count_row_dots_val = 0
      count_col_dots_val = 0
      for i in range(self.size):
          if state[row_idx][i] == kakurasu.DOT:
              count_row_dots_val += i
          if state[i][col_idx] == kakurasu.DOT:
              count_col_dots_val += i
      
      if count_col_dots_val > self.col_const[col_idx] or count_row_tents > self.row_const[row_idx]:
            return False
      #we have to check the trueness of the dots
    
    
    
  def is_legal_state(self, state):
    for row_idx in range(self.size):
        for col_idx in range(self.size):
            if state[row_idx][col_idx] == kakurasu.DOT:
                if self.can_have_dot_at(state, row_idx, col_idx) == False:
                    return False               
    return True

  #some method here

      
        
