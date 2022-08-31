""" UI Properties Dialog Code"""
import tkinter as tk


class PropertiesFrame(tk.Frame):
    """ This class creates a frame for my program window """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent_frame = parent
        self.create_properties_window()

    def create_properties_window(self):

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        label = tk.Label(self, text="Host Name:",
                         font=('Aerial', 12))
        label.grid(column=0, row=0, sticky=tk.W)

        host_var = tk.StringVar()  # For the messages to be sent.
        host_var.set("localhost")
        host_field = tk.Entry(self, textvariable=host_var)
        host_field.focus()
        host_field.grid(column=1, row=0, sticky=tk.W)

        port_label = tk.Label(self, text="Port Number:",
                              font=('Aerial', 12))
        port_label.grid(column=0, row=1, sticky=tk.W)

        port_var = tk.StringVar()  # For the messages to be sent.
        port_var.set("33000")
        port_field = tk.Entry(self, textvariable=port_var)
        port_field.grid(column=1, row=1, sticky=tk.W)

        user_label = tk.Label(self, text="User Name:",
                              font=('Aerial', 12))
        user_label.grid(column=0, row=2, sticky=tk.W)

        user_var = tk.StringVar()  # For the messages to be sent.
        user_var.set("guest")
        user_field = tk.Entry(self, textvariable=user_var)
        user_field.grid(column=1, row=2, sticky=tk.W)

        password_label = tk.Label(self, text="Password:",
                                  font=('Aerial', 12))
        password_label.grid(column=0, row=3, sticky=tk.W)
        password_var = tk.StringVar()  # For the messages to be sent.
        password_var.set("")
        password_field = tk.Entry(
            self, textvariable=password_var)
        password_field.grid(column=1, row=3, sticky=tk.W)

        button_frame = tk.Frame(self, bg="gray71")
        save_button = tk.Button(button_frame, text="Save", bg="blue", fg="white",
                                command=lambda: self.parent_frame.save_properties(
                                    host_var.get(),
                                    port_var.get(),
                                    user_var.get(),
                                    password_var.get()))
        save_button.grid(column=0, row=0, sticky=tk.W)

        button_frame.grid(column=0, row=4)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=5)
        self.pack()
