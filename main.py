

import os
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyttsx3
import google.generativeai as genai


GOOGLE_API_KEY = "AIzaSyAPnNnqEOprY7Q21efBwJhOu_NpfNmKbog"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-pro")



def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"AI error: {e}")
        return "Sorry, I couldn't get a response from AI."




def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Not understand")
        except sr.RequestError as e:
            print(f"API error (speech): {e}")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
   
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()


if __name__ == "__main__":
    while True:
        data = sptext()
        if data:
            data = data.lower()
            if "stop the program" in data:
                print("Stopping the program immediately!")
                speechtx("Stopping now.")
                break
            elif "exit" in data or "quit" in data:
                print("Exiting. Goodbye!")
                speechtx("Goodbye!")
                break
            elif "your name" in data:
                name = "my name is peter"
                speechtx(name)
            elif "how old are you" in data:
                age = "I am 2 years old"
                speechtx(age)
            elif "time" in data:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speechtx(f"The time is {current_time}")
            elif "youtube" in data:
                webbrowser.open("https://www.youtube.com/")
            elif "joke" in data:
                try:
                    joke = pyjokes.get_joke()
                    speechtx(joke)
                except Exception:
                    jokes = pyjokes.get_jokes(language="en", category="chuck")
                    if jokes:
                        import random
                        speechtx(random.choice(jokes))
                    else:
                        speechtx("Sorry, I couldn't find a joke right now.")
            else:
                print("Sending to Google Gemini...")
                ai_reply = ask_gemini(data)
                print("AI:", ai_reply)
                speechtx(ai_reply)
        else:
            print("Sorry, I did not catch that. Please try again.")
