#Basic setup code for tkinter
from tkinter import *
window = Tk()
window.title("Movie Finder")
window.geometry("800x600")

#Main UI Code
titleLabel = Label(window, text="Welcome to MovieFinder").pack()
blank1 = Label(window, text="").pack()
blank2 = Label(window, text="").pack()

parametersLabel = Label(window, text="Enter Your Parameters Below").pack()
blank3 = Label(window, text="").pack()

timeLabel = Label(window, text="Enter Your Desired Movie Showtime:").pack()
timeSpinbox1 = Spinbox(window, from_=1, to=12).pack()
timeSpinbox2 = Spinbox(window, values=(":00", ":15", ":30", ":45")).pack()
timeSpinboxAMPM = Spinbox(window, values=("AM", "PM")).pack()
blank4 = Label(window, text="").pack()

movieLabel = Label(window, text="Specify the Movie You Would Like to See").pack()
movieSpinbox = Spinbox(window, values=("N/A For Now")).pack()
blank5 = Label(window, text="").pack()




mainloop()
