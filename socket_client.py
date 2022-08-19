#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM

HOST = "localhost"
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)


class SocketClient:
    def __init__(self,  view_dispatcher):

        self.view_dispatcher = view_dispatcher
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(ADDR)

    def receive(self):
        """Handles receiving of messages."""
        while True:
            try:
                msg = self.client_socket.recv(BUFSIZ).decode("utf8")
                self.view_dispatcher("RECEIVE", msg)
            except OSError:  # Possibly client has left the chat.
                break

    def eventDispatcher(self, type, msg=None):
        """ Manage events from gui """
        match type:
            case "SEND_MESSAGE":
                self.client_socket.send(bytes(msg, "utf8"))
            case "EXIT":
                self.client_socket.close()
