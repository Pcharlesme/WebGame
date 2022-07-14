from tiktactoe import Player
from tiktactoe import HumanPlayer
from tiktactoe import RandomComputerPlayer
class TicTacToe:
    
    def __init__(self):
        self.board = [ '' (for_in range(9))]
        self.board = [' |' for_in range(9)]
        self.current_winner=None
        
    def print_board(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
          print('|' + '|'.join(row)+ '|') 
    
    @staticmethod
    def print_board_nums():
     
        
      