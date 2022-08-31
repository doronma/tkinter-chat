#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
import json
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

user_dict = {"Dave": "12345", "Yaara": "23456", "guest": ""}


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print(f"{client_address} has connected.")
        addresses[client] = client_address
        # creats a thred for  spasific client
        Thread(target=handle_client, args=(client,)).start()


def login_ok(name, password):
    if name in user_dict:
        return user_dict[name] == password
    return False


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    action_data_json = client.recv(BUFSIZ).decode("utf8")
    action_data = json.loads(action_data_json)
    user_data = action_data['user_data']
    name = user_data['user']

    # Login OK
    if login_ok(name, user_data['password']):
        welcome = f'Welcome {name}! If you ever want to quit, type {{quit}} to exit.'
        client.send(bytes("OK", "utf8"))
        client.send(bytes(welcome, "utf8"))
        msg = f"{name} has joined the chat!"
        start_brodcast(client, name, msg)
    # Login Failure
    else:
        client.send(bytes("ERROR", "utf8"))
        client.close()


def start_brodcast(client, name, msg):
    broadcast(bytes(msg, "utf8"))
    # addds the client to the dict so that the brodcast could work
    clients[client] = name

    while True:
        # gets msg from the client and sends it to everyone else.
        msg = client.recv(BUFSIZ)
        print(msg.decode("utf8"))
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            #client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes(f"{name} has left the chat.", "utf8"))
            break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)


clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    # specifies the number of unaccepted connections that the system will allow
    # before refusing new connections
    SERVER.listen(5)
    print("Waiting for connection...")
    # creats a thread which takes care of clients
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
