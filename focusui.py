# Import sections
import math
import random
from soundfile import Sound
from tkinter import *
from tkinter import messagebox
from settings import Settings

# Constants defined
TITLE_BG = "#f8c471"
BG = "#d5d8dc"
# aquamarine4
MINSIZE = (700, 600)
MAXSIZE = (900, 650)


# Define functionality...

class UserInterface:
    work_sessions = 0
    reps = 1
    pomodoro = 0
    LONG_BREAK_MIN = Settings.long_break
    SHORT_BREAK_MIN = Settings.short_break
    WORK_MIN = Settings.work
    task_text = Settings.task_name

    def __init__(self, About):

        self.checkmark = None
        self.checks = None
        self.minus = 1
        self.task_handle = None
        self.clicks = 1
        self.button2 = None
        self.timer = None

        self.logo_canvatext = ""
        self.logo_canvas = None
        self.text = "00:00"
        # self.settings_instance = Settings()
        # self.settings_instance.
        self.about = About
        self.window = Tk()
        self.window.maxsize(900, 650)
        self.window.minsize(700, 600)
        self.window.title("10Xfocus")
        self.icon_photo()
        self.window.config(bg=BG)
        self.button_canva()
        self.logo_canva()
        self.setting_canva()
        self.quotes_canva()
        self.timer_canva()

        self.window.mainloop()

    # Setting window
    def settings(self):
        instance = Settings(self.window, self.normalizer)
        # instance.settin.wait_window()

    def reset_value(self):
        UserInterface.LONG_BREAK_MIN = Settings.long_break
        UserInterface.SHORT_BREAK_MIN = Settings.short_break
        UserInterface.WORK_MIN = Settings.work
        UserInterface.task_text = Settings.task_name

    def normalizer(self):
        self.reset_value()
        self.reset_timer()
        self.start()
        self.start_time()

    # About window
    def about(self):
        self.about()

    def icon_photo(self):
        icon = PhotoImage(file="copy1.png")
        self.window.iconphoto(False, icon)

    def logo_canva(self):
        # separator = ttk.Separator(self.window)
        logo_canva = Canvas(self.window, width=900, height=130, bg=TITLE_BG, highlightthickness=2)
        logo_image = PhotoImage(file="copy1.png")
        logo_canva.create_image(275, 60, image=logo_image)
        logo_canva.create_text(500, 50, text="10Xfocus", font=("Arial", 60, "bold"))
        logo_canva.create_text(520, 100, text="Take Your Focus To The Next Level",
                               font=("Tahoma", 15, "bold", "italic"))
        logo_canva.image = logo_image  # To avoid garbage collection
        logo_canva.grid(row=0, column=0)

    def setting_canva(self):
        canvas = Canvas(self.window, width=900, height=70, bg=BG, highlightthickness=2)
        canvas.grid(row=1, column=0)
        # Create a button
        button1 = Button(self.window, text="Settings", borderwidth=4, font=("Arial", 15, "bold"), highlightthickness=0,
                         command=self.settings)
        button2 = Button(self.window, text="About", borderwidth=4, font=("Arial", 15, "bold"), highlightthickness=0,
                         command=self.about)
        # Embed the button inside the canvas
        canvas.create_window(400, 35, window=button1)
        canvas.create_window(500, 35, window=button2)

    def quotes_canva(self):
        with open("data_quotes.txt", "r") as file:
            all_quotes = file.readlines()
        quote = random.choice(all_quotes).rstrip("\n")
        logo_canva = Canvas(self.window, width=900, height=150, bg=BG, highlightthickness=0)
        logo_canva.create_text(450, 70, text=quote,
                               font=("Tahoma", 20, "italic"),
                               width=800
                               )
        logo_canva.grid(row=2, column=0)

    def timer_canva(self):
        self.logo_canvas = Canvas(self.window, width=900, height=100, bg=BG, highlightthickness=0)
        self.task_handle = self.logo_canvas.create_text(450, 15, text=UserInterface.task_text,
                                                        font=("Arial", 20, "italic", "bold"),
                                                        fill="blue")
        self.logo_canvatext = self.logo_canvas.create_text(450, 70, text=self.text,
                                                           font=("Arial", 50, "bold"),

                                                           )
        self.logo_canvas.grid(row=3, column=0)

    def button_canva(self):
        canvas = Canvas(self.window, width=900, height=50, bg=BG, highlightthickness=0)
        canvas.grid(row=4, column=0)
        # Create a button
        button1 = Button(self.window, text="Start", font=("Arial", 15, "bold"),
                         command=lambda: (self.start(), self.start_time()))
        self.button2 = Button(self.window, text="Pause", font=("Arial", 15, "bold"), command=self.pause_timer)
        button3 = Button(self.window, fg="red", text="Reset", font=("Arial", 15, "bold"), command=self.reset_timer)
        # Embed the button inside the canvas
        canvas.create_window(350, 30, window=button1)
        canvas.create_window(450, 30, window=self.button2)
        canvas.create_window(550, 30, window=button3)

    def checkmarks_canva(self):
        # w = 20
        # h = 50

        defined_w = 850
        self.checkmark = Canvas(self.window, width=900, height=300, bg=BG, highlightthickness=0)
        image_pathsn = []
        for i in range(UserInterface.work_sessions):
            image_pathsn.append("small_checkmark.png")

        self.images = []
        w = 15
        h = 20
        for path in image_pathsn:
            if w > defined_w:
                h += 35
                w = 15

            image = path
            photo = PhotoImage(file=image)
            self.images.append(photo)
            self.checkmark.create_image(w, h, anchor=NW, image=photo)
            w += 35

        # label.config(image=photo)
        self.checkmark.create_text(150, 10, text=f"Completed pomodoros: {UserInterface.work_sessions} ",
                                   font=("Arial", 15, "bold"), fill="green")
        self.checkmark.grid(row=5, column=0)
        if UserInterface.work_sessions > 71:
            messagebox.showwarning("Warning", "Unproductive work detected! \n The AI model have detected that you are "
                                              "engaging in unproductive work. \n Kindly restart your "
                                              "work sessions! ")
            self.reset_timer()

    # Define functionality of the start , pause, and reset buttons...
    def pause_timer(self):
        if self.minus == 1:
            self.minus = 0
            self.button2.config(text="Continue", fg="green")
        else:
            self.minus = 1
            self.button2.config(text="Pause", fg="black")

    def start_time(self):
        if self.clicks > 1 and self.window is not None:
            self.window.after_cancel(self.timer)
        #     print("after method called..")
        # print(UserInterface.reps, self.clicks)
        self.button2.config(text="Pause", fg="black")

        FONT_NAME = "Courier"
        FONT_DEF = (FONT_NAME, 20, "bold")

        work_sec = UserInterface.WORK_MIN * 60
        short_break_sec = UserInterface.SHORT_BREAK_MIN * 60
        long_break_sec = UserInterface.LONG_BREAK_MIN * 60

        # self.count_down(work_sec)
        if UserInterface.reps % 8 == 0:
            self.count_down(long_break_sec)
            # UserInterface.task_text = f"{UserInterface.LONG_BREAK_MIN}-Minutes Break"
            self.logo_canvas.itemconfig(self.task_handle, text=f"{UserInterface.LONG_BREAK_MIN}-Minutes Break")

            # title_label.config(text="20-Minutes Break", fg=RED)
        elif UserInterface.reps % 2 == 0:
            self.count_down(short_break_sec)
            # UserInterface.task_text = f"{UserInterface.SHORT_BREAK_MIN}-Minutes Break"
            self.logo_canvas.itemconfig(self.task_handle, text=f"{UserInterface.SHORT_BREAK_MIN}-Minutes Break")

        else:
            self.count_down(work_sec)
            # UserInterface.task_text = UserInterface.task_text
            self.logo_canvas.itemconfig(self.task_handle, text=UserInterface.task_text)
        self.clicks += 1
        UserInterface.reps += 1

    def count_down(self, count):
        # self.timer_canva()
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        if count_min < 10:
            count_min = f"0{count_min}"

        self.text = f"{count_min}:{count_sec}"
        # change the timer_canvas text
        self.logo_canvas.itemconfig(self.logo_canvatext, text=self.text)
        if count > 0:
            # instance timer
            self.timer = self.window.after(1000, self.count_down, count - self.minus)
        else:
            Sound()
            self.start_time()
            UserInterface.pomodoro = math.floor(UserInterface.reps / 2)
            # self.checkmarks_canva()
            # checkmark_img = PhotoImage(file="small_checkmark.png")
            # check_marks = []
            # print(f"The number of reps at this instance is {UserInterface.reps}")
            UserInterface.work_sessions = math.floor((UserInterface.reps - 1) / 2)
            # print(f"The number of work session is {UserInterface.work_sessions}")
            self.checkmarks_canva()

    def reset_timer(self):
        # self.reset_value()
        if self.clicks > 1 and self.window is not None:
            self.window.after_cancel(self.timer)
            UserInterface.reps = 2
        else:
            UserInterface.reps = 1
        self.text = "00:00"
        UserInterface.pomodoro = 0
        self.logo_canvas.itemconfig(self.logo_canvatext, text=self.text)
        self.button2.config(text="Pause", fg="black")
        if self.checkmark is not None:
            self.checkmark.delete("all")

    def start(self):
        self.minus = 1
        if self.clicks > 1:
            UserInterface.reps += -1
