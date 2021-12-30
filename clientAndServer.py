import socket
import threading
import lanChat

port = 5000

# Starting threads. Program will wait for threads to end before closing.
def start(txtBox):
    lanChat.txtBox = txtBox
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

        lanChat.Print("THEM:" + str(incomingMsg), "blue")
    finally:
        connFromClient.close()


def connAndSend(targetIP, msg):
    # establishing tcp socket connection
    connToServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connToServer.connect((targetIP, port))
    except:
        lanChat.Print("Connection failure")
        return

    # Send a msg to host
    try:
        msg = msg.encode("ISO-8859-1")
        connToServer.sendall(msg)
        lanChat.Print("YOU:" + msg.decode("ISO-8859-1"))
    except:
        lanChat.Print("Failed to send")
        return