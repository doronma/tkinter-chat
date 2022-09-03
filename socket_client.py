#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
import json
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


BUFSIZ = 1024


class SocketClient:
    """Socket Client Side Class"""

    def __init__(self,  view_dispatcher):

        self.view_dispatcher = view_dispatcher
        self.client_socket = None

    def receive(self):
        """Handles receiving of messages."""
        while True:
            try:
                msg = self.client_socket.recv(BUFSIZ).decode("utf8")
                self.view_dispatcher("RECEIVE", msg)
            except OSError:  # Possibly client has left the chat.
                break

    def event_dispatcher(self, event_type, data=None):
        """ Manage events from gui """
        match event_type:
            case "CONNECT":
                self.client_socket = socket(AF_INET, SOCK_STREAM)
                print("connecting")
                # HOST = "localhost"
                # PORT = 33000
                connection_data, action_data = data
                self.client_socket.connect(connection_data)
                print("sending")
                print(json.dumps(action_data))
                self.client_socket.send(bytes(json.dumps(action_data) , "utf8"))
                msg = self.client_socket.recv(BUFSIZ).decode("utf8")
                print("Message is - " + msg)
                if msg == "OK":
                    self.view_dispatcher("LOGIN_OK")
                    # Start Socket Listning Thred
                    receive_thread = Thread(target=self.receive)
                    receive_thread.start()
                elif msg == "SIGNIN":
                    pass

                else:
                    self.view_dispatcher("LOGIN_ERROR")
                    print("Erorr message is - " + msg)
                    self.client_socket.close()


            case "SEND_MESSAGE":
                self.client_socket.send(bytes(data, "utf8"))
            case "EXIT":
                self.client_socket.close()
