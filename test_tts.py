import pyttsx3

engine = pyttsx3.init()
engine.say("This is a test of text to speech.")
engine.runAndWait()
print("If you hear this message spoken, TTS is working!")
