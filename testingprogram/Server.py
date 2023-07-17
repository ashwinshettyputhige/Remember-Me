import socket
from database import check_user, create_user

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8003)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1000)
print('Server is listening on', server_address)

# Accept a connection
client_socket, client_address = server_socket.accept()
print('Connected by', client_address)

# Receive and process data from the client
data = client_socket.recv(1024).decode()  # Receive data from the client
username, password = data.split(',')  # Split the received data using a delimiter (e.g., comma)

# Check if the username and password exist
k = check_user(username, password)

print('Received username:', username)
print('Received password:', password)
# Send the data back to the client
if k == 1:
    response = f'Hi {username}, Welcome to REMEMBER ME'
    client_socket.sendall(response.encode())

    while True:
        ch = client_socket.recv(1024).decode()

        if ch == '1':
            try:
                with open(f"{username}.txt", 'r') as file:
                    # File exists, read its content
                    request1 = file.read()
                    if request1 == "":
                        with open(f"{username}.txt", 'a+') as file:
                            file.write("TO DO:")
                            request1 = file.read()
                            client_socket.sendall(request1.encode())
                    else:
                        client_socket.sendall(request1.encode())
            except FileNotFoundError:
                with open(f"{username}.txt", 'a+') as file:
                    file.write("TO DO:")

                with open(f"{username}.txt", 'r') as file:
                    request1 = file.read()
                client_socket.sendall(request1.encode())

        elif ch == '2':
            message = client_socket.recv(1024).decode()
            with open(f"{username}.txt", "a+") as file:
                message = message + "\n"
                file.write(message)
        elif ch == '3':
            line = int(client_socket.recv(1024).decode())
            with open(f"{username}.txt", 'r') as file:
                lines = file.readlines()

            if line < 1 or line > len(lines):
                print('Invalid line number.')
                raise Exception

            del lines[line - 1]

            with open(f"{username}.txt", 'w') as file:
                file.writelines(lines)

else:
    response = f'Username: {username}, Password: {password} is Not Exist. If you are new here, please register.'
    client_socket.sendall(response.encode())
    data = client_socket.recv(1024).decode()  # Receive data from the client
    username, password = data.split(',')
    create_user(username, password)

# Close the connection
client_socket.close()
server_socket.close()
