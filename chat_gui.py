import tkinter as tk


class MainView(tk.Frame):

    def __init__(self, master, event_dispatcher):
        self.master = master
        self.event_dispatcher = event_dispatcher
        tk.Frame.__init__(self, self.master)
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        self.pack()

    def create_widgets(self):
        self.generate_messages_frame()
        self.generate_message()
        self.create_entry_field()
        self.create_send_button()

    def generate_messages_frame(self):
        messages_frame = tk.Frame(self)

        scrollbar = tk.Scrollbar(messages_frame)
        self.msg_list = tk.Listbox(messages_frame, height=15,
                                   width=50, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.msg_list.pack()
        messages_frame.pack()

    def generate_message(self):
        self.my_msg = tk.StringVar()  # For the messages to be sent.
        self.my_msg.set("Type your messages here.")

    def create_entry_field(self):
        entry_field = tk.Entry(self, textvariable=self.my_msg)
        entry_field.bind("<Return>", self.send)
        entry_field.pack()

    def create_send_button(self):
        send_button = tk.Button(self, text="Send", command=self.send)
        send_button.pack()

    def send(self, event=None):
        msg = self.my_msg.get()
        self.my_msg.set("")  # Clears input field.
        self.event_dispatcher("SEND_MESSAGE", msg)
        if msg == "{quit}":
            self.event_dispatcher("EXIT")
            self.quit()

    def force_quit(self):
        self.my_msg.set("{quit}")
        self.send()

    def receive(self, event):
        print("got - " + event)
        self.msg_list.insert(tk.END, event)


if __name__ == '__main__':
    root = tk.Tk()
    root.title = ("Chat Client")
    main_app = MainApplication(root)
    root.mainloop()
