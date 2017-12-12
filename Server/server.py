import socket
import threading

class Server:
    #parameters for the server
    def __init__(self):
        self.bind_ip = '192.168.42.1'
        self.bind_port = 4999

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.bind_ip, self.bind_port))
        self.server.listen(5)  # max backlog of connections
        print 'Listening on {}:{}'.format(self.bind_ip, self.bind_port)

    #Sends a message to the client to indicate the start of a game, then received the result of that game    
    def handle_client_connection(self, client_socket, game_code):
        client_socket.send(game_code)
        request = client_socket.recv(1024)
        if request == "Fail":
            client_socket.close() 
            return(0)
        if request == "Success":
            client_socket.close() 
            return(1)
            
    #Starts the server, waits for a connection with a client, receives the result of the game(Fail or Success)
    def start_server(self, game_code):
        while True:
            client_sock, address = self.server.accept()
            print 'Accepted connection from {}:{}'.format(address[0], address[1])
            result = self.handle_client_connection(client_sock, game_code)                              
            return result
            

if __name__ == '__main__':
    g = Server()
    code = "1234"
    c = g.start_server(code)
    print c
