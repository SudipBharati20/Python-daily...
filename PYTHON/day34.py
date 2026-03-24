import speech_recognition as sr
import pyttsx3

# Initialize recognizer and speaker
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
        speak("Sorry, I didn't understand.")
        return ""

def run_voice_bot():
    speak("Hello! I am your voice assistant.")
    
    while True:
        command = listen()

        if "hello" in command:
            speak("Hi there!")

        elif "your name" in command:
            speak("I am your Python voice bot.")

        elif "time" in command:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {now}")

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        else:
            speak("Try another command.")

# Run the bot
run_voice_bot()