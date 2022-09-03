""" UI About Frame"""
import tkinter as tk


class AboatFrame():
    """ UI About Frame Class"""
    def __init__(self, master):
        self.master = master
        self.about_window = tk.Toplevel(master)
        self.create_about_dialog()

    def create_about_dialog(self):

        self.about_window.geometry("500x150")
        self.about_window.iconbitmap('./gui/icons/Chat.ico')
        # Create a Label Text
        dialog_text = "this is a chat pogram witch uses python, gui and threds"
        label = tk.Label(self.about_window, text=dialog_text,
                         font=('Aerial', 12))
        label.pack(pady=20)
        # Add a Frame
        frame = tk.Frame(self.about_window, bg="gray71")
        frame.pack(pady=10)
        # Add Button for making selection
        button = tk.Button(frame, text="Close",
                           command=self.about_window.destroy, bg="blue", fg="white")
        button.grid(row=0, column=1)
