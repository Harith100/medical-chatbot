import tkinter as tk
from tkinter import scrolledtext
from main import Brain  # Assuming the Brain class is defined in main.py

# Initialize the Brain class for handling responses
brain = Brain()

class ChatbotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("400x500")
        
        # Display area for the chat
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", font=("Arial", 12))
        self.chat_display.place(x=10, y=10, width=380, height=400)
        
        # Entry box for user input
        self.entry_box = tk.Entry(root, font=("Arial", 12))
        self.entry_box.place(x=10, y=420, width=300, height=30)
        
        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message, font=("Arial", 12))
        self.send_button.place(x=320, y=420, width=60, height=30)
        
    def send_message(self):
        # Get the user message and display it in the chat area
        user_message = self.entry_box.get().strip()
        if user_message:
            self.display_message("You: " + user_message)
            self.entry_box.delete(0, tk.END)  # Clear the entry box
            
            try:
                # Get the bot's response
                response = self.get_bot_response(user_message)  
                print(f"Bot Response: {response}")  # Debugging: print the response
                self.display_message("Bot: " + response)  # Display the bot's response
            except Exception as e:
                self.display_message("Bot: Sorry, I couldn't process that.")  # Fallback message
                print(f"Error while getting response: {e}")  # Log the error for debugging
            
    def display_message(self, message):
        self.chat_display.config(state="normal")  # Enable editing to add text
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.config(state="disabled")  # Disable editing after adding text
        self.chat_display.yview(tk.END)  # Auto-scroll to the end of the chat
        
    def get_bot_response(self, message):
        # Generate a response from the brain instance
        reply = brain.generate(message)  # Pass the user message to the generate method
        return reply

# Run the UI
if __name__ == "__main__":
    root = tk.Tk()
    chat_ui = ChatbotUI(root)
    root.mainloop()
