def chatbot():
    print("AI Bot: Hello! Type 'bye' to exit.")
    
    while True:
        user = input("You: ").lower()
        
        if user == "hello":
            print("AI Bot: Hi there!")
        elif user == "how are you":
            print("AI Bot: I'm just code, but I'm doing great!")
        elif user == "bye":
            print("AI Bot: Goodbye!")
            break
        else:
            print("AI Bot: I don't understand.")

chatbot()