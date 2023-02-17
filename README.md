# tictactoe

Description: tictac.py simulates the classic game of tic-tac-toe by importing board.py and player.py, and generates a traditional 3x3 board in the terminal

Functionality:
- The program outputs interactive messages and a board interface
- Users can select where they want to place their sign by inputting [A-C][1-3] into the terminal, (e.g. A1 will select the top left cell and C3 will select the bottom right cell)
- A user can either play against another user which is identified by a Player() object or an AI which identified by the AI() object
- There are three different types of AI to play against that can be differentiated by their algorithms
- The AI() object is the easiest AI to play against as it's programmed to randomly select cells
- The SmartAI() object has a "medium" difficulty as it uses heuristic approaches to find the best cell combined with the randomness of the AI() object
- The MiniMax() object is the hardest AI to play against as it is impossible to win against. This is because the object uses the recursive MiniMax algorithm to calculate every single possible move, then returns the absolute best cell that will either tie or win the game
