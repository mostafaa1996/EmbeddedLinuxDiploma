import speech_recognition as sr
import pyttsx3
import platform
import os 
import subprocess

# Initialize the recognizer 
recognizer = sr.Recognizer()
# Initialize the text-to-speech engine based on the platform
def init_tts_engine():
    if platform.system() == 'Windows':
        return pyttsx3.init('sapi5')
    elif platform.system() == 'Darwin':  # macOS
        return pyttsx3.init('nsspeechsynth')
    else:
        return pyttsx3.init()  # Assume espeak for other systems

tts_engine = init_tts_engine()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def open_application(app_name):
    try:
        if platform.system() == 'Linux':
            os.system(app_name + " &")
        speak(f"Opening {app_name}.")
    except Exception as e:
        speak(f"Failed to open {app_name}. Error: {str(e)}")

def open_calculator():
    if platform.system() == 'Windows':
        subprocess.Popen('calc.exe')
    elif platform.system() == 'Darwin':  # macOS
        subprocess.Popen(['open', '-a', 'Calculator'])
    else:  # Assume Linux
        try:
            subprocess.Popen(['gnome-calculator'])
        except FileNotFoundError:
            try:
                subprocess.Popen(['kcalc'])
            except FileNotFoundError:
                speak("Calculator application not found.")
                return

def listen(phrase_time_limit = 5):
    with sr.Microphone() as source:
        print("Listening for up to 5 seconds...")
        audio = recognizer.listen(source , phrase_time_limit=phrase_time_limit)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            # speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return None
        
def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "what's your name" in command:
        speak("I am a virtual assistant created by you.")
    elif "exit" in command:
        speak("Goodbye!")
        return False
    elif "open" in command:
        pos = command.index("open")
        appName = command[pos+len("open"):].strip()
        print(appName)
        open_application(app_name=appName)
    else:
        speak("I'm sorry, I don't know how to respond to that.")
    return True

def main():
    speak("Initializing the virtual assistant.")
    running = True
    while running:
        command = listen()
        if command:
            running = process_command(command)

if __name__ == "__main__":
    main()

