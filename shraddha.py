import warnings
warnings.filterwarnings('ignore')
import pyttsx3  # text-to-speech

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Good Morning!")

wishMe()