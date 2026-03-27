print("Bot: Hello! I am your simple AI bot.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi there!")
    
    elif user == "how are you":
        print("Bot: I'm fine, thanks!")
    
    elif user == "what is your name":
        print("Bot: I am a simple Python bot.")
    
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    
    else:
        print("Bot: I don't understand that.")