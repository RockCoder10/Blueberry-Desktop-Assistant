import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing")
            command = r.recognize_google(audio, language='en-in')
            print(f"User said: {command}\n")

        except Exception as e:
            print(e)
            print("Could you please repeat what you said...")
            return "None"
        return command


if __name__ == '__main__':
    wish()
    
    bad_words = "dumb","stupid","idiot"

    command = takeCommand().lower()

    if 'open youtube' in command:
        webbrowser.open("youtube.com")

    elif 'open tiktok' in command:
        webbrowser.open("tiktok.com")

    elif 'open facebook' in command:
        webbrowser.open("facebook.com")

    elif 'open yahoo' in command:
        webbrowser.open("yahoo.com")

    elif 'wikipedia' in command:
        speak("Searching Wiki")
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        speak("Wikipedia Says")
        print(results)
        speak(results)

    elif 'open gmail' in command:
        webbrowser.open("gmail.com")

    elif 'open outlook' in command:
        webbrowser.open("outlook.com")

    elif 'open office' in command:
        webbrowser.open("office.com")

    elif 'open byjus' in command:
        webbrowser.open("byjus.com")

    elif 'open byjus future school' in command:
        webbrowser.open("byjusfutureschool.com")

    elif 'open snapchat' in command:
        webbrowser.open("snapchat.com")

    elif 'open w3schools' in command:
        webbrowser.open("w3schools.com")

    elif 'open google' in command:
        webbrowser.open("gooogle.com")
    
    elif 'open google slides' in command:
        webbrowser.open("slides.google.com")
    
    elif 'open google docs' in command:
        webbrowser.open("docs.google.com")
    
    elif 'open google sheets' in command:
        webbrowser.open("sheets.google.com")
    
    elif 'open google maps' in command:
        webbrowser.open("maps.google.com")
    
    elif 'open gmail' in command:
        webbrowser.open("gmail.com")
    
    elif 'open twitter' in command:
        webbrowser.open("twitter.com")
    
    elif 'open netflix' in command:
        webbrowser.open("netflix.com")
    
    elif 'open prime video' in command:
        webbrowser.open("primevideo.com")
    
    elif 'open stan' in command:
        webbrowser.open("stan.com")
    
    elif 'open disney plus' in command:
        webbrowser.open("disneyplus.com")
    
    elif 'open google meet' in command:
        webbrowser.open("meet.google.com")
    
    elif 'open google drive' in command:
        webbrowser.open("drive.google.com")
    
    elif 'open google photos' in command:
        webbrowser.open("drive.google.com")
    
    elif 'open google sites' in command:
        webbrowser.open("sites.google.com")
    
    elif 'open google classroom' in command:
        webbrowser.open("classroom.google.com")
    
    elif 'open google play' in command:
        webbrowser.open("play.google.com")
    
    elif 'open google forms' in command:
        webbrowser.open("forms.google.com")
    
    elif 'open onedrive' in command:
        webbrowser.open("onedrive.live.com")
    
    elif 'search google for' in command:
        command = command.replace("search google for", "")
        webbrowser.open("https://www.google.com/search?q=" + command)
    
    elif 'on youtube' in command:
        command = command.replace("on youtube", "")
        webbrowser.open("https://www.youtube.com/results?search_query=" + command)
    

    elif 'hi' in command:
        speak("hi")
    
    elif 'how are you' in command:
        speak("Good. How Are You")
    
    elif 'good night' in command:
        speak("Sweet Dreams")
    
    elif 'tell me a joke' in command:
        joke = "what do you call a boomerang that wonâ€™t come back. A Stick"
        speak(joke)
    
    elif 'good job' in command:
        speak("Thanks")

    elif bad_words in command:
        speak("That's Not Nice")
    
    elif "You don't have many features" in command:
        speak("I am improving day by day as technology gets more advanced. If you have any suggestion for me you can review me at github.com")

    elif 'open whatsapp' in command:
        webbrowser.open("web.whatsapp.com")
    
