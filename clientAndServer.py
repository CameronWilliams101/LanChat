import socket
import threading
import lanChat

port = 5000
serverIP = ""

# Starting threads. Program will wait for threads to end before closing.
def start(txtBox, sIP):
    lanChat.txtBox = txtBox
    global serverIP
    serverIP = sIP
    threading.Thread(target=server).start()


# Starting server with a TCP socket. And start the thread to handle a connecting client
def server():
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        listener.bind(('', port))
        listener.listen(5)
        lanChat.Print("Server is listening on port " + str(port) + "\n")

        while True:
            connFromClient = listener.accept()[0]
            handleClient(connFromClient)
    finally:
        lanChat.Print("Closing Server")
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

        lanChat.Print("INCOMING MSG: " + str(incomingMsg) + "\n\n")
    finally:
        connFromClient.close()


# establishing tcp socket connection
def client(msg):
    global serverIP
    lanChat.Print("Connecting to " + serverIP)
    connToServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connToServer.connect((serverIP, port))
    except:
        lanChat.Print("Failed to send, connection failure")
    
    # Send a msg to host
    try:
        # sendall sending message
        print(msg)
        msg = msg.encode("ISO-8859-1")
        connToServer.sendall(msg)
        lanChat.Print("Sent msg")
    except:
        lanChat.Print("Failed to send, sendall failure")