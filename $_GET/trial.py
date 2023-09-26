import socket

IP = '127.0.0.1'  # Use the server's IP address
PORT = 9998

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))

    message = "Hello, server!"
    client.send(message.encode('utf-8'))

    response = client.recv(1024)
    print(f"[*] Received: {response.decode('utf-8')}")

    client.close()

if __name__ == '__main__':
    main()
