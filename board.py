# author: Landon Nguyen
# date: February 3, 2023
# file: board.py a Python file that defines a tic tac toe board object
# input: object and method calls from the main file (tictac.py)
# output: a tic-tac-toe board

class Board:
      def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ""
      
      def get_size(self):
             # optional, return the board size (an instance size)
            return self.size
      
      def get_winner(self):
            # return the winner's sign O or X (an instance winner)     
            return self.winner
      
      def set(self, cell, sign):
            # mark the cell on the board with the sign X or O
            valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
            index = valid_choices.index(cell)
            self.board[index] = sign
            
      def isempty(self, cell):
            # return True if the cell is empty (not marked with X or O)
            valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
            index = valid_choices.index(cell)

            if self.board[index] == " ":
                  return True
            else:
                  return False
      
      def isdone(self):
            done = False
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X
            # vertical O
            if self.board[0] == 'O' and self.board[1] == 'O' and self.board[2] == 'O':
                  done = True
                  self.winner = 'O'
            elif self.board[3] == 'O' and self.board[4] == 'O' and self.board[5] == 'O':
                  done = True
                  self.winner = 'O'
            elif self.board[6] == 'O' and self.board[7] == 'O' and self.board[8] == 'O':
                  done = True
                  self.winner = 'O'
            
            # horizontal O
            elif self.board[0] == 'O' and self.board[3] == 'O' and self.board[6] == 'O':
                  done = True
                  self.winner = 'O'
            elif self.board[1] == 'O' and self.board[4] == 'O' and self.board[7] == 'O':
                  done = True
                  self.winner = 'O'
            elif self.board[2] == 'O' and self.board[5] == 'O' and self.board[8] == 'O':
                  done = True
                  self.winner = 'O'

            # diagnonal O
            elif self.board[0] == 'O' and self.board[4] == 'O' and self.board[8] == 'O':
                  done = True
                  self.winner = 'O'
            elif self.board[2] == 'O' and self.board[4] == 'O' and self.board[6] == 'O':
                  done = True
                  self.winner = 'O'


            # vertical X
            elif self.board[0] == 'X' and self.board[1] == 'X' and self.board[2] == 'X':
                  done = True
                  self.winner = 'X'
            elif self.board[3] == 'X' and self.board[4] == 'X' and self.board[5] == 'X':
                  done = True
                  self.winner = 'X'
            elif self.board[6] == 'X' and self.board[7] == 'X' and self.board[8] == 'X':
                  done = True
                  self.winner = 'X'
            
            # horizontal X
            elif self.board[0] == 'X' and self.board[3] == 'X' and self.board[6] == 'X':
                  done = True
                  self.winner = 'X'
            elif self.board[1] == 'X' and self.board[4] == 'X' and self.board[7] == 'X':
                  done = True
                  self.winner = 'X'
            elif self.board[2] == 'X' and self.board[5] == 'X' and self.board[8] == 'X':
                  done = True
                  self.winner = 'X'

            # diagnonal X
            elif self.board[0] == 'X' and self.board[4] == 'X' and self.board[8] == 'X':
                  done = True
                  self.winner = 'X'
            elif self.board[2] == 'X' and self.board[4] == 'X' and self.board[6] == 'X':
                  done = True
                  self.winner = 'X'
            
            # tie
            else:
                  if self.board[0] != " " and self.board[1] != " " and self.board[2] != " " and self.board[3] != " " and self.board[4] != " " and self.board[5] != " " and self.board[6] != " " and self.board[7] != " " and self.board[8] != " ":
                        done = True
                        self.winner = ''

            return done
      
      def show(self):
            # draw the board
            # need to complete the code
            print()
            print('   A   B   C') 
            print(' +---+---+---+')
            print('1| {} | {} | {} |'.format(self.board[0], self.board[3], self.board[6]))
            print(' +---+---+---+')
            print('2| {} | {} | {} |'.format(self.board[1], self.board[4], self.board[7]))
            print(' +---+---+---+')
            print('3| {} | {} | {} |'.format(self.board[2], self.board[5], self.board[8]))
            print(' +---+---+---+')
               
