from tkinter import *


class About:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x300")
        self.root.maxsize(800, 500)
        self.root.minsize(800, 500)
        self.root.title("About")
        self.setting_icon()
        self.root.config(bg="powder blue")
        self.canva_text()

        self.root.mainloop()

    def setting_icon(self):
        self.root.iconbitmap("copy1.ico")

        # Create a function to show usage of the app

    # Create a canvas and populate the canvas with text and lines...
    # Include a link to my email in the about page....
    # End of the about page...

    def canva_text(self):
        # define all the text as the guidelines for the usage and directions
        text_area = Canvas(self.root, width=800, height=500)
        text_area.create_text(250, 15, text="About 10Xfocus", font=("Arial", 15, "bold", "italic"), fill="black")
        # text_area.create_line(180, 35, 320, 35)
        text_area.create_text(380, 185, font=("tahoma", 10),
                              text=("\n10Xfocus is a pomodoro application which uses the pomodoro technique to "
                                    "improve productivity. Developed in the late 1980s "
                                    "by then-university student Francesco Cirillo, The Pomodoro technique is one of "
                                    "the best productivity technique ever invented. Using the Pomodoro method,"
                                    "you break your workday into 25-minute focus periods"
                                    " followed by five-minute breaks. Each of these focus periods plus a"
                                    " break period is called a Pomodoro. The aim of 10Xfocus is to help"
                                    " the user focus on any task they are working on with laser-"
                                    "like focus avoiding any disturbances.\n"

                                    "\nThe 10Xfocus pomodoro technique has the following steps:\n"

                                    "\n1. Navigate to the settings tab and add the name of your task e.g studying, "
                                    "Android dev, video editing, etc."
                                    "\n2. Decide whether to use the default settings or change the durations i.e, "
                                    "the work duration, the short-break duration, the long-break duration"
                                    "\n3. Start timer and focus on the task for the allocated minutes (default = 25 "
                                    "minutes)"
                                    "  \n4. Take a short-break when the timer rings"
                                    "\n5. After the short-break, Go back to Step 3 and repeat until you complete 4 "
                                    "work sessions(pomodoro)."
                                    "\n6. After 4 pomodoro, take a long break (typically 20 to 30 minutes) instead "
                                    "of a short break. Once the long break is finished, return to step 3."
                                    "\n7. Continue this way until the task is finished. After this, reset the timer "
                                    "for another task."

                                    "\n\n10Xfocus is a product of yumixlabs."
                                    " For bug reporting fixes, visit www.yumixlabs.com or report to "
                                    "the developer's email\n"
                                    "stephennjiu@gmail.com"),
                              width=750,
                              fill="black")

        # text_area.create_text(180, 3800, text="For bug reporting and bug fixes, visit www.yumixlabs.com or report to "
        #                                       "the developer's email\n"
        #                                       "stephennjiu@gmail.com")
        text_area.grid(row=0, column=0)
