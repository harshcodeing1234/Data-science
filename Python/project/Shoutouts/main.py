# Write a program to pronnounce list of names using Win32 API. 

import win32com.client


def speak(names):
    for name in names:
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.speak(f"shoutouts to {name}")

speak(["Harsh","Rahul","Shalini","Rajan"]) 

