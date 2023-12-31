import pyttsx3
import speech_recognition
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import pyjokes
import pyautogui

import keyboard
import random
from plyer import notification
import pywhatkit
import requests
from playsound import playsound
from bs4 import BeautifulSoup
from pygame import mixer
from pynput.keyboard import Key, Controller

import smtplib

import subprocess
from tkinter import *


from googletrans import Translator
from gtts import gTTS
import googletrans
import time

from pywikihow import search_wikihow

from time import sleep

keyboard = Controller()  # volume controller


enginge = pyttsx3.init('sapi5')
voices = enginge.getProperty('voices')
# print(voices[0].id)
enginge.setProperty('voice', voices[1].id)


def speak(audio):
    enginge.say(audio)
    enginge.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good Morning!")

    elif hour >= 12 and hour < 18:
        speak("good afternoon!")
    else:
        speak("good evening")

    speak("hiii sir,please tell me how may I helpe you")


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)


def takecommand():
    # it take input form the user and return string output

    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 4)  # take this any problem occurs

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please....")
        return "None"
    return query.lower()


def sendemail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail", "password")
    server.sendmail("Reciveremail", to, content)
    server.close()


def translategl(query):
    speak("sure sir")
    print(googletrans.LANGUAGES)
    translator = Translator()
    speak("Choose the language in which you want to translate")
    b = input("To Lang : ")
    text_to_translate = translator.translate(
        query, src="auto", dest=b,)  # translator.translate
    text = text_to_translate.text
    try:
        speakgl = gTTS(text=text, lang=b, slow=False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")

        time.sleep(5)
        os.remove("voice.mp3")
    except:
        print("Unable to translate")


def Whatsapp():
    speak("Tell me the Name of the Person!")
    name = takecommand()

    if 'md faiz' in name:
        speak("Tell Me The Message!")
        msg = takecommand()
        speak("Tell me the Time sir!")
        speak("Time in Hour!")
        hour = int(takecommand())
        speak("Time in Minutes!")
        min = int(takecommand())
        pywhatkit.sendwhatmsg("+918431557856", msg, hour, min, 20)
        speak("ok sir, Sending Whatsapp Message!")

    else:
        speak("Tell Me The Phone Number!")
        Phone = int(takecommand())
        ph = '+91' + Phone
        speak("Tell me the message!")
        msg = takecommand()
        speak("Tell me the Time sir!")
        speak("Time in Hour!")
        hour = int(takecommand())
        speak("Time in Minutes!")
        min = int(takecommand())
        pywhatkit.sendwhatmsg(ph, msg, hour, min, 20)
        speak("ok sir, Sending Whatsapp Message!")


def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)


def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)


if __name__ == "__main__":
    wishMe()

