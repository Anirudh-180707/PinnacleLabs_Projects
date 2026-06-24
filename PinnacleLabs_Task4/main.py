import tkinter as tk
from tkinter import scrolledtext

# Chatbot responses
def chatbot_response(message):
    message = message.lower()

    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! Nice to meet you.",
        "how are you": "I'm doing great. How about you?",
        "what is python": "Python is a popular programming language used for software development, AI, and data science.",
        "what is ai": "AI stands for Artificial Intelligence, which enables machines to mimic human intelligence.",
        "what is machine learning": "Machine Learning is a branch of AI that allows systems to learn from data.",
        "who created python": "Python was created by Guido van Rossum.",
        "bye": "Goodbye! Have a great day!"
    }

    return responses.get(
        message,
        "Sorry, I don't understand that question. Please try something else."
    )

# Send message
def send_message():
    user_message = entry.get().strip()

    if user_message == "":
        return

    chat_area.config(state=tk.NORMAL)

    chat_area.insert(tk.END, f"You: {user_message}\n")

    bot_reply = chatbot_response(user_message)

    chat_area.insert(tk.END, f"Bot: {bot_reply}\n\n")

    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    entry.delete(0, tk.END)

# GUI Window
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("600x500")

# Chat Area
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    state=tk.DISABLED,
    font=("Arial", 11)
)

chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Input Frame
frame = tk.Frame(root)
frame.pack(fill=tk.X, padx=10, pady=10)

entry = tk.Entry(frame, font=("Arial", 12))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

send_button = tk.Button(
    frame,
    text="Send",
    command=send_message
)

send_button.pack(side=tk.RIGHT, padx=5)

# Enter key support
root.bind("<Return>", lambda event: send_message())

root.mainloop()