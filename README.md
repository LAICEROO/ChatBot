# Chat Application
This is a simple chat application built using Python and Tkinter GUI library. The application allows users to communicate with a bot, which provides predefined responses based on user input.

## Features
- User-friendly interface for sending and receiving messages
- Bot functionality with predefined responses loaded from a JSON file
- Integration of regular expressions for message parsing

## Usage
- Enter your message in the input field and press Enter or click the Send button to send it.
- The bot will respond with a predefined message based on your input.

## Configuration
You can customize the bot responses by modifying the bot.json file. Each response consists of the following fields:
- `response_type`: Specifies the type of response (e.g., "greeting", "question", "opinion", "advice").
- `user_input`: List of keywords or phrases that trigger the bot response.
- `bot_response`: The response provided by the bot.
- `required_words` (optional): List of words required to be present in the user input for the response to be triggered.
