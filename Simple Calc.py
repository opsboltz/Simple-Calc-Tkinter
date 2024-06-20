from tkinter import *

#Main Windows **Has to happen**
root = Tk()

# e for entry
e = Entry(root, width=20, bg="white", fg="black")
e.pack()
#e.get to get the info put in
e.get()


##  BG can also be used for background elemnt

#function/ command for clicking on button
def myClick():
    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()



myButton = Button(root, text="Enter Your Name", padx=120, pady=30, command=myClick, background="white", fg="Black").pack()



root.mainloop()

