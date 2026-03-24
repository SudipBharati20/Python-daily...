import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Setup
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return ""

def run_bot():
    speak("Hello! I am your voice assistant. How can I help you?")

    while True:
        command = listen()

        if command == "":
            speak("Please say that again.")
            continue

        # 🔹 Greetings
        if "hello" in command or "hi" in command:
            speak("Hello! How are you?")

        elif "how are you" in command:
            speak("I am fine, thank you!")

        # 🔹 Time & Date
        elif "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {time}")

        elif "date" in command:
            date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today is {date}")

        # 🔹 Open websites
        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        # 🔹 Search Google
        elif "search" in command:
            speak("What should I search?")
            query = listen()
            if query:
                speak(f"Searching for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query}")

        # 🔹 Open apps (Windows)
        elif "open notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")

        elif "open calculator" in command:
            speak("Opening Calculator")
            os.system("calc")

        # 🔹 Exit
        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        # 🔹 Default response
        else:
            speak("I don't know that yet, but I'm learning!")

# Run
run_bot()