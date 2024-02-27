import socket
import threading

class battleship:

    def __init__(self):
        self.first_row = ["0","1","2","3","4","5","6","7","8","9"]
        self.board = [[" "," "," "," "," "," "," "," "," "," "],
                      [" "," "," "," "," "," "," "," "," "," "],
                      [" "," "," "," "," "," "," "," "," "," "],
                      [" "," "," "," "," "," "," "," "," "," "],
                      [" "," "," "," "," "," "," "," "," "," "],
                      [" "," "," "," "," "," "," "," "," "," "],
                      [" "," "," "," "," "," "," "," "," "," "],
                      [" "," "," "," "," "," "," "," "," "," "],
                      [" "," "," "," "," "," "," "," "," "," "],
                      [" "," "," "," "," "," "," "," "," "," "],
                      [" "," "," "," "," "," "," "," "," "," "],]
        self.turn = "X"
        self.you = "X"
        self.opponent = "O"
        self.ship_coords = None
        self.winner = None
        self.game_over = False
        self.turn_count = 1

    def host_game(self, host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)

        client, addr = server.accept()

        self.you = "X"
        self.opponent = "O"
        threading.Thread(target=self.handle_connection, args=(client,)).start()
        server.close()

    def connect_to_game(self, host, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        self.you = "X"
        self.opponent = "O"
        threading.Thread(target=self.handle_connection, args=(client,)).start()
        
        
    def handle_connection(self, client):
        while not self.game_over:
            
            if self.turn == self.you:
                if self.turn_count == 1:
                    #build game here
                    placement = input("Enter coordinates for your ship (row, column): ")
                    print("Received placement:", placement)
                    if self.check_valid_move(placement.split(',')):
                        self.place_ship(placement.split(','))
                        self.turn = self.opponent
                        client.send(placement.encode('utf-8'))
                        self.turn_count +=1
                    else:
                        print("Not a valid move")
                else:
                    move = input("Enter coordinates (row, column): ")
                    print("Received move:", move)
                    if self.check_valid_move(move.split(',')):
                        self.make_move(move.split(','), self.you)
                        self.turn = self.opponent
                        client.send(move.encode('utf-8'))
                        self.turn_count +=1
                    else:
                        print("Not a valid move")
            else:
                try:
                    data = client.recv(1024)
                    if not data:
                        break
                    else:
                        if self.turn_count < 3:
                            self.place_ship(data.decode('utf-8').split(','))
                            self.turn = self.you
                        else:
                            self.make_move(data.decode('utf-8').split(','), self.opponent)
                            self.turn = self.you
                except ConnectionAbortedError as e:
                    print("Connection was ended. This most likely means your opponent hit your battleship. Either way, you lose!")
                    break
        client.close()

    def place_ship(self, placement):
        self.user_ship_coords = tuple(map(int, placement))

    
    def make_move(self, move, player):
        if self.game_over:
            return
        
        x, y = map(int, move) 
        if (x, y) == self.user_ship_coords:
            self.game_over = True
            self.winner = self.you
            print("You sunk their ship. You Win!")
            return 
        self.board[x][y] = player
        self.print_board()


    def check_valid_move(self, move):
        x, y = map(int, move)
        return self.board[x][y] == " "
    
    def clear_console(self):
        print('\n' * 100) 

    def print_board(self):
        self.clear_console()
        row_number = 0

        print("_" * 43)
        print(" " + " | " + " | ".join(self.first_row) + " |")
        print("-" * 43)
        for row in range(11):
            if row != 0:
                print(f"{row_number}"" | " + " | ".join(self.board[row]) + " |") 
                row_number += 1
                if row < 10:
                    print("-" * 43)
        print("-" * 43)

game = battleship()
game.connect_to_game("localhost", 9999)