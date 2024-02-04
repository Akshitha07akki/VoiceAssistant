import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import  pyjokes

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query.lower()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. Please tell me how may I assist you.")

if __name__ == "__main__":
    wishMe()
    while True:
        query = listen()
        if 'time' in query or 'date' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
            speak(f"Here is what I found for {query} on Google.")
        elif 'play' in query:
            query = query.replace("play", "")
            webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={query}")
            speak(f"Here is what I found for {query} on YouTube.")
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
        elif 'stop' in query or 'quit' in query:
            speak("Goodbye! Have a great day.")
            exit()
        else:
            speak("Sorry, I didn't understand that.")