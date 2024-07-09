from flask import Flask #, render_template, redirect, request
import warnings
warnings.filterwarnings('ignore')
import pywhatkit
import pyttsx3 #text-to-speech
import speech_recognition as sr #enable microphone
import datetime
import wikipedia
import pyjokes
import psutil
import requests
#import json
#import webbrowser #to open any website
#import os #to access a file


app = Flask("__name__")
engine = pyttsx3.init('sapi5') #sapi5 helps in synthesis and recognition of voice
rate = engine.getProperty('rate')
voices = engine.getProperty('voices') #to get details for current voice
engine.setProperty('voice', voices[0].id) # 0 = male and 1 = female
engine.setProperty('rate', 150)


def speak(audio): #function to convert text 2 speech
    engine.say(audio)
    engine.runAndWait() #speech will not be audible without this command



def wishMe(): #to greet
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Elis. How may I help you")

def greetings(): #closing
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Thank You Sir... Have a great Day")

    elif hour>=12 and hour<20:
        speak("Thank You Sir... Have a great Day")

    else:
        speak("Thank You Sir!! Good Night..!")

def temperature(city):
    api_key = "66edc4e830c1f660519017acdf5020c1"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        temp_in_celcius = current_temperature - 273.15
        return(str(int(temp_in_celcius)))

def takeCommandMic():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  #Using google for voice recognition.
        print(f"You said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"  #none string will be returned
    return query

if _name_ == "__main__":
    wishMe()
    while True:

        query = takeCommandMic().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2) #wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'play' in query:
            song = query.replace("play", "")
            speak('Playing...' + song)
            print("Playing...")
            pywhatkit.playonyt(song)
            break

        elif 'search' in query:
            srch = query.replace("search", "")
            speak("Searching on Google...")
            pywhatkit.search(srch)
            break

        elif 'temperature' in query:
            print('Please tell the name of the city')
            speak('Please tell the name of the city')
            city = takeCommandMic()
            weather_api = temperature(city)
            speak(f"Sir, The temperature in {city} is {weather_api} degree celcius")
            print(weather_api)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'sleep' in query:
            greetings()
            break

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'percentage' in query:
            speak('Your CPU percentage used is printed')
            print(psutil.cpu_percent(1))

        elif 'message' in query:
            try:
                pywhatkit.sendwhatmsg_instantly('+919579368714', "This is message from Elis", 20, False, 5)
                print("Sent....")
                break
            except:
                print("Unexpected Error!..")