import socket

HOST = '169.254.23.12'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

gnd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    gnd.bind((HOST, PORT))
    gnd.listen()
    conn, addr = gnd.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

except:
    gnd.close()