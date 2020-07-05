from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

# Create chatbot objects
cbot = ChatBot("Demini")

# Create training list
dialog = [
    'Hi',
    'Hi there!',
    'Hello',
    'Hello there!',
    'How are you?',
    'I am fine! Thank you',
    'What is your name?',
    'I am Demini',
    'Who are you?',
    'I am a chat bot',
    'What are you doing?',
    'I am helping elder citizens to figure out their daily problems',
    'What is your task?',
    'I am helping elder citizens to figure out their daily problems',
    'Who created you?',
    'I am created by Dinesh',
    'Who build you?',
    'Dinesh build me',
    'Where do you live?',
    'In your computer',
    'Where are you from?',
    'I am from your computer',
    'What is your speaking language?',
    'I mostly speak in english. But I can speak sinhala little bit',
    'How old are you?',
    'I have no idea about my age',
    'What is going on?',
    'I am enjoying my time',
    'Whats up?'
    'Great'
]

# Assign Bot to trainer
trainer = ListTrainer(cbot)

# Train the bot with the help of list trainer
trainer.train(dialog)

# ---Uncomment this to see the terminal process---
# response = cbot.get_response("what is your age")
# print(response)

# print("Talk to the Chat bot.")
# while True:
#     q = input("You : ")
#     if q == 'exit':
#         break
#     response = cbot.get_response(q)
#     print("Bot : ", response)

# Create GUI interface
# Main Window
main = Tk()
main.geometry("750x950")
main.configure(bg = "silver")
main.title("Chat Bot for Help Elder Citizens")

# Icon Photo
img = PhotoImage(file = "./img/ch.png")
picL = Label(main,image = img, bg = "silver")
picL.pack(pady = 5)

# Getting Response from the Bot by Passing User input
def ask_from_bot():
    q = txtField.get()
    response = cbot.get_response(q)
    msgs2.insert(END, "You : " + q)
    msgs1.insert(END, "Bot : " + str(response))
    txtField.delete(0, END)

# Creating Bot Message Area
# Bot Lable
lbl1 = Label(main, text = "Bot :", font = "Arial 18", width = 49, height = 1, anchor = W, bg = "silver")
lbl1.pack(pady = 10)
# List box for Bot's chats
frame1 = Frame(main)
sc1 = Scrollbar(frame1)
msgs1 = Listbox(frame1, width = 60, height = 10, bg = "ivory", font = "Arial 15")
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
msgs2 = Listbox(frame2, width = 60, height = 10, bg = "wheat", font = "Arial 15")
sc2.pack(side = RIGHT, fill = Y)
msgs2.pack(side = LEFT, fill = BOTH, pady = 10)
frame2.pack()

# Creating a Message Text Field
txtField = Entry(main, width = 50, font = "Arial 18", bg = "yellow")
txtField.pack(padx = 60, pady = 30)

# Creating a Send Button
btn = Button(main, text = "Ask from the Bot", font = "Arial 15", width = 20, bg = "salmon", command = ask_from_bot)
btn.pack()

main.mainloop()
