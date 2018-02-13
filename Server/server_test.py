import socket
import threading
import time
class Server:
    #parameters for the server
    client_sock = None
    def __init__(self, server_num):
        self.bind_ip = '192.168.42.1'
        self.port_numbers = [4999, 3999, 5999] #0 = gesture, #1 = button/wire, #2 = screen2
        self.bind_port = self.port_numbers[server_num]

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.bind_ip, self.bind_port))
        self.server.listen(5)  # max backlog of connections
        self.result = "Nothing Yet"
        print 'Listening on {}:{}'.format(self.bind_ip, self.bind_port)

    #Sends a message to the client to indicate the start of a game, then received the result of that game    
    def handle_client_connection(self, client_socket, game_code):
        client_socket.send(game_code)

        self.result = client_socket.recv(1024)

        while True:
            msg = client_socket.recv(1024)
            time.sleep(1)
            if msg != "":
                self.result = msg

    def get_result(self):
        return self.result

    #Starts the server, waits for a connection with a client, receives the result of the game(Fail or Success)
    def start_server(self, game_code):
        while True:
            self.client_sock, address = self.server.accept()
            print 'Accepted connection from {}:{}'.format(address[0], address[1])
            result = self.handle_client_connection(self.client_sock, game_code)                              
            return result
            

    def send(self, message):
        self.client_sock.send(message)

    def set_result(self, code):
        self.result =  code
if __name__ == '__main__':
    server_number = 0
    g = Server(server_number)
    code = "ReRe"
    c = g.start_server(code)
    print c
