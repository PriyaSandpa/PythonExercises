from tkinter import *
import random

names=[]
global questions_answers
asked=[] #asked questions will be stored in this list so questions aren't repeated.
score=0

questions_answers={
    1: ["What's the capital of Australia?", "Sydney", "Canberra", "Vienna", "Canberra", 2],
    2: ["How many countries are in Asia?", "56", "33", "48", "48", 3],
    3: ["Where would you find Rotorua?", "New Zealand", "Cook Islands", "America", "New Zealand", 1],
    4: ["Which one of the main islands (NZ) is the biggest? ", "North Island", "South Island", "Stewart Island", "South Island", 2]
}

def randomiser():
    global qnum
    qnum= random.randint(1,4)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()
        

class Quiz_Starter:
    def __init__(self, parent): #self-indicates that method is part of a class, parent=window 
        background_colour = "OldLace"
        #Frame
        self.quiz_frame = Frame(parent, bg=background_colour, padx=100, pady=100) 
        #self.objectname = widget(widget_platform, background_colour, padding)
        self.quiz_frame.grid() #arrangement of items on the frame
        #Heading
        self.heading_label = Label(self.quiz_frame, text="Basic Geography Quiz", font=("Tw Cen MT", "18", "bold"), bg=background_colour)
        self.heading_label.grid(row=0, padx=20)
        #Label for Username
        self.user_label=Label(self.quiz_frame, text="Enter your username below:", font=("Tw Cen MT", "16"), bg=background_colour)
        self.user_label.grid(row=1, padx=20, pady=20)
        #Entry Box
        self.entry_box= Entry(self.quiz_frame)
        self.entry_box.grid(row=2, padx=20, pady=20)
        #Continue Button
        self.continue_button=Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"),bg="orange",command=self.name_collection)
        self.continue_button.grid(row=3, padx=20, pady=20)

    def name_collection(self):
        name=self.entry_box.get()
        names.append(name)
        self.quiz_frame.destroy()
        Quiz(window)

class Quiz:
    def __init__(self, parent):
        background_colour= "OldLace"
        self.quiz_frame=Frame(parent, bg=background_colour, padx=40, pady=40)
        #self.objectname = widget(widget_platform, background_colour, padding)
        self.quiz_frame.grid() #arrangement of items on the frame
        #question
        self.question_label=Label(self.quiz_frame, text=questions_answers[qnum][0], font=("Tw Cen MT", "16"), bg=background_colour)
        self.question_label.grid(row=1, padx=10, pady=10)
        #Buttons
        self.var1=IntVar() #holds value of radio buttons.
        #Button 1
        self.rb1=Radiobutton(self.quiz_frame, text=questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_colour, value=1, padx=10, pady=10, variable=self.var1, indicator=0, background="light blue")
        self.rb1.grid(row=2, sticky=W)
        #Button 2
        self.rb2=Radiobutton(self.quiz_frame, text=questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_colour, value=2, padx=10, pady=10, variable=self.var1, indicator=0, background="light blue")
        self.rb2.grid(row=3, sticky=W)
        #Button 3
        self.rb3=Radiobutton(self.quiz_frame, text=questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_colour, value=3, padx=10, pady=10, variable=self.var1, indicator=0, background="light blue")
        self.rb3.grid(row=4, sticky=W)
        #Confirm Button
        self.quiz_instance= Button(self.quiz_frame, text="Confirm", font=("Helvetica", "13", "bold"), bg="SpringGreen3", command= self.test_progress)   
        self.quiz_instance.grid(row=7, padx=5, pady=5)
        #Score label
        self.score_label=Label(self.quiz_frame, text="SCORE", font=("Tw Cen MT", "16"), bg=background_colour)
        self.score_label.grid(row=8, padx=10, pady=1)
    
    def questions_setup(self):
        randomiser()
        self.var1.set(0)
        self.question_label.config(text=questions_answers[qnum][0])
        self.rb1.config(text=questions_answers[qnum][1])
        self.rb2.config(text=questions_answers[qnum][2])
        self.rb3.config(text=questions_answers[qnum][3])

    def test_progress(self):
        global score
        scr_label=self.score_label
        choice=self.var1.get()
        if len(asked)>3: #determine if it's last  question.
            if choice==questions_answers[qnum][5]:
                score+=1
                scr_label.config(text=score)
                self.quiz_instance.config(text="Confirm")
            else:
                score+=0
                scr_label.config(text="Incorrect. The correct answer is: " + questions_answers[qnum][4])
                self.quiz_instance.config(text="Confirm")
        else:
            if choice==0:
                self.quiz_instance.config(text="You haven't picked an option. Try again: ")
                choice=self.var1.get()
            else:
                if choice == questions_answers[qnum][5]:
                    scr_label.config(text=score)
                    self.quiz_instance.config(text="Confirm")
                    self.questions_setup()
                else:
                    score+=0
                    scr_label.config(text="The correct answer was: " + questions_answers[qnum][4])
                    self.quiz_instance.config(text="Confirm")
                    self.questions_setup()

randomiser()

if __name__== "__main__": #if the main python file is running
    window=Tk() #window is tk window
    window.title("Geography Quiz") #name of the window
    quiz_instance=Quiz_Starter(window) #making instance of/calling class "Quiz_Starter"
    window.mainloop() #makes sure that window doesnt close until user closes it themselves.