while True:
    query = takecommand().lower()

    if 'hi' in query:  # remove this any problems comes
        speak("hello sir,how can i help you ")

    elif 'how are you' in query:
        speak("I am fine, what about you sir")

    elif 'fine' in query:
        speak("It's good to know that your fine")

    elif 'hello' in query:
        speak("hello sir, please till how can i help you")
    
    elif 'good morning' in query: 
        speak("good morning sir,please tell me how may I helpe you")

    elif 'good afternoon' in query: 
        speak("good afternoon sir,please tell me how may I helpe you")    
    
    elif 'good evening' in query: 
        speak("good evening sir,please tell me how may I helpe you")
    
    elif 'good night' in query: 
        speak("good night sirkk")    
    
    elif 'stop' in query:
        speak("ok sir!")
        break

    elif 'write a note' in query:
        speak("What should i write, sir")
        note = takecommand()
        file = open('note.txt', 'w')
        speak("Sir, Should i include date and time")
        snfm = takecommand()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)

    elif "show my note" in query:
        speak("showinq notes")
        file = open("note.txt", "r")
        print(file.read())
        speak(file.read(6))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir, the time is {strTime}")

    elif 'the date' in query:
        date()

    elif 'send email' in query:
        try:
            to = "Reciveremail"
            speak("what should i send?")
            content = takecommand()
            sendemail(to, content)
            speak("email has been successfully!")
        except Exception as e:
            print(e)
            speak("sorry I not able to send this email")

    elif 'google search' in query:
        speak("This is what i found for your search sir!")
        query = query.replace("google", "")
        query = query.replace("google search", "")
        pywhatkit.search(query)
        speak("Done sir!")

    elif 'google' in query:
        import wikipedia as googleScrap
        query = query.replace("google", "")
        query = query.replace("google search", "")
        speak("this is what i found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)

        except:
            speak("no speakable output available")

    elif 'youtube' in query:
        speak("This is What I found for your Search!")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.replace("google", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, sir")

    elif 'wikipedia' in query:
        speak("Searching from Wikipedia...")
        query = query.replace("wikipedia", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("google", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia..")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        speak("ok sir,wai a second")
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        speak("ok sir,wai a second")
        webbrowser.open("google.com")

    elif 'open code' in query:
        os.startfile(
            "C:\\Users\\vampi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        speak("ok sir,wai a second")

    elif 'open brave' in query:
        os.startfile(
            "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")
        speak("done sir!")

    elif 'open chrome' in query:
        os.startfile(
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        speak("done sir!")

    elif 'open facebook' in query:
        speak("ok sir!")
        webbrowser.open('https://www.facebook.com/')

    elif 'open instagram' in query:
        speak("ok sir!")
        webbrowser.open('https://www.instagram.com/')

    elif 'open map' in query:
        speak("opening map sir")
        webbrowser.open(
            'https://www.google.com/maps/@12.9662976,77.5880704,12z')

    elif 'close code' in query:
        os.system("taskkill /f /im Code.exe")
        speak("ok sir")

    elif 'close brave' in query:
        os.system("taskkill /f /im brave.exe")
        speak("ok sir")

    elif 'close chrome' in query:
        os.system("taskkill /f /im chrome.exe")
        speak("ok sir")

    elif 'close facebook' in query:
        os.system("taskkill /f /im chrome.exe")
        speak("ok sir")

    elif 'close instagram' in query:
        os.system("taskkill /f /im chrome.exe")
        speak("ok sir")

    elif 'close map' in query:
        os.system("taskkill /f /im chrome.exe")
        speak("ok sir")

    elif 'play music' in query:
        speak("Tell Me The Name of the Song")
        musicname = takecommand()
        if 'brids of Prey' in musicname:
            os.startfile('C:\\Users\\vampi\\Music\\Brids _of_prey.mp3')

        elif 'prefectk' in musicname:
            os.startfile('C:\\Users\\vampi\\Music\\Ed_shareen.mp3')
        elif 'into your arms' in musicname:
            os.startfile(
                'C:\\Users\\vampi\\Music\\Witty_Lowry_-_Into_your_Arms.mp3')
        else:
            pywhatkit.playonyt(musicname)
        speak("your Song has been started!, Enjoy sir!")

    elif 'play songs' in query:
        music_dir = 'C:\\Users\\vampi\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("playing songs from your PC")

    elif 'tired' in query:
        speak("Playing your favourite songs,sir")
        a = (1, 2, 3, 4, 5, 6)
        b = random.choice(a)
        if b == 1:
            webbrowser.open("https://www.youtube.com/watch?v=g6fnFALEseI")
        elif b == 2:
            webbrowser.open("https://www.youtube.com/watch?v=orYf6VDtj_k")
        elif b == 3:
            webbrowser.open("https://www.youtube.com/watch?v=V7LwfY5U5WI")
        elif b == 4:
            webbrowser.open("https://www.youtube.com/watch?v=86h_3HSoEkc")
        elif b == 5:
            webbrowser.open("https://www.youtube.com/watch?v=J7ck984Qhso")
        else:
            webbrowser.open("https://www.youtube.com/watch?v=qoq8B8ThgEM")

    elif 'website' in query:
        speak("ok sir, Launching....")
        query = query.replace("google", "")
        query = query.replace("website", "")
        web1 = query.replace("opem", "")
        web2 = 'https://www.google.com/search?q=' + web1 + '.com'
        webbrowser.open(web2)
        speak("done sir")

    elif 'launch' in query:
        speak("Tell me the name of the website!")
        name = takecommand()
        web = 'https://www.' + name + '.com'
        webbrowser.open(web)
        speak("Done sir")

    elif 'joke' in query:
        get = pyjokes.get_joke()
        speak(get)
        print(get)

    elif 'repeat my words' in query:
        speak("speak sir!")
        jj = takecommand()
        speak(f"You said: {jj}")

    elif 'my location' in query:
        speak("ok sir ,wait a second!")
        webbrowser.open(
            'https://www.google.com/maps/place/East+Point+College+of+Higher+Education/@13.0491856,77.7141417,17z/data=!3m1!4b1!4m6!3m5!1s0x3bae104db6325bff:0x95487852730b0803!8m2!3d13.0491804!4d77.7163304!16s%2Fg%2F11bt_89bbs')

    elif 'temperature' in query:
        search = "temperature in Bangalore"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak(f"current{search} is {temp}")

    elif 'weather' in query:
        search = "temperature in Bangalore"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak(f"current{search} is {temp}")

    elif 'alarm' in query:
        speak("Enter The Time!")
        time = input("Enter the Time:")

        while True:
            Time_Ac = datetime.datetime.now()
            now = Time_Ac.strftime("%H:%M:%S")

            if now == time:
                speak("Time To wake up sir!")
                playsound('Into_Your_Arms.mp3')
                speak("Alarm closed!")

            elif now > time:
                break

    if 'pause' in query:
        keyboard.press('space bar')

    elif 'restart' in query:
        keyboard.press('0')

    elif 'mute' in query:
        keyboard.press('m')

    elif 'skip' in query:
        keyboard.press('l')

    elif 'back' in query:
        keyboard.press('j')

    elif 'full screen' in query:
        keyboard.press('f')

    elif 'film mode' in query:
        keyboard.press('t')

    elif 'pause' in query:
        pyautogui.press("k")
        speak("video pause")

    elif 'play' in query:
        pyautogui.press("k")
        speak("video played")

    elif 'mute' in query:
        pyautogui.press("m")
        speak("video metued")

    elif 'volume up' in query:
        speak("Turning volume up,sir")
        volumeup()

    elif 'volume down' in query:
        speak("Turning volume down,sir")
        volumedown()

    elif 'remember that' in query:
        rememberMessage = query.replace("remember that", "")
        rememberMessage = query.replace("google", "")
        speak("You told me   "+rememberMessage)
        remember = open("Remember.txt", "a")
        remember.write(rememberMessage)
        remember.close()

    elif 'what do you remember' in query:
        remember = open("Remember.txt", "r")
        speak("You told me  " + remember.read())

    elif 'screenshot' in query:
        import pyautogui
        im = pyautogui.screenshot()  # use screenshot
        im.save("ss.jpg")

    elif 'click my photo' in query:
        pyautogui.press("super")
        pyautogui.typewrite("camera")
        pyautogui.press("enter")
        pyautogui.sleep(2)
        speak("SMILE")
        pyautogui.press("enter")

    elif 'schedule my day' in query:
        tasks = []  # Empty list
        speak("Do you want to clear old tasks(Please speak Yes or No)")
        query = takecommand().lower()

        if "yes" in query:
            file = open("tasks.txt", "w")
            file.write(f"")

            file.close()
            no_tasks = int(input("Enter the no. of  tasks:- "))
            i = 0
            for i in range(no_tasks):
                tasks.append(input("Enter the task:-  "))
                file = open("tasks.txt", "a")
                file.write(f"{i}. {tasks[i]}\n")
                file.close()
        elif "no" in query:
            i = 0
            no_tasks = int(input("Enter the no. of  tasks:- "))

            for i in range(no_tasks):
                tasks.append(input("Enter the task:-  "))
                file = open("tasks.txt", "a")
                file.write(f"{i}. {tasks[i]}\n")
                file.close()

    elif 'show my schedule' in query:
        file = open("tasks.txt", "r")
        content = file.read()
        file.close()
        mixer.init()
        mixer.music.load("Football.mp3")
        mixer.music.play()
        notification.notify(
            title="my schedule :- ",
            message=content,
            timeout=15)

    elif 'whatsapp' in query:
        Whatsapp()

    elif 'translate' in query:
        query = query.replace("google", " ")
        query = query.replace("translate", " ")
        translategl(query)

    elif 'how to' in query:
        speak("Getting data from the Internet!")
        op = query.replace("google", " ")
        max_result = 1
        how_to_func = search_wikihow(op, max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        speak(how_to_func[0].summary)

    elif 'log off' in query:
        speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])

    elif 'stop listening' in query:
        speak("listening stop")

    elif 'shutdown system' in query:
        speak("Are You sure you want to shutdown")
        shutdown = input("Do you wish to shutdown your pc? (yes/no)")
        if shutdown == 'yes':
            os.system("shutdown /s /t 1")

        elif shutdown == 'no':
            break

    elif 'restart' in query:
        subprocess.call(["shutdown", "/r"])

    elif ' finally sleep' in query:
        speak("ok sir going to sleep")
        subprocess.call("shutdown / h")

    elif 'thank you' in query:
        speak("Being around you always makes me happy")
