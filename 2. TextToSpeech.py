import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.say("Hey I am Anwarul haque Learning Python For You")
engine.runAndWait()


engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()
