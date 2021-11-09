import socket

host = ""
conn = None

def start(ip):
    global host
    global conn

    # Parse url to host and uri
    host = ip

    # establishing tcp socket connection
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        conn.connect((host, 80))
    except:
        print("connection to host failed")
    
    # determine http method
    send()

def send():
    global conn

    try:
        # sendall sending request http message
        request = "users msg input"
        conn.sendall(request)

        # make sure to recieve all the bytes, loop until none left to get
        chunks = []
        chunk = conn.recv(4096)      
        while len(chunk) > 0:
            chunks.append(chunk.decode("ISO-8859-1"))
            chunk = conn.recv(4096)

        # compile now whole response
        response = ''.join(chunks)
        print(response)
    finally:
        conn.close()