#!/usr/bin/env python3
"""Main Client App"""
import tkinter as tk
from gui.chat_gui_ui import MainView
from socket_client import SocketClient

if __name__ == '__main__':

    root = tk.Tk()
    root.geometry('400x300')
    view = MainView(root)

    socket_client = SocketClient(view.event_dispatcher)
    view.set_event_dispatcher(socket_client.event_dispatcher)

    def cb_on_closing(event=None):
        view.force_quit()

    root.protocol("WM_DELETE_WINDOW", cb_on_closing)

    root.mainloop()
