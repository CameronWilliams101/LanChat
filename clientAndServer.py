import socket
import threading

port = 5000

# Starting threads. Program will wait for threads to end before closing.
def start():
    threading.Thread(target=server).start()
    threading.Thread(target=client).start()


# Starting server with a TCP socket. And start the thread to handle a connecting client
def server():
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        listener.bind(('', port))
        listener.listen(5)
        print("Server is listening on port", port, '\n')

        while True:
            connFromClient = listener.accept()[0]
            handleClient(connFromClient)
    finally:
        print("Closing Server")
        listener.close()

# Handles a client who has connected to this server by parsing the incoming msg
def handleClient(connFromClient):
    try:
        # make sure to recieve all the bytes, loop until none left to get
        chunks = []
        chunk = connFromClient.recv(4096)      
        while len(chunk) > 0:
            chunks.append(chunk.decode("ISO-8859-1"))
            chunk = connFromClient.recv(4096)
        incomingMsg = ''.join(chunks)

        print("INCOMING MSG:", incomingMsg, "\n\n")
    finally:
        connFromClient.close()


# establishing tcp socket connection
def client():
    serverIP = input("Enter server IP addr you want to connect with:")
    print("Type your messages")
    while True:
        connToServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            connToServer.connect((serverIP, port))
        except:
            return
        
        # Send a msg to host
        send(connToServer)

def send(connToServer):
    try:
        # sendall sending message
        request = input("MY MSG:")
        print("\n")
        request = request.encode("ISO-8859-1")
        connToServer.sendall(request)
    finally:
        return