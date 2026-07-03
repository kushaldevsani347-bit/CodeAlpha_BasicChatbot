from datetime import datetime
import random

jokes = [
    "Why do programmers prefer Python? Because it's easy to understand!",
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "Debugging: Being the detective in a crime movie where you're also the criminal!"
]

quotes = [
    "Success comes to those who never give up.",
    "Every expert was once a beginner.",
    "Keep learning, keep growing.",
    "Dream big, work hard, stay consistent."
]

print("=" * 55)
print("        WELCOME TO CODEALPHA CHATBOT")
print("=" * 55)
print("Type 'help' to see available commands.")
print("Type 'bye' to exit.\n")

while True:

    user = input("You: ").lower().strip()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you today?")

    elif user == "how are you":
        print("Bot: I'm doing great! Hope you're having a wonderful day.")

    elif user in ["your name", "who are you"]:
        print("Bot: I'm CodeAlpha Rule-Based ChatBot.")

    elif user == "who created you":
        print("Bot: I was created by a CodeAlpha Python Intern.")

    elif user == "time":
        print("Bot:", datetime.now().strftime("%H:%M:%S"))

    elif user == "date":
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))

    elif user == "joke":
        print("Bot:", random.choice(jokes))

    elif user == "quote":
        print("Bot:", random.choice(quotes))

    elif user in ["thank you", "thanks"]:
        print("Bot: You're welcome! 😊")

    elif user == "what can you do":
        print("Bot: I can greet you, tell the date and time, share jokes and quotes, and answer simple questions.")

    elif user == "weather":
        print("Bot: Sorry, I can't access live weather information right now.")

    elif user == "help":
        print("\nAvailable Commands:")
        print("- hello")
        print("- how are you")
        print("- your name")
        print("- who created you")
        print("- time")
        print("- date")
        print("- joke")
        print("- quote")
        print("- weather")
        print("- what can you do")
        print("- thank you")
        print("- bye")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day. 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see available commands.")