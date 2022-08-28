import tkinter as tk


class MainView(tk.Frame):

    def __init__(self, master):
        self.master = master

        tk.Frame.__init__(self, self.master)
        self.configure_gui()
        self.create_widgets()

    def set_event_dispatcher(self, event_dispathcer):
        self.event_dispatcher = event_dispathcer

    def configure_gui(self):
        self.pack()

    def create_widgets(self):
        self.create_menu()
        self.create_properties_window()

    def generate_messages_frame(self):
        self.messages_frame = tk.Frame(self)

        scrollbar = tk.Scrollbar(self.messages_frame)
        self.msg_list = tk.Listbox(self.messages_frame, height=15,
                                   width=100, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.msg_list.pack()
        self.messages_frame.pack()

    def generate_message(self):
        self.my_msg = tk.StringVar()  # For the messages to be sent.

    def create_entry_field(self):
        entry_field = tk.Entry(self, textvariable=self.my_msg)
        entry_field.bind("<Return>", self.send)
        entry_field.pack()

    def create_send_button(self):
        send_button = tk.Button(self, text="Send", command=self.send)
        send_button.pack()

    def create_menu(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = tk.Menu(menu, tearoff=0)
        fileMenu.add_command(label="Exit", command=self.force_quit)
        menu.add_cascade(label="File", menu=fileMenu)

        helpMenu = tk.Menu(menu, tearoff=0)
        helpMenu.add_command(label="About", command=self.aboutProgram)
        menu.add_cascade(label="Help", menu=helpMenu)

    def aboutProgram(self):
        self.about_window = tk.Toplevel(self)
        self.about_window.geometry("500x150")
        # Create a Label Text
        label = tk.Label(self.about_window, text="this is a chat pogram witch uses python, gui and threds",
                         font=('Aerial', 12))
        label.pack(pady=20)
        # Add a Frame
        frame = tk.Frame(self.about_window, bg="gray71")
        frame.pack(pady=10)
        # Add Button for making selection
        button = tk.Button(frame, text="Close",
                           command=lambda: self.about_window.destroy(), bg="blue", fg="white")
        button.grid(row=0, column=1)

    def create_properties_window(self):
        self.properties_window = tk.Frame(self)

        self.properties_window.columnconfigure(0, weight=1)
        self.properties_window.columnconfigure(1, weight=3)

        label = tk.Label(self.properties_window, text="Host Name:",
                         font=('Aerial', 12))
        label.grid(column=0, row=0, sticky=tk.W)

        host_var = tk.StringVar()  # For the messages to be sent.
        host_var.set("localhost")
        host_field = tk.Entry(self.properties_window, textvariable=host_var)
        host_field.focus()
        host_field.grid(column=1, row=0, sticky=tk.W)

        port_label = tk.Label(self.properties_window, text="Port Number:",
                              font=('Aerial', 12))
        port_label.grid(column=0, row=1, sticky=tk.W)

        port_var = tk.StringVar()  # For the messages to be sent.
        port_var.set("33000")
        port_field = tk.Entry(self.properties_window, textvariable=port_var)
        port_field.grid(column=1, row=1, sticky=tk.W)

        user_label = tk.Label(self.properties_window, text="User Name:",
                              font=('Aerial', 12))
        user_label.grid(column=0, row=2, sticky=tk.W)

        user_var = tk.StringVar()  # For the messages to be sent.
        user_var.set("guest")
        user_field = tk.Entry(self.properties_window, textvariable=user_var)
        user_field.grid(column=1, row=2, sticky=tk.W)

        button_frame = tk.Frame(self.properties_window, bg="gray71")
        save_button = tk.Button(button_frame, text="Save", command=lambda: self.save_properties(
            host_var.get(), port_var.get(), user_var.get()), bg="blue", fg="white")
        save_button.grid(column=0, row=0, sticky=tk.W)

        button_frame.grid(column=0, row=3)

        for widget in self.properties_window.winfo_children():
            widget.grid(padx=0, pady=5)
        self.properties_window.pack()

    def save_properties(self, host, port, user):
        print(host, port, user)
        self.properties_window.destroy()
        self.generate_messages_frame()
        self.generate_message()
        self.create_entry_field()
        self.create_send_button()
        self.event_dispatcher("CONNECT", (host, int(port), user))

    def show_properties(self, host, port, user_name):
        print(host, port, user_name)
        self.messages_frame.destroy()

    def send(self, event=None):
        msg = self.my_msg.get()
        self.my_msg.set("")  # Clears input field.
        self.event_dispatcher("SEND_MESSAGE", msg)
        if msg == "{quit}":
            self.event_dispatcher("EXIT")
            self.quit()

    def force_quit(self):
        if hasattr(self, 'my_msg'):
            print("sending")
            self.my_msg.set("{quit}")
            self.send()
        self.quit()

    def receive(self, event):
        print("got - " + event)
        self.msg_list.insert(tk.END, event)

    def event_dispatcher(self, type, msg=None):
        """ Manage events from socket """
        match type:
            case "RECEIVE":
                self.receive(msg)
