class Chess:
    def __init__(self, player):
        # para definir el jugador, su tablero y sus movimientos (guardados en una lista)
        self.player = player # para definir el jugador, su tablero y sus movimientos 
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.init_board()
        self.moves = [] 
        self.save_game()

    def init_board(self):
        # configura el tablero inicial con letras para las piezas
        self.board[0] = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
        self.board[1] = ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟']
        for i in range(2, 6):
            self.board[i] = [' 'for _ in range(8)]
        self.board[6] = ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙']
        self.board[7] = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']

    def save_game(self): # para guardar el estado inicial del tablero en el fichero de la partida (llamado ..._ajedrez.txt)
        with open(f"{self.player}_ajedrez.txt", "w") as file:
            for row in self.board:
                file.write('\t'.join(row) + '\n')
            file.write("\n")

    def show_board(self): #para hacer el tablero mas visual y poder usarlo para hacer los movimientos
        column_letters = 'abcdefgh'
        print('    ' + '   '.join(column_letters))
        for i, row in enumerate(self.board[::-1], 1):
            print(f"{9 - i}   {'   '.join(row)}")

    def move_piece(self, start, end, move_number): # para mover las piezas
        start = (ord(start[0]) - ord('a'), int(start[1]) - 1) if len(start) == 2 else (ord(start[0]) - ord('a'), int(start[1:]) - 1)
        end = (ord(end[0]) - ord('a'), int(end[1]) - 1)
        if start == end: #quita las situaciones de errores 
            print("\nError: The initial position is the same as the last one.")
            return
        if self.board[start[1]][start[0]] == ' ':
            print("\nError: There is no piece to move at the initial position.")
            return
        if self.board[end[1]][end[0]] != ' ':
            print("\nError: There is already a piece at the entered final position.")
            return
        self.board[end[1]][end[0]] = self.board[start[1]][start[0]] # para mover la pieza en su sitio 
        self.board[start[1]][start[0]] = ' '
        self.save_move(start, end, move_number)

    def save_move(self, start, end, move_number): # para guardar el movimiento hecho en el fichero y el tablero modificado con su numero asignado
        with open(f"{self.player}_chess.txt", "a") as file:
            file.write("\nBoard after move {}:\n".format(move_number))
            for row in self.board:
                file.write('\t'.join(row) + '\n')
            file.write(f"{self.convert_notation(start)} -> {self.convert_notation(end)}\n")
        self.moves.append((start, end))

    def consult_move(self, move_number): #para proponer a los jugadores al finalde la partida de revisitar algun movimiento
        if move_number < 0 or move_number > len(self.moves):
            print("\nError: Invalid move number.")
            return None
        self.init_board() # para asegurarse que el tablero esta en su estado inicial
        
        for i in range(move_number+1): # realiza los movimientos hasta el numero asignado
            start, end = self.moves[i]
            self.move_piece(start, end)
        return self.board # devuelve el tablero despues del movimiento

    def convert_notation(self, position): # para que los movimientos guardados sean con la misma anotacion que lo que esta alrededor del tabler (ej b2 -> b4)
        column = chr(position[0] + ord('a'))
        row = str(position[1] + 1)
        return f"{column}{row}"

def play_chess(player): #funcion principal del juego 
    chess_game = Chess(player)
    chess_game.show_board()
    move_number = 0

    while True: # bucle con el desarollo del juego 
        start = input("\nEnter the position of the piece you want to move (or 'exit' to end the game): ").lower()
        if start == 'exit':
            revisit = input("\nDo you want to revisit a specific move? (y/n): ").lower()
            if revisit == 'y':
                move_to_consult = int(input("Enter the move number you want to revisit: "))
                board_state = chess_game.consult_move(move_to_consult)
                if board_state:
                    print("\nBoard after move {}:".format(move_to_consult))
                    for row in board_state:
                        print(row)
                else:
                    print("\nFailed to consult the move.")
            break

        end = input("Enter the position where you wish to move your piece: ").lower()
        move_number += 1
        chess_game.move_piece(start, end, move_number)
        chess_game.show_board()

if __name__ == "__main__":
    player = input("What is the name of the game: ")
    play_chess(player)