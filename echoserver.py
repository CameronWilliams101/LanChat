import socket
import threading

port = 80

def start(p):
    global port
    if p:
        port = p

    # Starting http server with a TCP socket
    # and start the thread to handle a connecting client
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        listener.bind(('', port))
        listener.listen(5)
        print('HTTP file server is listening at', port, '\n')

        while True:
            conn, addr = listener.accept()
            threading.Thread(target=handleClient, args=(conn, addr)).start()
    finally:
        print("Closing Program")
        listener.close()


# Handles a client who has connected to this server by parsing the http response and returning an http request
def handleClient(conn, addr):
    print('New client from', addr)
    try:
        data = conn.recv(4096)
        data = data.decode("ISO-8859-1")
        conn.sendall(data)
    finally:
        print("--------Connection Closed.--------\n")
        conn.close()