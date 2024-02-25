import json
import re
import random_responses
import tkinter as tk

# Function to load JSON data from a file
def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)
    
# Load bot responses from the JSON file
responses_data = load_json("bot.json")

# Function to get a response based on user input
def get_response(input_string):
    # Split the input string into words
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Iterate through each response in the JSON data
    for response in responses_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

         # If there are required words for the response, calculate the score
        if required_words:
            for word in split_message:
                if word in required_words:
                    response_score += 1

        # If required words are present, calculate the score based on user input
        if required_score == len(required_words):
            for word in split_message:
                if word in response["user_input"]:
                    response_score += 1
    
        score_list.append(response_score)

    # Find the best response based on the highest score
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # If the input is empty, prompt the user to type something
    if input_string == "":
        return "Please type something so we can chat :D"

    # If a suitable response is found, return it
    if best_response != 0:
        return responses_data[response_index]["bot_response"]
    
    # If no suitable response is found, return a random response from the provided module
    return random_responses.random_string()

# Function to send a message
def send_message():
    message = message_entry.get()
    if message:
        # Display user message in the message history
        message_history.config(state=tk.NORMAL)
        message_history.insert(tk.END, f"You: {message}\n")
        message_history.config(state=tk.DISABLED)

        # Get and display bot response
        bot_response = get_response(message)
        message_history.config(state=tk.NORMAL)
        message_history.insert(tk.END, f"Bot: {bot_response}\n")
        message_history.config(state=tk.DISABLED)
        
        message_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("ChatBot")
root["bg"] = "black"

# Create a Text widget for message history
message_history = tk.Text(root, wrap=tk.WORD, width=60, height=20)
message_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
message_history.config(state=tk.DISABLED)

# Create an Entry widget for entering messages
message_entry = tk.Entry(root, width=60)
message_entry.grid(row=1, column=0, padx=10, pady=10)

# Create a "Send" button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()