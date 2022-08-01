#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter as tk
from chat_gui import MainView

HOST = "localhost"
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            view.receive(msg)
        except OSError:  # Possibly client has left the chat.
            break


def eventDispatcher(type, msg=None):
    """ Manage events from gui """
    match type:
        case "SEND_MESSAGE":
            client_socket.send(bytes(msg, "utf8"))
        case "EXIT":
            client_socket.close()


""" Create GUI Application """
root = tk.Tk()
view = MainView(root, eventDispatcher)


def on_closing(event=None):
    view.force_quit()


root.protocol("WM_DELETE_WINDOW", on_closing)

""" Start Socket Thred """
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
receive_thread = Thread(target=receive)
receive_thread.start()

""" Start GUI Main Loop"""
root.mainloop()
