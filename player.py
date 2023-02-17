# author: Landon Nguyen
# date: February 3, 2023
# file: player.py a Python file that defines a player and the in-game AI
# input: strings, a board object, and object and method calls from the main file (tictac.py)
# output: interactive text messages
import random

class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      
      def get_sign(self):
            # return an instance sign
            return self.sign
      
      def get_name(self):
            # return an instance name
            return self.name
      
      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
            while True: 
                  cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:').upper()
                  if cell in valid_choices:
                        if board.isempty(cell):
                              board.set(cell, self.sign)
                              break
                        else:
                              print('\nYou did not choose correctly.')
                  else:
                        print('\nYou did not choose correctly.')
                        
                  
class AI(Player):
      def __init__(self, name, sign, board):
            self.board = board
            super().__init__(name, sign)

      def choose(self, board):
            valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
            while True:
                  cell = random.choice(valid_choices)
                  if board.isempty(cell):
                        print(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')
                        print(cell)
                        board.set(cell, self.sign)
                        break

class SmartAI(AI):
      def __init__(self, name, sign, board):
            super().__init__(name, sign, board)

      def choose(self, board):
            turn = 0
            valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
            for i in valid_choices:
                  if board.isempty(i) == False:
                        turn += 1
            print(turn)
            if turn == 1 or 0:
                  choices = [0,1,2,3,5,6,7,8]
                  index = random.choice(choices)
                  cell = valid_choices[index]
                  if board.isempty(cell):
                        print(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')
                        print(cell)
                        board.set(cell, self.sign)
            
            elif turn == 3 or 2:
                  index = self.threatCheck(board)
                  cell = valid_choices[index]
                  if index != -1:
                        print(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')
                        print(cell)
                        board.set(cell, self.sign)
                  else:
                        while True:
                              index = random.randint(0,8)
                              cell = valid_choices[index]
                              if board.isempty(cell):
                                    print(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')
                                    print(cell)
                                    board.set(cell, self.sign)
                                    break

            elif turn == 5 or 4:
                  index = self.evaluate(board)
                  if index != -1:
                        cell = valid_choices[index]
                        print(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')
                        print(cell)
                        board.set(cell, self.sign)
                  else:
                        index = self.threatCheck(board)
                        if index != -1:
                              cell = valid_choices[index]
                              print(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')
                              print(cell)
                              board.set(cell, self.sign)
                        else:
                              while True:
                                    index = random.randint(0,8)
                                    cell = valid_choices[index]
                                    if board.isempty(cell):
                                          print(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')
                                          print(cell)
                                          board.set(cell, self.sign)
                                          break

            elif turn == 7 or 6:
                  index = self.evaluate(board)
                  if index != -1:
                        cell = valid_choices[index]
                        print(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')
                        print(cell)
                        board.set(cell, self.sign)
                  else:
                        index = self.threatCheck(board)
                        print(index)
                        if index != -1:
                              cell = valid_choices[index]
                              print(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')
                              print(cell)
                              board.set(cell, self.sign)
                        else:
                              while True:
                                    index = random.randint(0,8)
                                    cell = valid_choices[index]
                                    if board.isempty(cell):
                                          print(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')
                                          print(cell)
                                          board.set(cell, self.sign)
                                          break


      def threatCheck(self, board):
            valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

            if board.board[1] == 'X' and board.board[2] == 'X':
                  cell = valid_choices[0]
                  if board.isempty(cell):
                        return 0
            if board.board[3] == 'X' and board.board[6] == 'X':
                  cell = valid_choices[0]
                  if board.isempty(cell):
                        return 0
            if board.board[4] == 'X' and board.board[8] == 'X':
                  cell = valid_choices[0]
                  if board.isempty(cell):
                        return 0
            
            if board.board[0] == 'X' and board.board[1] == 'X':
                  cell = valid_choices[2]
                  if board.isempty(cell):
                        return 2
            if board.board[5] == 'X' and board.board[8] == 'X':
                  cell = valid_choices[2]
                  if board.isempty(cell):
                        return 2
            if board.board[4] == 'X' and board.board[6] == 'X':
                  cell = valid_choices[2]
                  if board.isempty(cell):
                        return 2
            
            if board.board[0] == 'X' and board.board[3] == 'X':
                  cell = valid_choices[6]
                  if board.isempty(cell):
                        return 6
            if board.board[2] == 'X' and board.board[4] == 'X':
                  cell = valid_choices[6]
                  if board.isempty(cell):
                        return 6
            if board.board[7] == 'X' and board.board[8] == 'X':
                  cell = valid_choices[6]
                  if board.isempty(cell):
                        return 6
            
            if board.board[0] == 'X' and board.board[4] == 'X':
                  cell = valid_choices[8]
                  if board.isempty(cell):
                        return 8
            if board.board[6] == 'X' and board.board[7] == 'X':
                  cell = valid_choices[8]
                  if board.isempty(cell):
                        return 8
            if board.board[2] == 'X' and board.board[5] == 'X':
                  cell = valid_choices[8]
                  if board.isempty(cell):
                        return 8

            if board.board[0] == 'X' and board.board[2] == 'X':
                  cell = valid_choices[1]
                  if board.isempty(cell):
                        return 1
            if board.board[4] == 'X' and board.board[7] == 'X':
                  cell = valid_choices[1]
                  if board.isempty(cell):
                        return 1
            
            if board.board[0] == 'X' and board.board[6] == 'X':
                  cell = valid_choices[3]
                  if board.isempty(cell):
                        return 3
            if board.board[4] == 'X' and board.board[5] == 'X':
                  cell = valid_choices[3]
                  if board.isempty(cell):
                        return 3
            
            if board.board[2] == 'X' and board.board[8] == 'X':
                  cell = valid_choices[5]
                  if board.isempty(cell):
                        return 5
            if board.board[3] == 'X' and board.board[4] == 'X':
                  cell = valid_choices[5]
                  if board.isempty(cell):
                        return 5

            if board.board[1] == 'X' and board.board[4] == 'X':
                  cell = valid_choices[7]
                  if board.isempty(cell):
                        return 7
            if board.board[6] == 'X' and board.board[8] == 'X':
                  cell = valid_choices[7]
                  if board.isempty(cell):
                        return 7

            if board.board[0] == 'X' and board.board[8] == 'X':
                  cell = valid_choices[4]
                  if board.isempty(cell):
                        return 4
            if board.board[2] == 'X' and board.board[6] == 'X':
                  cell = valid_choices[4]
                  if board.isempty(cell):
                        return 4
            if board.board[1] == 'X' and board.board[7] == 'X':
                  cell = valid_choices[4]
                  if board.isempty(cell):
                        return 4
            if board.board[3] == 'X' and board.board[5] == 'X':
                  cell = valid_choices[4]
                  if board.isempty(cell):
                        return 4
                  
            return -1


      def evaluate(self, board):
            valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

            if board.board[1] == 'O' and board.board[2] == 'O':
                  cell = valid_choices[0]
                  if board.isempty(cell):
                        return 0
            if board.board[3] == 'O' and board.board[6] == 'O':
                  cell = valid_choices[0]
                  if board.isempty(cell):
                        return 0
            if board.board[4] == 'O' and board.board[8] == 'O':
                  cell = valid_choices[0]
                  if board.isempty(cell):
                        return 0
            
            if board.board[0] == 'O' and board.board[1] == 'O':
                  cell = valid_choices[2]
                  if board.isempty(cell):
                        return 2
            if board.board[5] == 'O' and board.board[8] == 'O':
                  cell = valid_choices[2]
                  if board.isempty(cell):
                        return 2
            if board.board[4] == 'O' and board.board[6] == 'O':
                  cell = valid_choices[2]
                  if board.isempty(cell):
                        return 2
            
            if board.board[0] == 'O' and board.board[3] == 'O':
                  cell = valid_choices[6]
                  if board.isempty(cell):
                        return 6
            if board.board[2] == 'O' and board.board[4] == 'O':
                  cell = valid_choices[6]
                  if board.isempty(cell):
                        return 6
            if board.board[7] == 'O' and board.board[8] == 'O':
                  cell = valid_choices[6]
                  if board.isempty(cell):
                        return 6
            
            if board.board[0] == 'O' and board.board[4] == 'O':
                  cell = valid_choices[8]
                  if board.isempty(cell):
                        return 8
            if board.board[6] == 'O' and board.board[7] == 'O':
                  cell = valid_choices[8]
                  if board.isempty(cell):
                        return 8
            if board.board[2] == 'O' and board.board[5] == 'O':
                  cell = valid_choices[8]
                  if board.isempty(cell):
                        return 8

            if board.board[0] == 'O' and board.board[2] == 'O':
                  cell = valid_choices[1]
                  if board.isempty(cell):
                        return 1
            if board.board[4] == 'O' and board.board[7] == 'O':
                  cell = valid_choices[1]
                  if board.isempty(cell):
                        return 1
            
            if board.board[0] == 'O' and board.board[6] == 'O':
                  cell = valid_choices[3]
                  if board.isempty(cell):
                        return 3
            if board.board[4] == 'O' and board.board[5] == 'O':
                  cell = valid_choices[3]
                  if board.isempty(cell):
                        return 3
            
            if board.board[2] == 'O' and board.board[8] == 'O':
                  cell = valid_choices[5]
                  if board.isempty(cell):
                        return 5
            if board.board[3] == 'O' and board.board[4] == 'O':
                  cell = valid_choices[5]
                  if board.isempty(cell):
                        return 5

            if board.board[1] == 'O' and board.board[4] == 'O':
                  cell = valid_choices[7]
                  if board.isempty(cell):
                        return 7
            if board.board[6] == 'O' and board.board[8] == 'O':
                  cell = valid_choices[7]
                  if board.isempty(cell):
                        return 7

            if board.board[0] == 'O' and board.board[8] == 'O':
                  cell = valid_choices[4]
                  if board.isempty(cell):
                        return 4
            if board.board[2] == 'O' and board.board[6] == 'O':
                  cell = valid_choices[4]
                  if board.isempty(cell):
                        return 4
            if board.board[1] == 'O' and board.board[7] == 'O':
                  cell = valid_choices[4]
                  if board.isempty(cell):
                        return 4
            if board.board[3] == 'O' and board.board[5] == 'O':
                  cell = valid_choices[4]
                  if board.isempty(cell):
                        return 4
                  
            return -1



class MiniMax(AI):
      def __init__(self, name, sign, board):
            super().__init__(name, sign, board)
            self.valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
            self.opponent_sign = ''
            if self.sign == 'X':
                  self.opponent_sign = 'O'
            else:
                  self.opponent_sign = 'X'
      
      def choose(self, board):
            print(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')
            cell = MiniMax.minimax(self, board, True, True)
            print(cell)
            board.set(cell, self.sign)

      def minimax(self, board, self_player, start):
            # check the base conditions
            if board.isdone():
                  if board.get_winner() == self.sign:
                        return 1
                  elif board.get_winner() == "":
                        return 0
                  else:
                        return -1
            else:
                  # make a move (choose a cell) recursively
                  maxscore = -10
                  minscore = 10
                  move = ''
                  for cell in self.valid_choices:
                        if board.isempty(cell):
                        # call minimax recursively
                              if self_player:
                                    board.set(cell, self.sign)
                                    score = MiniMax.minimax(self, board, False, False)
                                    if score > maxscore:
                                          maxscore = score
                                          move = cell
                                    board.set(cell, " ")
                              else:
                                    board.set(cell, self.opponent_sign)
                                    score = MiniMax.minimax(self, board, True, False)
                                    if score < minscore:
                                          minscore = score
                                          move = cell
                                    board.set(cell, " ")
                  if start:
                        return move
                  elif self_player:
                        return maxscore
                  else:
                        return minscore

      