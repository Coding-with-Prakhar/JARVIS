import speech_recognition as sr
import pyaudio
import pyttsx3 
import webbrowser
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
apikey = "63edc4526e894feaac8548ea8170d93e"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://x.com")
    elif "open x" in c.lower():
        webbrowser.open("https://x.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    # For listening music: 
    elif c.lower().startswith("play"):
        song = c.lower().split(" ",1)[1] 
        link = musicLibrary.music[song]
        webbrowser.open(link)
    # For getting news: 
    elif "news" in c.lower():
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apikey}")
        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])

            print("\nTop Headlines:\n")
        for article in articles: 
             speak(article['title'])
        else:
            print("Error fetching news:", response.json())
    
    
if __name__ == "__main__":
    speak("Initialising JARVIS..")
    while True:

    # For the bot to wake up with the word "JARVIS"
    # Obtaining the audio from microphone:

        r = sr.Recognizer()
        print("Recognizing the command for activating..")

        try:
            with sr.Microphone() as source: 
                print("Listening..")
                audio = r.listen(source, timeout = 2.5, phrase_time_limit = 1)
            word = r.recognize_google(audio)
            # print(word)
            if(word.lower() == "jarvis"):
                speak(" YES, what do you want ?")
                with sr.Microphone() as source:
                    print("JARVIS Activated..")
                    audio = r.listen(source)
                command = r.recognize_google(audio)
                # print(command) 

                processCommand(command)


        except Exception as e:
            print(f"ERROR during execution.\n{e}")
