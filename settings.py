from tkinter import *
from tkinter import messagebox


def contains_character(input_string):
    return any(c.isalnum() or not c.isspace() for c in input_string)


class Settings:
    task_name = "Work"
    work = 1
    short_break = 1
    long_break = 1

    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback
        self.settin = Toplevel(parent)
        self.settin.geometry("670x400")

        self.settin.maxsize(670, 400)
        self.settin.config(bg="powder blue")
        self.settin.title("Settings")
        self.setting_icon()
        # Creating the string to hold the variable values
        self.task = StringVar()
        self.work_min = StringVar()
        self.short_breakT = StringVar()
        self.long_breakT = StringVar()

        self.lbltask = Label(self.settin, font=("Arial", 16, "bold"),
                             text="Task Name:", bg="powder blue")

        self.lbltask.grid(row=0, column=0)

        self.entry_task = Entry(self.settin, font=("Arial", 26),
                                textvariable=self.task, bd=4, bg="white")

        self.entry_task.grid(row=0, column=1)

        self.lblwork = Label(self.settin, font=("Arial", 16, "bold"),
                             text="Work Duration:", bg="powder blue")

        self.lblwork.grid(row=1, column=0)

        self.entrywork = Entry(self.settin, font=("Arial", 26, "bold"),
                               textvariable=self.work_min, bd=4, bg="white")

        self.entrywork.grid(row=1, column=1)

        self.lblshort_break = Label(self.settin, font=("Arial", 16, "bold"),
                                    bg="powder blue", text="Short Break Duration:")

        self.lblshort_break.grid(row=2, column=0)

        self.entry_short_break = Entry(self.settin, font=("Arial", 26, "bold"),
                                       textvariable=self.short_breakT, bd=4,
                                       bg="white")

        self.entry_short_break.grid(row=2, column=1)

        self.lbl_long_break = Label(self.settin, font=("Arial", 16, "bold"),
                                    bg="powder blue", text="Long Break Duration:")

        self.lbl_long_break.grid(row=3, column=0)

        self.entry_long_break = Entry(self.settin, font=("Arial", 26, "bold"), textvariable=self.long_breakT, bd=4,
                                      bg="white")
        self.entry_long_break.grid(row=3, column=1)

        space_label = Label(self.settin, text="", font=("Arial", 20, "italic", "bold"), pady=5, bg="powder blue", )
        space_label.grid(row=4, column=0)

        default_button = Button(self.settin, text="Reset to default",
                                bg="powder blue", fg="black",
                                font=("Arial", 10, "bold"),
                                pady=5,
                                command=self.default_values)

        default_button.grid(row=5, column=0)
        apply_settings = Button(self.settin, font=("Arial", 10, "bold"),
                                pady=5, bg="powder blue",
                                text="Apply new settings",
                                command=self.apply_new_settings)
        apply_settings.grid(row=5, column=1)
        self.settin.mainloop()

    def setting_icon(self):
        self.settin.iconbitmap("copy1.ico")

        # Enable end user customizations. Enable task name to be configured, task duration, short break duration,

    # and long_break duration  to be changed dynamically during runtime Pass these values to the self.values in the
    # focus ui Allow a default button at the bottom that will reset these values to their defaults which is 25,5,25,
    # 5,25,5,25,20 Ensure that if any field is not filled, then the default value is used...
    # put an exit button alongside default button

    def default_values(self):
        Settings.task_name = "Work"
        Settings.work = 25
        Settings.short_break = 5
        Settings.long_break = 20
        messagebox.showinfo("durations", f" Task Name: {Settings.task_name}"
                                         f" \n Work duration: {Settings.work} \n "
                                         f"Short Break Duration: {Settings.short_break} "
                                         f"\n Long Break Duration: {Settings.long_break}")

        self.entry_task.delete(0, END)
        self.entrywork.delete(0, END)
        self.entry_short_break.delete(0, END)
        self.entry_long_break.delete(0, END)
        self.exit()

    def apply_new_settings(self):
        try:
            self.work = self.entrywork.get()
            self.work_min.set(self.work)
            self.work = int(self.work)
            if self.work > 360:
                messagebox.showerror("Too long duration", "work duration set to 6hrs+ seem unrealistic!")
                self.work = 25
            else:
                Settings.work = self.work
        except ValueError:
            if self.work == "":
                Settings.work = 25
            else:
                messagebox.showwarning("Wrong inputs", "please enter valid number(s) only for work!")
                Settings.work = 25

        # setting time for short breaks
        try:
            self.short_break = self.entry_short_break.get()
            self.short_breakT.set(self.short_break)
            self.short_break = int(self.short_break)
            if self.short_break > 120:
                messagebox.showerror("Too long duration", "Short break duration set to 2hrs+ seem unrealistic!")
                self.short_break = 5
            else:
                Settings.short_break = self.short_break
        except ValueError:
            if self.short_break == "":
                Settings.short_break = 5
            else:
                messagebox.showwarning("Wrong inputs", "please enter valid number(s) only for short break!")
                Settings.short_break = 5

        # setting time for long breaks.
        try:
            self.long_break = self.entry_long_break.get()
            self.long_breakT.set(self.long_break)
            self.long_break = int(self.long_break)
            if self.long_break > 180:
                messagebox.showerror("Too long duration", "Long break duration set to 3hrs+ seem unrealistic!")
                Settings.long_break = 20
            else:
                Settings.long_break = self.long_break
        except ValueError:
            if self.long_break == "":
                Settings.long_break = 20
            else:
                messagebox.showwarning("Wrong inputs", "please enter valid number(s) only for long break!")
                Settings.long_break = 20

        # setting the task name from work to user specified...
        try:
            self.task_name = self.entry_task.get()
            self.task.set(self.task_name)
            self.task_name = str(self.task_name)
            if contains_character(self.task_name):
                Settings.task_name = self.task_name

            else:
                Settings.task_name = "Work"
        except ValueError:
            Settings.task_name = "Work"
        # End of settings

        messagebox.showinfo("durations", f" Task Name: {Settings.task_name} "
                                         f"\n Work duration: {Settings.work} "
                                         f"\nShort Break Duration: {Settings.short_break} "
                                         f"\n Long Break Duration: {Settings.long_break}")
        self.entry_task.delete(0, END)
        self.entrywork.delete(0, END)
        self.entry_short_break.delete(0, END)
        self.entry_long_break.delete(0, END)
        self.exit()

    def exit(self):
        self.settin.destroy()
        self.callback()
        # print(Settings.task_name)
        # print(Settings.work)
        # print(Settings.short_break)
        # print(Settings.long_break)
