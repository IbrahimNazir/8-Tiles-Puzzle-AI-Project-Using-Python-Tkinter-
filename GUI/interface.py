#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, simpledialog
from PIL import ImageTk,Image
import os.path
import main
from accounts import Account


### Global Variables to store the solution analytics ###
algorithm = "A* Manhattan"
initialState = "012345678"
statepointer = cost = counter = depth = 0
runtime = 0.0
path = []





class InterfaceApp:

    # =============================================================================================================== #
    ###     Build the GUI     ###

    def __init__(self, master=None):

        self._job = None

        # signup frame
        self.signup = Frame(master)
        self.signup.configure(height=550, width=800, bg="white")
        # self.signup.pack(side="top")

        # signin frame
        self.signin = Frame(master)
        self.signin.configure(height=550, width=800, bg="white")
        # self.signin.pack(side="top")

        # play learn choice frame
        self.playLearn = Frame(master)
        self.playLearn.configure(height=550, width=800, bg="white")
        # self.playLearn.pack(side="top")

        # learn frame
        self.appFrame = Frame(master)
        self.appFrame.configure(height=550, width=800, bg="white")
        # self.appFrame.pack(side="top")

        # play frame
        self.playFrame = Frame(master)
        self.playFrame.configure(height=550, width=800, bg="white")
        # self.playFrame.pack(side="top")

    def playLearnChoicePage(self):

        self.mainlabel = Label(self.playLearn)
        self.mainlabel.configure(
            anchor="center", font="{Forte} 36 {bold}", foreground="#80461B", justify="center",
            text='Sliding Puzzle\nGame', background="white")

        self.mainlabel.place(anchor="center", x=400, y=60)

        self.playLearn.pack(side="top")
        self.appFrame.forget()
        self.playImage = Image.open("Play.png")
        self.resizedPlayImage = self.playImage.resize((100, 60), Image.LANCZOS)
        self.playImage = ImageTk.PhotoImage(self.resizedPlayImage)
        self.playButton = Button(self.playLearn, image=self.playImage, background="white",command=self.play,
                                 relief="flat", activebackground="white", borderwidth=0)
        self.playButton.place(x=800 // 2 - 50, y=550 // 2 - 100)


        self.learnImage = Image.open("Learn.png")
        self.resizedLearnImage = self.learnImage.resize((95, 60), Image.LANCZOS)
        self.learnImage = ImageTk.PhotoImage(self.resizedLearnImage)
        self.learnButton = Button(self.playLearn, image=self.learnImage, background="white",command=self.learn,
                                  relief="flat", activebackground=
                                  "white", borderwidth=0)
        self.learnButton.place(x=800 // 2 - 45, y=550 // 2 + 40)

    def play(self):
        self.playFrame.pack()
        self.playgame()
        self.appFrame.forget()
        self.playLearn.forget()
        self.signup.forget()
        self.signup.forget()

    def learn(self):
        self.playFrame.forget()
        self.signup.forget()
        self.signup.forget()
        # self.playLearn.forget()
        self.playLearn.forget()
        self.appFrame.pack()
        app.learngame()


        # self.appFrame.forget()
    def signuppage(self):
        self.mainlabel = Label(self.signup)
        self.mainlabel.configure(
            anchor="center", font="{Forte} 36 {bold}", foreground="#80461B", justify="center",
            text='Sliding Puzzle\nPlay', background="white")
        self.mainlabel.place(x=60, y=60)

        self.pic = Image.open(r"slidingpuzzle.png")
        self.pic = self.pic.resize((230, 250), Image.Resampling.LANCZOS)
        self.pic = ImageTk.PhotoImage(self.pic)
        Label(self.signup, image=self.pic, bg="white").place(x=100, y=190)

        Label(self.signup, text="Create Your Account", bg="white", fg="#80461B",
              font=("yu gothic ui", 15, "bold")).place(x=590 - 150, y=200 - 120)
        self.user_first_name_val = StringVar()
        self.user_last_name_val = StringVar()
        self.user_email_signup_val = StringVar()
        self.user_password_signup_val = StringVar()
        Label(self.signup, text="First Name", font=("yu gothic ui", 12, "bold"), fg="#D2B48C", bg="white").place(
            x=570 - 150, y=250 - 120)
        self.user_first_name = Entry(self.signup, width=14, insertbackground="white", font="Helvetica 10",
                                     border=0, bg="white", selectforeground="white", selectbackground="#D2B48C"
                                     ,
                                     foreground="black", textvariable=self.user_first_name_val).place(x=570 + 3 - 150,
                                                                                                      y=280 - 120)
        Label(self.signup, text="Last Name", font=("yu gothic ui", 12, "bold"), fg="#D2B48C", bg="white").place(
            x=700 - 150, y=250 - 120)
        self.user_last_name = Entry(self.signup, width=14, insertbackground="white", font="Helvetica 10",
                                    border=0, bg="white", selectforeground="white", selectbackground="#D2B48C"
                                    ,
                                    foreground="black", textvariable=self.user_last_name_val).place(x=700 + 3 - 150,
                                                                                                    y=280 - 120)
        Label(self.signup, text="Username", font=("yu gothic ui", 12, "bold"), fg="#D2B48C", bg="white").place(
            x=570 - 150, y=300 + 30 - 120)
        self.user_email = Entry(self.signup, width=32, insertbackground="white", font="Helvetica 10", border=0,
                                bg="white", selectforeground="white", selectbackground="#D2B48C"
                                , foreground="black",
                                textvariable=self.user_email_signup_val).place(x=570 + 3 - 150, y=330 + 30 - 120)
        Label(self.signup, text="Password", font=("yu gothic ui", 12, "bold"), fg="#D2B48C", bg="white").place(
            x=570 - 150, y=380 + 30 - 120)
        self.user_password = Entry(self.signup, insertbackground="white", show="*", width=32,
                                   font="Helvetica 10", border=0, bg="white", selectforeground="white",
                                   selectbackground="#D2B48C"
                                   , foreground="black",
                                   textvariable=self.user_password_signup_val).place(x=570 + 3 - 150, y=410 + 30 - 120)
        self.can_area1 = Canvas(self.signup, width=100, height=1.4, bg="#80461B", highlightthickness=0).place(
            x=570 + 3 - 150, y=300 - 120)
        can_area2 = Canvas(self.signup, width=100, height=1.4, bg="#80461B", highlightthickness=0).place(
            x=700 + 3 - 150, y=300 - 120)
        can_area3 = Canvas(self.signup, width=230, height=1.4, bg="#80461B", highlightthickness=0).place(
            x=570 + 3 - 150, y=350 + 30 - 120)
        can_area4 = Canvas(self.signup, width=230, height=1.4, bg="#80461B", highlightthickness=0).place(
            x=570 + 3 - 150, y=430 + 30 - 120)
        self.mainpagecreateaccountpic = Image.open(r"createaccount.png")
        self.mainpagecreateaccountpic = self.mainpagecreateaccountpic.resize((190, 23), Image.Resampling.LANCZOS)
        self.mainpagecreateaccountpic = ImageTk.PhotoImage(self.mainpagecreateaccountpic)
        self.mainpagecreateaccountbutton = Button(self.signup, image=self.mainpagecreateaccountpic,command=self.signupbuttonhandler,
                                                  highlightthickness=0, border=0, background="white",
                                                  activebackground="white").place(
            x=593 - 150, y=490 - 120)
        self.already_have_account = Button(self.signup, text="Already have an account?",
                                           font=("yu gothic ui", 10, "bold"), fg="#D2B48C"
                                           , bg="white", border=0,command=self.signinfunc,
                                           activebackground="white", activeforeground="grey").place(x=607 - 150,
                                                                                                    y=529 - 120)

    def signinpage(self):
        self.mainlabel = Label(self.signin)
        self.mainlabel.configure(
            anchor="center", font="{Forte} 36 {bold}", foreground="#80461B", justify="center",
            text='Sliding Puzzle\nPlay', background="white")
        self.mainlabel.place(x=60, y=60)

        self.pic1 = Image.open(r"slidingpuzzle.png")
        self.pic1 = self.pic1.resize((230, 250), Image.Resampling.LANCZOS)
        self.pic1 = ImageTk.PhotoImage(self.pic1)
        Label(self.signin, image=self.pic1, bg="white").place(x=100, y=190)

        Label(self.signin, text="Sign In", bg="white", fg="#80461B",
              font=("yu gothic ui", 15, "bold")).place(x=500, y=130)

        self.user_email_signin_val = StringVar()
        self.user_password_val = StringVar()

        Label(self.signin, text="Username", font=("yu gothic ui", 12, "bold"), fg="#D2B48C", bg="white").place(
            x=570 - 150, y=300 + 30 - 120)
        self.user_email_login = Entry(self.signin, width=32, insertbackground="white", font="Helvetica 10", border=0,
                                bg="white", selectforeground="white", selectbackground="#D2B48C"
                                , foreground="black",
                                textvariable=self.user_email_signin_val).place(x=570 + 3 - 150, y=330 + 30 - 120)
        Label(self.signin, text="Password", font=("yu gothic ui", 12, "bold"), fg="#D2B48C", bg="white").place(
            x=570 - 150, y=380 + 30 - 120)
        self.user_password_login = Entry(self.signin, insertbackground="white", show="*", width=32,
                                   font="Helvetica 10", border=0, bg="white", selectforeground="white",
                                   selectbackground="#D2B48C"
                                   , foreground="black",
                                   textvariable=self.user_password_val).place(x=570 + 3 - 150, y=410 + 30 - 120)
        can_area3 = Canvas(self.signin, width=230, height=1.4, bg="#80461B", highlightthickness=0).place(
            x=570 + 3 - 150, y=350 + 30 - 120)
        can_area4 = Canvas(self.signin, width=230, height=1.4, bg="#80461B", highlightthickness=0).place(
            x=570 + 3 - 150, y=430 + 30 - 120)
        self.mainpageloginpic = Image.open(r"login.png")
        self.mainpageloginpic = self.mainpageloginpic.resize((120, 23), Image.Resampling.LANCZOS)
        self.mainpageloginpic = ImageTk.PhotoImage(self.mainpageloginpic)
        self.mainpagecreateaccountbutton = Button(self.signin, image=self.mainpageloginpic,
                                                  highlightthickness=0, border=0, background="white",
                                                  activebackground="white",command=self.loginbuttonhandler).place(
            x=480, y=490 - 120)
        self.sign_in = Button(self.signin, text="Create a new account",
                                           font=("yu gothic ui", 10, "bold"), fg="#D2B48C"
                                           , bg="white", border=0, command= self.signupfunc,
                                           activebackground="white", activeforeground="grey").place(x=623 - 150,
                                                                                                    y=529 - 120)
    def signupfunc(self):
        self.signin.forget()
        self.signup.pack()
        self.appFrame.forget()
    def signinfunc(self):
        self.signin.pack()
        self.signup.forget()
        self.appFrame.forget()
        self.signinfunc()



    def loginbuttonhandler(self):
        print(self.user_email_signin_val.get(),self.user_password_val.get())
        print(Account().authenticate(self.user_email_signin_val.get() , self.user_password_val.get()))
        if not Account().authenticate(self.user_email_signin_val.get() , self.user_password_val.get())["error"]:
            self.signin.forget()
            self.signup.forget()
            self.playLearn.pack()
            self.playLearnChoicePage()
        else:
            Label(self.signin,text="*",background="white",foreground="red").place(x=500,y=210)
            Label(self.signin,text="*",background="white",foreground="red").place(x=500,y=290)

    def signupbuttonhandler(self):
        print(self.user_first_name_val.get(),self.user_last_name_val.get(),self.user_email_signup_val.get(),self.user_password_signup_val.get())
        signedup = Account().signUp(self.user_email_signup_val.get(),self.user_password_signup_val.get(),self.user_first_name_val.get() , self.user_last_name_val.get())
        if not signedup["error"]:
            self.signin.forget()
            self.signup.forget()
            self.playLearn.pack()
            self.playLearnChoicePage()
        else:
            print("ye me hu ",signedup)
            Label(self.signup,text=signedup["response"], foreground="red", background="white").place(x=510,y=212)
            print(signedup["response"])

    def shuffle(self):
        global initialState
        initialState = main.shuffle_puzzle(initialState,20)
        self.displayStateOnGridPlay(initialState)




    def playgame(self):
        global initialState

        initialState = "102" \
                       "345" \
                       "678"



        self.mainlabel = Label(self.playFrame)
        self.mainlabel.configure(
            anchor="center", font="{Forte} 36 {bold}", foreground="#80461B", justify="center",
            text='Sliding Puzzle\nPlay', background="white")

        self.mainlabel.place(anchor="center", x=400, y=60)
        # shuffle button
        self.shufflebutton = Button(self.playFrame)
        self.shufflebutton.configure(text="Shuffle", font="{Franklin Gothic Medium} 25 {}",bg="#D2B48C", borderwidth=8,relief="groove", activebackground="#80461B",command=self.shuffle)
        self.shufflebutton.place(anchor="center",x=400,y=500,width=300, height=60)

        # hint button
        self.hintbutton = Button(self.playFrame)
        self.img_hinticon = PhotoImage(file="solve-icon.png")
        self.hintbutton.configure(cursor="hand2", command=self.hint1,text='Hint', image=self.img_hinticon, compound="top", bg="white")
        self.hintbutton.place(anchor="s", height=150, width=150, x=700, y=200)



        # play game cells
        self.pcell0 = Label(self.playFrame)
        self.pcell0.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text=' ')
        self.pcell0.place(anchor="center", height=100, width=100, x=300, y=200)
        self.pcell0.bind("<ButtonPress>", self.onClickShuffle)

        self.pcell1 = Label(self.playFrame)
        self.pcell1.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text='1')
        self.pcell1.place(anchor="center", height=100, width=100, x=400, y=200)
        self.pcell1.bind("<ButtonPress>", self.onClickShuffle)

        self.pcell2 = Label(self.playFrame)
        self.pcell2.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text='2')
        self.pcell2.place(anchor="center", height=100, width=100, x=500, y=200)
        self.pcell2.bind("<ButtonPress>", self.onClickShuffle)

        self.pcell3 = Label(self.playFrame)
        self.pcell3.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text='3')
        self.pcell3.place(anchor="center", height=100, width=100, x=300, y=300)
        self.pcell3.bind("<ButtonPress>", self.onClickShuffle)

        self.pcell4 = Label(self.playFrame)
        self.pcell4.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text='4')
        self.pcell4.place(anchor="center", height=100, width=100, x=400, y=300)
        self.pcell4.bind("<ButtonPress>", self.onClickShuffle)

        self.pcell5 = Label(self.playFrame)
        self.pcell5.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text='5')
        self.pcell5.place(anchor="center", height=100, width=100, x=500, y=300)
        self.pcell5.bind("<ButtonPress>", self.onClickShuffle)

        self.pcell6 = Label(self.playFrame)
        self.pcell6.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text='6')
        self.pcell6.place(anchor="center", height=100, width=100, x=300, y=400)
        self.pcell6.bind("<ButtonPress>", self.onClickShuffle)

        self.pcell7 = Label(self.playFrame)
        self.pcell7.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text='7')
        self.pcell7.place(anchor="center", height=100, width=100, x=400, y=400)
        self.pcell7.bind("<ButtonPress>", self.onClickShuffle)

        self.pcell8 = Label(self.playFrame)
        self.pcell8.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text='8')
        self.pcell8.place(anchor="center", height=100, width=100, x=500, y=400)
        self.pcell8.bind("<ButtonPress>", self.onClickShuffle)


        self.displayStateOnGridPlay(initialState)
        # InterfaceApp.refreshFrame()
        print(initialState)

    def hint1(self):
        app.solve()
        print(path)
        if len(path) > 1:
            indexof0 = main.getStringRepresentation(path[1]).index("0")
            hintindex = main.getStringRepresentation(path[0])[indexof0]
            print(hintindex)

            cells = [self.pcell0, self.pcell1, self.pcell2, self.pcell3, self.pcell4, self.pcell5, self.pcell6,
                     self.pcell7, self.pcell8]
            for i in cells:
                if i.cget("text") == hintindex:
                    i.configure(background="#80461B")






    def onClickShuffle(self,event):
        global initialState
        print("index of 0:",initialState.index("0"))
        children = main.getChildren(initialState)
        print(children)
        print("cell text:",event.widget.cget("text"))

        cells = [self.pcell0, self.pcell1, self.pcell2, self.pcell3, self.pcell4, self.pcell5, self.pcell6, self.pcell7,
                 self.pcell8]
        for i in cells:
            i.configure(background="#D2B48C")

        for state in children:
            print()
            if event.widget.cget("text") != " " and state.index(event.widget.cget("text")) == initialState.index("0"):
                print("shuffle")
                initialState = state
                print(initialState)
                print(state)
                app.displayStateOnGridPlay(initialState)
                if state == "012345678":
                    self.hintbutton.configure(default="disabled")
                    # self.hintbutton.place_forget()
                    Label(self.playFrame,text="You win").place(x=50, y=50)

                break


        # state = main.getStringRepresentation(12345678)
        # app.stepCount.configure(text=app.getStepCountString())
        # app.displaySearchAnalysis()


    def learngame(self):
        self.mainlabel = Label(self.appFrame)
        self.mainlabel.configure(
            anchor="center", font="{Forte} 36 {bold}", foreground="#80461B", justify="center",
            text='Sliding Puzzle\nPlay', background="white")

        self.mainlabel.place(anchor="center", x=300, y=45)
        # previous step button
        self.backbutton = Button(self.appFrame)
        self.img_backicon = PhotoImage(file="back-icon.png")
        self.backbutton.configure(cursor="hand2", image=self.img_backicon, bg="white")
        self.backbutton.place(anchor="center", height=80, width=80, x=250, y=500)
        self.backbutton.bind("<ButtonPress>", self.prevSequence)
        # next step button
        self.nextbutton = Button(self.appFrame)
        self.img_nexticon = PhotoImage(file="next-icon.png")
        self.nextbutton.configure(cursor="hand2", image=self.img_nexticon, bg="white")
        self.nextbutton.place(anchor="center", height=80, width=80, x=350, y=500)
        self.nextbutton.bind("<ButtonPress>", self.nextSequence)
        # fast forward button
        self.fastforwardbutton = Button(self.appFrame)
        self.img_fastforwardicon = PhotoImage(file="fast-forward-icon.png")
        self.fastforwardbutton.configure(cursor="hand2", image=self.img_fastforwardicon, bg="white")
        self.fastforwardbutton.place(anchor="center", height=80, width=80, x=450, y=500)
        self.fastforwardbutton.bind("<ButtonPress>", self.fastForward)
        # fast backward button
        self.fastbackwardbutton = Button(self.appFrame)
        self.img_fastbackwardicon = PhotoImage(file="fast-backward-icon.png")
        self.fastbackwardbutton.configure(cursor="hand2", image=self.img_fastbackwardicon, bg="white")
        self.fastbackwardbutton.place(anchor="center", height=80, width=80, x=150, y=500)
        self.fastbackwardbutton.bind("<ButtonPress>", self.fastBackward)
        # stop button
        self.stopbutton = Button(self.appFrame)
        self.img_stopicon = PhotoImage(file="stop.png")
        self.stopbutton.configure(cursor="hand2", image=self.img_stopicon, state='disabled', bg="white")
        self.stopbutton.place(anchor="center", height=80, width=80, x=550, y=500)
        self.stopbutton.bind("<ButtonPress>", self.stopFastForward)
        # reset button
        self.resetbutton = Button(self.appFrame)
        self.img_reseticon = PhotoImage(file="reset-icon.png")
        self.resetbutton.configure(cursor="hand2", image=self.img_reseticon, state='disabled', bg="white")
        self.resetbutton.place(anchor="center", height=80, width=80, x=50, y=500)
        self.resetbutton.bind("<ButtonPress>", self.resetStepCounter)
        # steps count label
        self.stepCount = Label(self.appFrame)
        self.stepCount.configure(anchor="center", background="white",
                                 font="{@Malgun Gothic Semilight} 12 {}", justify="center", text='0 / 0', bg="white")
        self.stepCount.place(anchor="center", width=200, x=300, y=440)
        # contributors label
        self.contributorsbutton = Button(self.appFrame)
        self.contributorsbutton.configure(cursor="hand2", text='Contributors', bg="white")
        self.contributorsbutton.place(anchor="n", width=150, x=700, y=510)
        self.contributorsbutton.bind("<ButtonPress>", self.showContributors)
        # solve button
        self.solvebutton = Button(self.appFrame)
        self.img_solveicon = PhotoImage(file="solve-icon.png")
        self.solvebutton.configure(cursor="hand2", text='Solve', image=self.img_solveicon, compound="top", bg="white")
        self.solvebutton.place(anchor="s", height=150, width=150, x=700, y=200)
        self.solvebutton.bind("<ButtonPress>", self.solve)
        # loading gif
        self.gif_loading = Label(self.appFrame)
        self.gif_loading.configure(bg="white")
        # dropdown menu
        self.algorithmbox = ttk.Combobox(self.appFrame)
        self.algorithmbox.configure(cursor="hand2", state="readonly", background="white",
                                    values=('BFS', 'DFS', 'A* Manhattan', 'A* Euclidean'))
        self.algorithmbox.place(anchor="center", height=30, width=150, x=700, y=230)
        self.algorithmbox.bind("<<ComboboxSelected>>", self.selectAlgorithm)

        self.algolabel = Label(self.appFrame)
        self.algolabel.configure(anchor="center", text='Search Algorithm:', bg="white")
        self.algolabel.place(anchor="center", x=570, y=230)

        self.analysisbox = Label(self.appFrame)
        self.analysisbox.configure(anchor="center", text='', borderwidth=3, relief="sunken", bg="white")
        self.analysisbox.place(anchor="center", width=150, height=210, x=700, y=400)
        # main cells
        self.cell0 = Label(self.appFrame)
        self.cell0.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text=' ')
        self.cell0.place(anchor="center", height=100, width=100, x=200, y=150)

        self.cell1 = Label(self.appFrame)
        self.cell1.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text='1')
        self.cell1.place(anchor="center", height=100, width=100, x=300, y=150)

        self.cell2 = Label(self.appFrame)
        self.cell2.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text='2')
        self.cell2.place(anchor="center", height=100, width=100, x=400, y=150)

        self.cell3 = Label(self.appFrame)
        self.cell3.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text='3')
        self.cell3.place(anchor="center", height=100, width=100, x=200, y=250)

        self.cell4 = Label(self.appFrame)
        self.cell4.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text='4')
        self.cell4.place(anchor="center", height=100, width=100, x=300, y=250)

        self.cell5 = Label(self.appFrame)
        self.cell5.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text='5')
        self.cell5.place(anchor="center", height=100, width=100, x=400, y=250)

        self.cell6 = Label(self.appFrame)
        self.cell6.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text='6')
        self.cell6.place(anchor="center", height=100, width=100, x=200, y=350)

        self.cell7 = Label(self.appFrame)
        self.cell7.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text='7')
        self.cell7.place(anchor="center", height=100, width=100, x=300, y=350)

        self.cell8 = Label(self.appFrame)
        self.cell8.configure(anchor="center", background="#D2B48C", borderwidth=8,
                             font="{Franklin Gothic Medium} 48 {}", justify="center", relief="groove", text='8')
        self.cell8.place(anchor="center", height=100, width=100, x=400, y=350)
        # Input button
        self.enterstatebutton = Button(self.appFrame)
        self.img_inputicon = PhotoImage(file="input-icon.png")
        self.enterstatebutton.configure(
            cursor="hand2", text='Enter initial state', image=self.img_inputicon, compound="left", bg="white")
        self.enterstatebutton.place(anchor="n", width=150, x=700, y=250)
        self.enterstatebutton.bind("<ButtonPress>", self.enterInitialState)

        self.mainwindow = self.appFrame

        self.gif = [PhotoImage(file='loading.gif', format='gif -index %i' % i) for i in range(10)]


    def run(self):
        """
        Run the program, display the GUI
        """
        app.displayStateOnGrid('012345678')
        app.gif_loading.place_forget()
        InterfaceApp.refreshFrame()
        self.mainwindow.after(0, app.refreshGIF, 0)
        self.mainwindow.mainloop()

    # =============================================================================================================== #
    ###     Widget Methods     ###

    @staticmethod
    def refreshGIF(ind):
        """
        Refreshes the loading gif to show the next frame
        """
        frame = app.gif[ind]
        ind = (ind + 1) % 10
        app.gif_loading.configure(image=frame)
        app.appFrame.after(50, app.refreshGIF, ind)

    def prevSequence(self, event=None):
        """
        Displays the previous state on the grid
        """
        global statepointer
        if statepointer > 0:
            self.stopFastForward()
            statepointer -= 1
            InterfaceApp.refreshFrame()

    def nextSequence(self, event=None):
        """
        Displays the next state on the grid
        """
        global statepointer
        if statepointer < len(path) - 1:
            self.stopFastForward()
            statepointer += 1
            InterfaceApp.refreshFrame()

    def solve(self, event=None):
        """
        Function is invoked at pressing the solve button. Solves the puzzle with the given initialState and algorithm
        then gives a suitable response to the user
        """
        global algorithm, initialState
        app.gif_loading.place(x=600, y=125, anchor="s")
        if InterfaceApp.readyToSolve():
            msg = 'Algorithm: ' + str(algorithm) + '\nInitial State = ' + str(initialState)
            messagebox.showinfo('Confirm', msg)
            self.resetGrid()
            self.solveState()
            if len(path) == 0:
                messagebox.showinfo('Unsolvable!', 'The state you entered is unsolvable')
                self.displaySearchAnalysis(True)
            else:
                InterfaceApp.refreshFrame()
        else:
            solvingerror = 'Cannot solve.\n' \
                           'Algorithm in use: ' + str(algorithm) + '\n' \
                                                                   'Initial State   : ' + str(initialState)
            messagebox.showerror('Cannot Solve', solvingerror)
        app.gif_loading.place_forget()

    def enterInitialState(self, event=None):
        """
        Invoked at pressing enter initial state button. Displays a simple dialog box for the user to enter their
        initial state. The state is validated and a suitable response it displayed to the user
        """
        global initialState, statepointer
        inputState = simpledialog.askstring('Initial State Entry', 'Please enter your initial state')
        if inputState is not None:
            if self.validateState(inputState):
                initialState = inputState
                self.reset()
                app.displayStateOnGrid(initialState)
            else:
                messagebox.showerror('Input Error', 'Invalid initial state')

    def selectAlgorithm(self, event=None):
        """
        Invoked at activating the algorithms combobox. Associates the chosen value to the global variable 'algorithm'
        """
        global algorithm
        try:
            choice = self.algorithmbox.selection_get()
            self.reset()
            algorithm = choice
        except:
            pass

    def fastForward(self, event=None):
        """
        Invoked at pressing fast-forward button. Displays following states in rapid succession until it reaches the
        goal state or until terminated by the stopFastForward() method
        """
        global statepointer
        self.stopFastForward()
        if statepointer < cost:
            app.stopbutton.configure(state='active')
            statepointer += 1
            InterfaceApp.refreshFrame()
            ms = 1000
            if 100 < cost <= 1000:
                ms = 20
            if cost > 1000:
                ms = 1
            app._job = app.stepCount.after(ms, self.fastForward)
        else:
            self.stopFastForward()

    def fastBackward(self, event=None):
        """
        Invoked at pressing fast-backward button. Displays previous states in rapid succession until it reaches the
        goal state or until terminated by the stopFastForward() method
        """
        global statepointer
        self.stopFastForward()
        if statepointer > 0:
            app.stopbutton.configure(state='active')
            statepointer -= 1
            ms = 500
            if cost > 1000:
                ms = 1
            app._job = app.stepCount.after(ms, self.fastBackward)
        else:
            self.stopFastForward()
        InterfaceApp.refreshFrame()

    @staticmethod
    def stopFastForward(event=None):
        """
        Invoked at pressing stop fast-forward/backward button. Stops fast-forward/backward
        """
        if app._job is not None:
            app.stopbutton.configure(state='disabled')
            app.stepCount.after_cancel(app._job)
            app._job = None

    def resetStepCounter(self, event=None):
        """
        Invoked at pressing reset button. Resets the grid to the initial state and the step counter to 0
        """
        global statepointer
        if statepointer > 0:
            self.stopFastForward()
            statepointer = 0
            InterfaceApp.refreshFrame()

    def showContributors(self, event=None):
        """
        Invoked at pressing the contributors button. Displays a message box Containing names and IDs of contributors
        """
        messagebox.showinfo('Contributors', "Cs-21018   -   Mirza Taha Hassan\n"
                                            "Cs-21037   -   Ibrahim Nazir\n"
                                            "Cs-21107   -   Muhammad Abdurrahman\n")

    # =============================================================================================================== #
    ###     Helper Functions     ###

    def displaySearchAnalysis(self, force_display=False):
        """
        Displays the analysis of the search algorithm after execution.
        """
        if InterfaceApp.solved() or force_display is True:
            analytics = 'Analysis of ' + str(algorithm) + \
                        '\ninitial state = ' + str(initialState)
            if force_display:
                analytics += '\n< UNSOLVABLE >'
            analytics += '\n-------------------------------' \
                         '\n' + 'Nodes expanded: \n' + str(counter) + \
                         '\n' + 'Search depth: \n' + str(depth) + \
                         '\n' + 'Search cost: \n' + str(cost) + \
                         '\n' + 'Running Time: \n' + str(runtime) + ' s'
        else:
            analytics = ''
        app.analysisbox.configure(text=analytics)

    def displayStateOnGrid(self, state):
        """
        Display input state to the grid
        :param state: String representation of the required state
        """
        print("display grid")
        if not self.validateState(state):
            state = '012345678'
        self.cell0.configure(text=self.adjustDigit(state[0]))
        self.cell1.configure(text=self.adjustDigit(state[1]))
        self.cell2.configure(text=self.adjustDigit(state[2]))
        self.cell3.configure(text=self.adjustDigit(state[3]))
        self.cell4.configure(text=self.adjustDigit(state[4]))
        self.cell5.configure(text=self.adjustDigit(state[5]))
        self.cell6.configure(text=self.adjustDigit(state[6]))
        self.cell7.configure(text=self.adjustDigit(state[7]))
        self.cell8.configure(text=self.adjustDigit(state[8]))


    def displayStateOnGridPlay(self, state):
        """
        Display input state to the grid
        :param state: String representation of the required state
        """
        print("display grid")
        if not self.validateState(state):
            state = '012345678'
        self.pcell0.configure(text=self.adjustDigit(state[0]))
        self.pcell1.configure(text=self.adjustDigit(state[1]))
        self.pcell2.configure(text=self.adjustDigit(state[2]))
        self.pcell3.configure(text=self.adjustDigit(state[3]))
        self.pcell4.configure(text=self.adjustDigit(state[4]))
        self.pcell5.configure(text=self.adjustDigit(state[5]))
        self.pcell6.configure(text=self.adjustDigit(state[6]))
        self.pcell7.configure(text=self.adjustDigit(state[7]))
        self.pcell8.configure(text=self.adjustDigit(state[8]))

    @staticmethod
    def readyToSolve():
        """
        Checks if current state is ready to be solved by checking if the global variables 'initialState' and
        'algorithm' are not None
        :return: boolean
        """
        return initialState is not None and algorithm is not None

    @staticmethod
    def solved():
        """
        Checks if there is a solution registe#D2B48C in the global variables
        :return: boolean
        """
        return len(path) > 0

    @staticmethod
    def solveState():
        """
        Solves the puzzle with 'initialState' and the chosen 'algorithm'. Assumes the current state is ready to solve.
        """
        global path, cost, counter, depth, runtime
        if str(algorithm) == 'BFS':
            main.BFS(initialState)
            path, cost, counter, depth, runtime = \
                main.bfs_path, main.bfs_cost, main.bfs_counter, main.bfs_depth, main.time_bfs
        elif str(algorithm) == 'DFS':
            main.DFS(initialState)
            path, cost, counter, depth, runtime = \
                main.dfs_path, main.dfs_cost, main.dfs_counter, main.dfs_depth, main.time_dfs
        elif str(algorithm) == 'A* Manhattan':
            main.AStarSearch_manhattan(initialState)
            path, cost, counter, depth, runtime = \
                main.manhattan_path, main.manhattan_cost, main.manhattan_counter, main.manhattan_depth, main.time_manhattan
        elif str(algorithm) == 'A* Euclidean':
            main.AStarSearch_euclid(initialState)
            path, cost, counter, depth, runtime = \
                main.euclid_path, main.euclid_cost, main.euclid_counter, round(main.euclid_depth), main.time_euclid

    def resetGrid(self):
        """
        Resets the grid and step counter to the initial state
        """
        global statepointer
        statepointer = 0
        InterfaceApp.refreshFrame()
        app.stepCount.configure(text=self.getStepCountString())

    def reset(self):
        """
        Resets global variables and the GUI frame. Removes currently registered solution. But the initial state remains the same
        """
        global path, cost, counter, runtime
        cost = counter = 0
        runtime = 0.0
        path = []
        self.resetGrid()
        app.analysisbox.configure(text='')

    @staticmethod
    def getStepCountString():
        """
        Returns string representation of the step count to be displayed on the step-counter
        :return: String
        """
        return str(statepointer) + ' / ' + str(cost)

    @staticmethod
    def refreshFrame():
        """
        Refreshes the frame with all its components: grid, counter, button, etc.
        """
        if cost > 0:
            state = main.getStringRepresentation(path[statepointer])
            app.displayStateOnGrid(state)
            app.stepCount.configure(text=app.getStepCountString())
            app.displaySearchAnalysis()
        if statepointer == 0:
            app.resetbutton.configure(state='disabled')
            app.backbutton.configure(state='disabled')
            app.fastbackwardbutton.configure(state='disabled')
        else:
            app.resetbutton.configure(state='active')
            app.backbutton.configure(state='active')
            app.fastbackwardbutton.configure(state='active')

        if cost == 0 or statepointer == cost:
            app.fastforwardbutton.configure(state='disabled')
            app.nextbutton.configure(state='disabled')
        else:
            app.fastforwardbutton.configure(state='active')
            app.nextbutton.configure(state='active')

    @staticmethod
    def validateState(inputState):
        """
        Validates given state
        :param inputState: String representation of state to be validated
        :return: boolean
        """
        alreadyPresent = []
        # checks whether inputState is numeric and length==9 or not none
        if inputState is None or len(inputState) != 9 or not inputState.isnumeric():
            return False
        # checks whether digits are repeated or not and doesn't contain 9
        for dig in inputState:
            if dig in alreadyPresent or dig == '9':
                return False
            alreadyPresent.append(dig)
        return True

    @staticmethod
    def adjustDigit(dig):
        """
        Converts the zero to an empty cell. Otherwise, returns the digit as it is.
        :param dig: Character of the digit to be adjusted
        :return: string
        """
        if dig == '0':
            return ' '
        return dig


if __name__ == "__main__":
    global app
    root = Tk()
    root.title('Sliding Puzzle')
    root.configure(background="white")
    app = InterfaceApp(root)
    # app.signup.forget()
    # app.signin.forget()
    app.signup.pack()
    app.signinpage()
    app.signuppage()
    # app.playLearnChoicePage()

    app.learngame()
    app.run()



