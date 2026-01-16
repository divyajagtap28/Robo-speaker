import os
import pyttsx3
import datetime
import random

from comtypes.tools.tlbparser import void_type


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate",150)
    engine.setProperty("volume",1)
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    engine.say(text)
    engine.runAndWait()
    del engine

jokes = [
            "Why did the computer go to the doctor? Because it caught a virus!",
            "Why was the math book sad? Because it had too many problems.",
            "Why did the robot go on vacation? It needed to recharge its batteries.",
            "Why did the programmer quit his job? Because he didn't get arrays.",
        ]


if __name__ == '__main__':
    print("welcome to ROBOSPEAKER,created by DIVYA")
    while True:
        x=input("enter what you want to say : ")
        if x.lower()=="quit":
            engine = pyttsx3.init()
            engine.say("goodbye")
            engine.runAndWait()
            del engine
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()
        del engine

        if "time" in x.lower():
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
        elif "date" in x.lower():
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")
        elif "joke" in x.lower():
            joke = random.choice(jokes)
            speak(joke)
        else:
            speak(x)

        with open("log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {x}\n")






