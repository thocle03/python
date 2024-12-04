import copy
import random

class Board:
    def __init__(self, position=None, children=None, parents=None):
        if position is None:
            self.position = [[" " for _ in range(3)] for _ in range(3)]  
        else:
            self.position = position

        if children is None:
            self.children = []
        else:
            self.children = children
            for child in self.children:
                child.parents.append(self)

        if parents is None:
            self.parents = []
        else:
            self.parents = parents
            for parent in self.parents:
                parent.children.append(self)

    def is_won(self, player):
        winning_combinations = [
            [[0, 0], [0, 1], [0, 2]],  
            [[1, 0], [1, 1], [1, 2]],  
            [[2, 0], [2, 1], [2, 2]],  
            [[0, 0], [1, 0], [2, 0]],  
            [[0, 1], [1, 1], [2, 1]],  
            [[0, 2], [1, 2], [2, 2]], 
            [[0, 0], [1, 1], [2, 2]],  
            [[0, 2], [1, 1], [2, 0]]   
        ]

        return any(all(self.position[row][col] == player for row, col in combination)
                   for combination in winning_combinations)

    def is_full(self):
        return all(cell != " " for row in self.position for cell in row)

    def get_empty_cells(self):
        return [(row, col) for row in range(3) for col in range(3) if self.position[row][col] == " "]

    def make_move(self, row, col, player):
        new_board = copy.deepcopy(self)
        new_board.position[row][col] = player
        return new_board

    def __str__(self):
        rows = [" | ".join(self.position[row]) for row in range(3)]
        return "\n--+---+---\n".join(rows)

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "X"  
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play_computer_move(self, player):
        empty_cells = self.board.get_empty_cells()
        if not empty_cells:
            return None  

        
        move = random.choice(empty_cells)
        self.board = self.board.make_move(move[0], move[1], player)

    def play_game(self):
        while not self.board.is_full() and not self.board.is_won("X") and not self.board.is_won("O"):
            print(self.board)
            print(f"C'est au tour de {self.current_player}.")
            self.play_computer_move(self.current_player)

            if self.board.is_won(self.current_player):
                print(self.board)
                print(f"{self.current_player} a gagné !")
                return

            self.switch_player()

        print(self.board)
        print("Match nul !")

if __name__ == "__main__":
    game = Game()
    game.play_game()
