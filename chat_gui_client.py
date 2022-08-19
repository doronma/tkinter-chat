#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from threading import Thread
import tkinter as tk
from chat_gui_ui import MainView
from socket_client import SocketClient

if __name__ == '__main__':

    """ Create GUI  """
    root = tk.Tk()
    view = MainView(root)
    socket_client = SocketClient(view.event_dispatcher)
    view.set_event_dispatcher(socket_client.eventDispatcher)

    def on_closing(event=None):
        view.force_quit()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    """ Start Socket Listning Thred """
    receive_thread = Thread(target=socket_client.receive)
    receive_thread.start()

    """ Start GUI Main Loop"""
    root.mainloop()
