class Game():
    board = {
        'a1': None, 'b1': None, 'c1': None,
        'a2': None, 'b2': None, 'c2': None,
        'a3': None, 'b3': None, 'c3': None,
    }
    
    def __init__(self, turn='X', tie=False, winner=None, board=board):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = board
    
    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)
        
    def check_winner(self):
        b = self.board
        if b['a1'] and b['a1'] == b['b1'] == b['c1']:
            self.winner = b['a1']
        elif b['a2'] and b['a2'] == b['b2'] == b['c2']:
            self.winner = b['a2']
        elif b['a3'] and b['a3'] == b['b3'] == b['c3']:
            self.winner = b['a3']
        elif b['a1'] and b['a1'] == b['a2'] == b['a3']:
            self.winner = b['a1']
        elif b['b1'] and b['b1'] == b['b2'] == b['b3']:
            self.winner = b['b1']
        elif b['c1'] and b['c1'] == b['c2'] == b['c3']:
            self.winner = b['c1']
        elif b['a1'] and b['a1'] == b['b2'] == b['c3']:
            self.winner = b['a1']
        elif b['a3'] and b['a3'] == b['b2'] == b['c1']:
            self.winner = b['a3']
        
        if all(self.board.values()):
            self.tie = True
    
    def print_message(self):
        if self.winner:
            self.print_board()
            print(f"\n\n\n!!!Player {self.winner} wins!!!")
        elif self.tie:
            self.print_board()
            print("\n\n\n!!!It's a tie!!!")

    def play_game(self):
        print("Shall we play a game?")
        
        while not self.winner and not self.tie:
            print("Enter 'q' to quit the game")
            self.print_board()
            print(f"Player {self.turn} Turn")
            position = input(f"Enter a valid movie (example: a1):  ").lower()
            if position == 'q':
                print("!!!Quitted the game!!!")
                break
            elif position not in self.board:
                print("\n\n\n!!!Invalid position!!!")
                continue
            elif self.board[position]:
                print("\n\n\n!!!Position already taken!!!")
                continue
            self.board[position] = self.turn
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
            self.check_winner()
            self.print_message()
            


game_instance = Game()
game_instance.play_game()