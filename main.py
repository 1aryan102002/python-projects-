import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import music
import requests
from openai import OpenAI

import os

# Initialize TTS engine
ttsx = pyttsx3.init()
voices = ttsx.getProperty('voices')
if len(voices) > 1:
    ttsx.setProperty('voice', voices[1].id)
else:
    ttsx.setProperty('voice', voices[0].id)
ttsx.setProperty('rate', 145)
ttsx.setProperty('volume', 1.0)

def spech(text):
    ttsx.say(text)
    ttsx.runAndWait()

NEWS_API_KEY = "YOUR_NEWS_API_KEY"
openai_api_key = "YOUR_OPENAI_API_KEY"

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        articles = response.json().get('articles', [])
        if not articles:
            spech("Sorry, I couldn't find any news.")
            return
        spech("Here are the top 5 news headlines:")
        for i, article in enumerate(articles[:5]):
            spech(f"Headline {i+1}: {article['title']}")
    except Exception as e:
        spech("Sorry, there was a problem fetching the news.")
        print("News error:", e)
        
def run_application(app_path):
    try:
        if os.path.exists(app_path):
            os.startfile(app_path)  # Windows only
            spech(f"Running application at {app_path}")
        else:
            spech("Sorry, I couldn't find that application.")
    except Exception as e:
        spech("There was an error running the application.")
        print(f"App error: {e}")

def aifriend(command):
    try:
        client = OpenAI(openai_api_key=openai_api_key)
        completion = client.chat.completions.create(
            model="chatgpt-4o-latest",
            messages=[
                {"role": "system", "content": "you are a virtual assistant named laila skilled in all the tasks like chat gpt. give short responses"},
                {"role": "user", "content": command}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        spech("Sorry, there was a problem with AI chat.")
        print("AI error:", e)
        return "I'm unable to answer right now."

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        wb.open("https://www.google.com/")
    elif c.startswith("run"):
        try:
            app_path = c.split(" ", 1)[1]
            run_application(app_path)
        except IndexError:
            spech("Please say the application path after 'run'.")
    elif "open yt" in c:
        wb.open("https://www.youtube.com/")
    elif "open gpt" in c:
        wb.open("https://chatgpt.com/")
    elif "open linkedin" in c:
        wb.open("https://www.linkedin.com/feed/")
    elif "open list" in c:
        wb.open("https://www.instagram.com/")
    elif c.startswith("play"):
        try:
            song = c.split(" ", 1)[1]
            link = music.music.get(song)
            if link:
                wb.open(link)
                spech(f"Playing {song}")
            else:
                spech("Sorry, I don't have that song.")
        except IndexError:
            spech("Please say the song name after 'play'.")
    elif "news" in c:
        get_news()
    elif "shutdown" in c:
        spech("Goodbye sir, signing off.")
        exit()
    else:
        spech(aifriend(c))

if __name__ == "__main__":
    spech("Initializing Lylla...")
    r = sr.Recognizer()
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=5, phrase_time_limit=2)
                commandword = r.recognize_google(audio)
                print(commandword)
            if commandword.lower() == "laila":
                spech("Hello sir")
                with sr.Microphone() as source:
                    print("Lylla is active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except sr.UnknownValueError:
            spech("Waiting for wake word...")
        except Exception as e:
            spech("Sorry, there was an error.")
            print(f"Lylla error: {e}")