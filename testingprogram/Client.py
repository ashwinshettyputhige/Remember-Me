import socket

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 8003)
client_socket.connect(server_address)

# Receive the username and password from the client
username = input('Enter username: ')
password = input('Enter password: ')

# Prepare and send data to the server
data = f'{username},{password}'  # Join the username and password with a delimiter (e.g., comma)
client_socket.sendall(data.encode())

# Receive the response from the server
response = client_socket.recv(1024).decode()
print(response)

if response.startswith(f'Hi {username}'):
    while True:
        print("Enter Number:")
        print("1. Do you want to see your note:")
        print("2. Do you want to add one more line to note:")
        print("3. Do you want to delete a specific line:")
        print("4. Exit")
        ch = input()
        client_socket.sendall(ch.encode())

        if ch == '1':
            response1 = client_socket.recv(1024).decode()
            print(response1)
        elif ch == '2':
            message = input("Enter the message you want me to remember: ")
            client_socket.sendall(message.encode())
        elif ch == '3':
            line = input("Enter the line number: ")
            client_socket.sendall(line.encode())
        elif ch == '4':
            break
else:
    print("(: Register your name:(Don't forget credentials) :)")
    username = input('Enter username: ')
    password = input('Enter password: ')

    # Prepare and send data to the server
    data = f'{username},{password}'  # Join the username and password with a delimiter (e.g., comma)
    client_socket.sendall(data.encode())


# Close the connection
client_socket.close()
