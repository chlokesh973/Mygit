import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import pywhatkit as pwt
import os
import pyjokes

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def wishme():
    """Greet the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning")
        print("Good morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
        print("Good afternoon")
    else:
        speak("Good evening")
        print("Good evening")

def command():
    """Listen to the user's voice command and return it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        speak("Now you can speak")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-us")
            print(f"User said: {query}")
        except Exception as e:
            print("Sorry, I didn't catch that. Please say that again.")
            return "none"
    return query.lower()

# Main program
wishme()
speak("I am Siri. How can I help you?")

while True:
    query = command()
    if "search in google" in query:
        speak("What do you want to search in Google?")
        search_query = command()
        speak("Searching in Google")
        pwt.search(search_query)
    elif "youtube" in query:
        webbrowser.open("https://www.youtube.com")
    elif "open google" in query:
        webbrowser.open("https://www.google.com")
    elif "time" in query:
        the_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"The time is {the_time}")
        speak(f"The time is {the_time}")
    elif "exit" in query:
        speak("Thanks for giving me your time. Goodbye!")
        break
    elif "i love you" in query:
        speak("I love you too!")
    elif "alone" in query:
        speak("Don't feel sad. I am always with you.")
    elif "twitter" in query:
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
    elif "music" in query:
        music_path = "F:\\videos\\song.mp3"  # Update this path to your music file
        if os.path.exists(music_path):
            speak("Playing song")
            os.startfile(music_path)
        else:
            speak("Sorry, I couldn't find the music file.")
    elif "music in online" in query:
        speak("Playing song on YouTube")
        webbrowser.open("https://www.youtube.com/watch?v=YE6LE9cwhXc")
    elif "instagram" in query:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif "joke" in query:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
    elif "power point" in query:
        ppt_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
        if os.path.exists(ppt_path):
            speak("Opening Microsoft PowerPoint")
            os.startfile(ppt_path)
        else:
            speak("PowerPoint is not installed or the path is incorrect.")
    elif "ms word" in query:
        word_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
        if os.path.exists(word_path):
            speak("Opening Microsoft Word")
            os.startfile(word_path)
        else:
            speak("Microsoft Word is not installed or the path is incorrect.")
    elif "ms excel" in query:
        excel_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"
        if os.path.exists(excel_path):
            speak("Opening Microsoft Excel")
            os.startfile(excel_path)
        else:
            speak("Microsoft Excel is not installed or the path is incorrect.")
    else:
        speak("Sorry for the inconvenience. This function is not yet developed.")