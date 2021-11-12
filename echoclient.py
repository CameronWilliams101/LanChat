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
        print("onnection to host", host, "succeded.")
    except:
        print("connection to host", host, "failed.")
        return
    
    # Send a msg to host
    send()

def send():
    global conn

    try:
        # sendall sending message
        request = input("\nEnter a msg: ")
        request = request.encode("ISO-8859-1")
        conn.sendall(request)
    finally:
        conn.close()