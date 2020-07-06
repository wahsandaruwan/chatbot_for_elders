from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as sr
from googletrans import Translator

# --Training & Initializing the Bot--
# Creating a Chatbot Object
cbot = ChatBot('Demini')
# Read Text file
conv = open('data.txt', 'r').readlines()
# Set the trainer
trainer = ListTrainer(cbot)
# Train the bot
trainer.train(conv)

# --For text to speech--
# For Male Voice For Bot
engine = pp.init()
voices = engine.getProperty('voices')
# To Speak Bot
def speak(text):
    # Request
    engine.setProperty('voice', voices[0].id)
    engine.say(text[0])
    engine.runAndWait()
    # Response
    engine.setProperty('voice', voices[1].id)
    engine.say(text[1])
    engine.runAndWait()
    
# --For Speech Recognition--
# Create recognizer object
recog = sr.Recognizer()
# Recognize
def voiceRecognize(lan):
    # Use microphone to get the voice
    with sr.Microphone() as source:
        print("Say Something : ")
        audio = recog.listen(source)
        print("Done!")
    if lan == "en-US":
        # Define the speaking language
        txts = recog.recognize_google(audio, language = lan)
        # Update message boxes
        updateMsgBoxes(txts,0)
    else:
        # Define the speaking language
        txts = recog.recognize_google(audio, language = lan)
        # Transale English
        txte = translatorEn(txts)
        # Update message boxes
        updateMsgBoxes(txte,txts)

# --For language Translation--
# Translator object
trans = Translator()
# Translator English
def translatorEn(text):
    # Translate sinhala to sinhala
    trans_sentence = trans.translate(text, src = 'si', dest = 'en')
    tr = trans_sentence.text
    updateMsgBoxes(tr,text)

# Translator Sinhala
def translatorSi(text):
    # Translate sinhala to sinhala
    trans_sentence = trans.translate(text, src = 'en', dest = 'si')
    tr = trans_sentence.text
    return tr

# --Common Functions--
# Update Message Boxes of Both User and Bot
def updateMsgBoxes(q,r):
    response = cbot.get_response(q)
    if r == 0:
        msgs2.insert(END, "You : " + q)
        msgs1.insert(END, "Bot : " + str(response))
        # Speech
        lst = [q,response]
        speak(lst)  
    else:
        msgs2.insert(END, "You : " + r)
        msgs1.insert(END, "Bot : " + translatorSi(str(response)))

    txtField.delete(0, END)
    msgs1.yview(END)
    msgs2.yview(END)

# Intermediate function that handles functionalities
def ask_from_bot():
    if clickedl.get() == "English":
        if clickedt.get() == "Text":
            q = txtField.get()
            updateMsgBoxes(q,0)
        else:
            voiceRecognize("en-US")
    else:
        if clickedt.get() == "Text":
            q = txtField.get()
            translatorEn(q)
        else:
            voiceRecognize("si-LK")

# Pressing 'enter' key to ask from bot
def enter_key(event):
    btn.invoke()

# --GUI Interface--
# Creating Main Window
main = Tk()
main.geometry("750x940")
main.configure(bg = "silver")
main.title("Chat Bot for Help Elder Citizens")

# Icon Photo
img = PhotoImage(file = "./img/ch.png")
picL = Label(main,image = img, bg = "silver")
picL.pack(pady = 5)

# Creating Bot Message Area
# Bot Lable
lbl1 = Label(main, text = "Bot :", font = "Arial 18", width = 49, height = 1, anchor = W, bg = "silver")
lbl1.pack(pady = 10)
# List box for Bot's chats
frame1 = Frame(main)
sc1 = Scrollbar(frame1)
msgs1 = Listbox(frame1, width = 60, height = 8, bg = "ivory", font = "Arial 15", yscrollcommand = sc1.set, xscrollcommand = sc1.set)
sc1.pack(side = RIGHT, fill = Y)
msgs1.pack(side = LEFT, fill = BOTH, pady = 10)
frame1.pack()

# Creating User Message Area
# User Lable
lbl2 = Label(main, text = "You :", font = "Arial 18", width = 49, height = 1, anchor = W, bg = "silver")
lbl2.pack(pady = 10)
# List box for User's chats
frame2 = Frame(main)
sc2 = Scrollbar(frame2)
msgs2 = Listbox(frame2, width = 60, height = 8, bg = "wheat", font = "Arial 15", yscrollcommand = sc2.set)
sc2.pack(side = RIGHT, fill = Y)
msgs2.pack(side = LEFT, fill = BOTH, pady = 10)
frame2.pack()

# Creating a Message Text Field
txtField = Entry(main, width = 50, font = "Arial 18", bg = "yellow")
txtField.pack(padx = 60, pady = 20)

# Creating a Dropdown Menu to Select languages
clickedl = StringVar()
clickedl.set("English")
dropl = OptionMenu(main, clickedl, "English", "සිංහල")
dropl.config(width=20)
dropl.pack(pady = 10)

# Creating a Dropdown Menu to Input Type
clickedt = StringVar()
clickedt.set("Text")
dropt = OptionMenu(main, clickedt, "Text", "Voice")
dropt.config(width=20)
dropt.pack(pady = 10)

# Creating a Send Button
btn = Button(main, text = "Ask From the Bot", font = "Arial 15", width = 20, bg = "salmon", command = ask_from_bot)
btn.pack()

# Binding the main window with 'enter' key
main.bind('<Return>', enter_key)

main.mainloop()
