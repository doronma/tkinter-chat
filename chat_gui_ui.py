""" UI Code"""
import tkinter as tk
from properties_frame import PropertiesFrame


class MainView(tk.Frame):
    """ Main Frame"""

    def __init__(self, master):
        self.master = master

        tk.Frame.__init__(self, self.master)

        # setup memberes
        self.messaging_dispatcher = None
        self.messages_frame = None
        self.msg_list = None
        self.about_window = None
        self.my_msg = None
        self.properties_window = None
        # init gui
        self.configure_gui()
        self.create_widgets()

    def set_event_dispatcher(self, messaging_dispatcher):
        self.messaging_dispatcher = messaging_dispatcher

    def configure_gui(self):
        self.pack()

    def create_widgets(self):
        self.create_menu()
        #self.create_properties_window()
        self.properties_window = PropertiesFrame(self)

    def create_messages_frame(self):
        self.messages_frame = tk.Frame(self)

        scrollbar = tk.Scrollbar(self.messages_frame)
        self.msg_list = tk.Listbox(self.messages_frame, height=15,
                                   width=100, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.msg_list.pack()
        self.messages_frame.pack()

    def create_entry_field(self):
        entry_field = tk.Entry(self, textvariable=self.my_msg)
        entry_field.bind("<Return>", self.cb_send)
        entry_field.pack()

    def create_send_button(self):
        send_button = tk.Button(self, text="Send", command=self.cb_send)
        send_button.pack()

    def create_menu(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Exit", command=self.force_quit)
        menu.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(menu, tearoff=0)
        help_menu.add_command(label="About", command=self.create_about_dialog)
        menu.add_cascade(label="Help", menu=help_menu)

    def create_about_dialog(self):
        self.about_window = tk.Toplevel(self)
        self.about_window.geometry("500x150")
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


    def save_properties(self, host, port, user, password):
        print("in save properties")
        action = "login"
        action_data = { "action" : action , "user_data" : {"user":user,"password":password} }
        self.messaging_dispatcher("CONNECT",((host, int(port)), action_data ))

    def create_main_frame(self):
        self.create_messages_frame()
        self.my_msg = tk.StringVar()  # For the messages to be sent.
        self.create_entry_field()
        self.create_send_button()

    def show_properties(self, host, port, user_name):
        print(host, port, user_name)
        self.messages_frame.destroy()

    def cb_send(self, event=None):
        msg = self.my_msg.get()
        self.my_msg.set("")  # Clears input field.
        self.messaging_dispatcher("SEND_MESSAGE", msg)
        if msg == "{quit}":
            self.messaging_dispatcher("EXIT")
            self.quit()

    def force_quit(self):
        if self.my_msg:
            self.my_msg.set("{quit}")
            self.cb_send()
        self.quit()

    def receive(self, event):
        self.msg_list.insert(tk.END, event)

    def event_dispatcher(self, event_type, msg=None):
        """ Manage events from socket """
        match event_type:
            case "RECEIVE":
                self.receive(msg)
            case "LOGIN_OK":
                self.show_main_dialog()
            case "LOGIN_ERROR":
                self.show_login_error()

    def show_main_dialog(self):
        self.properties_window.destroy()
        self.create_main_frame()

    def show_login_error(self):
        error_label = tk.Label(self.properties_window, text="Wrong Password", fg='red',
                               font=('Aerial', 9,))
        error_label.grid(column=0, row=6, sticky=tk.W)
