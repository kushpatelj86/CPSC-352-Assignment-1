There are two files(a server and a client) that communicate with each other all written in python, in order to run the program proepely you first must run the server file, because if you run the client file first, it will not know what server it'll be recieving messages from so in order to call the server file, you have to call the command " python3 server.py <port number> <key>, where the <port number> is the port number and <key> is the 16-byte key". The server will then wait for the client to connect on a specific port. When the client connects the server will recieve messages from the client, will recieve the encrypted message, decrypt the message, and print the decrypted message. After printing the message the server will go back and listen to more messages. The statement when entering the message says and prompts for user input "Please enter the message: ", the client uses the command "python3 client.py <server IP> <server port> <key> where <server IP> is the IP of the server, <server port> the port on which the server is listening, and <key> is the 16-byte encryption key". There'll be two WSL files, one for Server, and the other for the Client. 
