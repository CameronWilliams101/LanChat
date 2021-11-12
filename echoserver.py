import socket
import threading

port = 80

def start(p):
    global port
    if p:
        port = p

    # Starting server with a TCP socket. And start the thread to handle a connecting client
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        listener.bind(('', port))
        listener.listen(5)
        print("Server is listening on port", port, '\n')

        while True:
            conn, addr = listener.accept()
            threading.Thread(target=handleClient, args=(conn, addr)).start()
    finally:
        print("Closing Program")
        listener.close()


# Handles a client who has connected to this server by parsing the incoming msg
def handleClient(conn, addr):
    print("New client from", addr)

    try:
        # make sure to recieve all the bytes, loop until none left to get
        chunks = []
        chunk = conn.recv(4096)      
        while len(chunk) > 0:
            chunks.append(chunk.decode("ISO-8859-1"))
            chunk = conn.recv(4096)

        # compile now whole response
        incomingMsg = ''.join(chunks)

        print("INCOMING MSG: ", incomingMsg)
    finally:
        print("--------Connection Closed.--------\n")
        conn.close()