# Write a program to pronnounce list of names using pyttsx3. 


import pyttsx3

def speak(names):
    engine = pyttsx3.init()

    for name in names:
        text = f"shoutouts to {name}"
        engine.say(text)
    
        engine.runAndWait()

speak(["Harsh","Shalini","Tapsi"])