import random

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm fine!", "Doing great!", "All good!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "your name": ["I am a simple AI bot.", "You can call me PyBot!"],
    "default": ["I don't understand that.", "Can you say that again?", "Hmm... interesting."]
}

def chatbot():
    print("AI Bot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "bye" in user_input:
            print("AI Bot:", random.choice(responses["bye"]))
            break

        found = False

        for key in responses:
            if key in user_input:
                print("AI Bot:", random.choice(responses[key]))
                found = True
                break

        if not found:
            print("AI Bot:", random.choice(responses["default"]))

# Run chatbot
chatbot()