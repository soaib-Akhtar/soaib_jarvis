import speech_recognition as sr
import os
import win32com.client
import webbrowser
import openai
from config import apikey
import datetime
import re
import subprocess
import random
import numpy as np


chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Soaib: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Example usage:
say("Hello, Soaib .")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"],
                 ["chat GPT", "https://chat.openai.com/"],
                 ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"],
                 ["video maker", "https://pictory.ai/"],
                 ["presentation generator", "https://tome.app/futureai-620"],
                 ["Amazon", "https://www.amazon.com/"],
                 ["Amazon", "https://www.amazon.com/"],
                 ["whatsapp", "https://web.whatsapp.com/"],
                 ["Facebook", "https://www.facebook.com/"],
                 ["Instagram", "https://www.instagram.com/"],
                 ["Flipkart", "https://www.flipkart.com/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: Add a feature to play a specific song

        if "open music" in query.lower():
            musics = [["music 1", r"C:\\Users\\soaib\\Music\\music 1.mp3"],
                      ["music 2", r"C:\\Users\\soaib\\Music\\music 2.mp3"],
                      ["music 3", r"C:\\Users\\soaib\\Music\\music 3.mp3"],
                      ["music 4", r"C:\\Users\\soaib\\Music\\music 4.mp3"]]

            # Extract the music name from the user's query using regular expressions
            match = re.search(r"Open (music \d)", query, re.IGNORECASE)
            if match:
                requested_music = match.group(1).lower()

                for music in musics:
                    if music[0].lower() == requested_music:
                        say(f"Opening {music[0]} sir...")
                        subprocess.run(["start", "wmplayer", music[1]], shell=True)
                        break
                else:
                    say("Requested music not found.")
            else:
                say("Please specify the music you want to open.")

        elif "the time" in query:
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")
            print(hour, ":", min)


        elif "open vs code" in query:
            vscode_path = r"C:\Users\soaib\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            say(f"Opening vs code sir")
            subprocess.run([vscode_path], shell=True)

        elif "Notepad" in query:
            notepad_path = r"C:\Program Files\Notepad++\notepad++.exe"
            say(f"Opening notepad sir")
            subprocess.run([notepad_path], shell=True)

        elif "mansi kaise ho".lower() in query.lower():
            say(f"i am fine and you")
        elif "i am also fine".lower() in query.lower():
            say(f"i love you soaib")

        elif "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")

        elif "open pass".lower() in query.lower():
            os.system(f"open /Applications/Passky.app")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)





        # say(query)