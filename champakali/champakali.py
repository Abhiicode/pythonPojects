import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voices[1].id)

# Selecting  female(Zira) voice
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<4:
        speak("Good night shubh ratri")
    elif hour>=4 and hour<12:
        speak("Radhe Radhe Good morning")
    elif hour>=12 and hour<16:
        speak("Good afternoon have a nice day")
    elif hour>=16 and hour<21:
        speak("Good evening Dear")
    elif hour>=21 and hour<=23:
        speak("Good night")
    else:
        speak("Good night")
    
    speak("I am Champakali, Pleasse tell me how can I help you")

def takeCommand():
    ''' Will listen and return string'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold=1
        # r.energy_threshold=300
        r.adjust_for_ambient_noise(source,duration=0.8)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,key=None,language="en-US")
        #print(f"user said : {query}\n")
    except Exception as e:
        print(e)
        return "Sorry unable to recognize, Please say again"
    
    return query

if __name__ =="__main__":
    wishMe()
    run = True
    while(run):
        query = takeCommand().lower()
        print(query)

        if 'wikipedia' in query:
            speak("Searching wikipedia ...")
            query = query.replace('wikipedia',"")
            result = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia,")
            print(result)
            speak(result)
        elif 'exit' in query or 'quit' in query:
            speak("Thankyou, have a great time ahead. Bye!")
            run = False

        elif 'youtube' in query:
            query = query.replace('youtube',"")
            speak("Searching "+query+"on youtube")
            webbrowser.open("https://www.youtube.com/results?search_query="+query)
        elif 'google' in query:
            speak("Opening google in browser")
            webbrowser.open("www.google.com")
        elif 'say' in query or 'se' in query or 'a' in query:
            query = query.replace('say',"")
            query = query.replace('se',"")
            speak(query)
    
    # speak("Naageendra and abhii are codders")