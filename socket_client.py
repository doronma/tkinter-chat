#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


BUFSIZ = 1024


class SocketClient:
    def __init__(self,  view_dispatcher):

        self.view_dispatcher = view_dispatcher
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        # self.client_socket.connect(ADDR)

    def receive(self):
        """Handles receiving of messages."""
        while True:
            try:
                msg = self.client_socket.recv(BUFSIZ).decode("utf8")
                self.view_dispatcher("RECEIVE", msg)
            except OSError:  # Possibly client has left the chat.
                break

    def eventDispatcher(self, type, data=None):
        """ Manage events from gui """
        match type:
            case "CONNECT":
                print("connecting")
                # HOST = "localhost"
                # PORT = 33000
                host, port, user = data
                ADDR = host, port
                self.client_socket.connect(ADDR)
                """ Start Socket Listning Thred """
                receive_thread = Thread(target=self.receive)
                receive_thread.start()
                self.client_socket.send(bytes(user, "utf8"))

            case "SEND_MESSAGE":
                self.client_socket.send(bytes(data, "utf8"))
            case "EXIT":
                self.client_socket.close()
