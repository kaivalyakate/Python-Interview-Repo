class TicTacToe:

    def __init__(self, n: int):
        self.size = n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.rows = [0] * n
        self.cols = [0] * n

    def move(self, row: int, col: int, player: int) -> int:
        current_player = 1 if player == 1 else -1
        self.rows[row] += current_player
        self.cols[col] += current_player

        if (row == col):
            self.diagonal += current_player
        
        if (col == (self.size - col - 1)):
            self.anti_diagonal += current_player
        
        if abs(self.rows[row]) == self.size \
           or abs(self.cols[col]) == self.size or abs(self.diagonal) == self.size or abs(self.anti_diagonal) == self.size:  
            return player 
        return 0
    

if __name__ == "__main__":
    tt = TicTacToe(3)
    tt.move(0, 0, 1)
    tt.move(0, 2, 2)
    tt.move(2, 2, 1)
    tt.move(1, 1, 2)
    tt.move(2, 0, 1)
    tt.move(1, 0, 2)
    print(tt.move(2, 1, 1))