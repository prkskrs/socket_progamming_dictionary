import socket
server = socket.socket()
print("socket created")

dictt={"School":"place to learn","Writer h":"wh","Writer":"writer meaning","Creator":"creator meaning","Playground":"playground meaning"}
server.bind(("localhost",9999)) 
server.listen(3) 
print("waiting for connections")
while(True):
    client,addr = server.accept() 
    name = client.recv(1024).decode()
    name=name.capitalize()
    if(name in dictt):
        meaning = dictt[name]
        client.send(bytes(f"{meaning}","utf-8")) 
    else:
        client.send(bytes("No such word in dictionary","utf-8")) 
    client.close()
