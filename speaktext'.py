import speech_recognition as sr
import pyttsx3


recog = sr.Recognizer()

with sr.Microphone() as source :
    audio = recog.listen(source)
print(recog.recognize_google(audio))

def SpeechtoText(command):
    engine = pyttsx3.init()
    rate = engine.getproperty('rate')
    engine.setproperty('rate',rate-10)
    engine.say('Says{}'.format(command))
    engine.runAndWait()

print(recog.recognize_google(audio))
