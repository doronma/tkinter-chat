""" UI Properties Dialog Code"""
import tkinter as tk


class PropertiesFrame(tk.Frame):
    """ This class creates a frame for my program window """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent_frame = parent
        self.host_var = None
        self.port_var = None
        self.user_var = None
        self.password_var = None
        self.nickname_var = None
        self.state_signup = False
        self.create_properties_window()

    def create_properties_window(self):

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        caption = tk.Label(self, name="caption", text="Chat Login Form",
                           font=('Aerial', 14))
        caption.grid(column=0, row=0, sticky=tk.W)

        self.generate_host_field()
        self.generate_port_field()
        self.generate_user_field()
        self.generate_password_field()

        self.generate_button_frame()

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=5)
        self.pack()

    def generate_button_frame(self):
        login_button = tk.Button(self, name="btn_login", text="Login", bg="blue", fg="white",
                                 command=lambda: self.parent_frame.login(
                                     self.host_var.get(),
                                     self.port_var.get(),
                                     self.user_var.get(),
                                     self.password_var.get()))
        login_button.grid(column=0, row=8, sticky=tk.W)
        register_button = tk.Button(
            self, name="btn_signin", text="Signin", bg="blue", fg="white", command=self.cb_signin)
        register_button.grid(column=1, row=8, sticky=tk.W)

    def cb_signin(self):
        if not self.state_signup:
            self.children['caption'].configure(text="Chat Signin Form")
            self.children['btn_login'].grid_remove()
            self.children['btn_signin'].configure(text="OK")
            self.generate_nickname_field()
            self.state_signup = True
            self.children['lblError'].configure(text="")
        else:
            self.parent_frame.signin(
                                     self.host_var.get(),
                                     self.port_var.get(),
                                     self.user_var.get(),
                                     self.password_var.get(),
                                     self.nickname_var.get())

            self.children['caption'].configure(text="Chat Login Form")
            self.children['btn_login'].grid(column=0, row=8, sticky=tk.W)
            self.children['nickname_label'].grid_remove()
            self.children['nickname_field'].grid_remove()
            self.children['btn_signin'].grid_remove()
            self.user_var.set("")
            self.password_var.set("")

    def generate_password_field(self):
        password_label = tk.Label(self, text="Password:",
                                  font=('Aerial', 12))
        password_label.grid(column=0, row=5, sticky=tk.W)
        self.password_var = tk.StringVar()  # For the messages to be sent.
        self.password_var.set("")
        password_field = tk.Entry(
            self, textvariable=self.password_var, show="*")
        password_field.grid(column=1, row=5, sticky=tk.W)

    def generate_user_field(self):
        user_label = tk.Label(self, text="Mail:",
                              font=('Aerial', 12))
        user_label.grid(column=0, row=4, sticky=tk.W)
        self.user_var = tk.StringVar()  # For the messages to be sent.
        self.user_var.set("")
        user_field = tk.Entry(self, textvariable=self.user_var)
        user_field.grid(column=1, row=4, sticky=tk.W)

    def generate_port_field(self):
        port_label = tk.Label(self, text="Port Number:",
                              font=('Aerial', 12))
        port_label.grid(column=0, row=3, sticky=tk.W)
        self.port_var = tk.StringVar()  # For the messages to be sent.
        self.port_var.set("33000")
        port_field = tk.Entry(self, textvariable=self.port_var)
        port_field.grid(column=1, row=3, sticky=tk.W)

    def generate_host_field(self):
        label = tk.Label(self, text="Host Name:",
                         font=('Aerial', 12))
        label.grid(column=0, row=2, sticky=tk.W)
        self.host_var = tk.StringVar()  # For the messages to be sent.
        self.host_var.set("localhost")
        host_field = tk.Entry(self, textvariable=self.host_var)
        host_field.focus()
        host_field.grid(column=1, row=2, sticky=tk.W)

    def generate_nickname_field(self):
        nickname_label = tk.Label(self, name="nickname_label", text="Nickname:",
                                  font=('Aerial', 12))
        nickname_label.grid(column=0, row=6, sticky=tk.W)
        self.nickname_var = tk.StringVar()  # For the messages to be sent.
        self.nickname_var.set("")
        nickname_field = tk.Entry(
            self, name="nickname_field", textvariable=self.nickname_var)
        nickname_field.grid(column=1, row=6, sticky=tk.W)
