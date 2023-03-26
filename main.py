import threading
import nltk
import tkinter as tk
from tkinter import ttk
from src.bot import chatbot, load_default_responses, load_excluded_words
from src.config import BOT_NAME


def download_nltk_data():
    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)


class ChatbotUI(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Messages frame
        self.messages_frame = ttk.Frame(self, padding=10)
        self.messages_frame.pack(fill="both", expand=True)

        # Chatbox
        self.chatbox = tk.Text(self.messages_frame, height=20, width=80, font=("Segoe UI", 12))
        self.chatbox.pack(side=tk.LEFT, fill="both", expand=True)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.messages_frame, orient="vertical", command=self.chatbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")
        self.chatbox.config(yscrollcommand=self.scrollbar.set, state="disabled")

        # Input frame
        self.input_frame = ttk.Frame(self, padding=10)
        self.input_frame.pack(fill="x")

        # Input field
        self.input_field = ttk.Entry(self.input_frame, width=80, font=("Segoe UI", 12))
        self.input_field.pack(side=tk.LEFT, fill="x", expand=True, padx=5, pady=5)
        self.input_field.bind("<Return>", self.send_message)

        # Send button
        self.send_button = ttk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT)

        # Configure tag for user and bot messages
        self.chatbox.tag_configure("user", foreground="#007bff", font=("Segoe UI", 12, "bold"))
        self.chatbox.tag_configure("bot", foreground="#28a745", font=("Segoe UI", 12, "bold"))

    def send_message(self, event=None):
        message = self.input_field.get()
        self.input_field.delete(0, tk.END)
        self.chatbox.config(state="normal")

        # Add user message with different font color and style
        self.chatbox.insert(tk.END, "You: ", "user")
        self.chatbox.insert(tk.END, f"{message}\n")

        # Start a new thread to handle the chatbot logic
        threading.Thread(target=self.handle_chatbot_response, args=(message,), daemon=True).start()

    def handle_chatbot_response(self, message):
        # Add bot response with different font color and style
        response = chatbot(message)
        self.chatbox.config(state="normal")
        self.chatbox.insert(tk.END, f"{BOT_NAME}: ", "bot")
        self.chatbox.insert(tk.END, f"{response}\n")
        self.chatbox.config(state="disabled")
        self.chatbox.see(tk.END)

    def run(self):
        threading.Thread(target=download_nltk_data).start()
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Chatbot")
    root.resizable(False, False)
    app = ChatbotUI(master=root)
    app.run()
