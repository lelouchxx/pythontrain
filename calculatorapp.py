import tkinter
from tkinter import *

root = Tk()
root.title("Calculator")
operation = True
firstnum=0
secondnum =0 


e= Entry(root, width=35, borderwidth = 5)
e.grid(row=0, column = 0, columnspan = 3,padx = 10, pady=10)
sumoperation = False
def onclick(number):
	e.insert(END, number)

def clearbtn():
	e.delete(0,END)

def sumbtn():
	global firstnum 

	firstnum = e.get()
	e.delete(0,END)
def equalbtn():
	global secondnum
	secondnum = e.get()
	e.delete(0,END)
	total = int(firstnum) +int(secondnum)
	e.insert(END, str(total))
	
	


#Define Buttons
b1= Button(root,text = "1",  command= lambda: onclick(1),padx=40, pady =20)
b2= Button(root,text = "2",  command=lambda: onclick(2),padx=40, pady =20)
b3= Button(root,text = "3", command=lambda: onclick(3),padx=40, pady =20)
b4= Button(root,text = "4",  command=lambda: onclick(4),padx=40, pady =20)
b5= Button(root,text = "5",  command=lambda: onclick(5),padx=40, pady =20)
b6= Button(root,text = "6",  command=lambda: onclick(6),padx=40, pady =20)
b7= Button(root,text = "7",  command=lambda: onclick(7),padx=40, pady =20)
b8= Button(root,text = "8", command=lambda: onclick(8),padx=40, pady =20)
b9= Button(root,text = "9", command=lambda: onclick(9),padx=40, pady =20)
b0= Button(root,text = "0", command=lambda: onclick(0),padx=40, pady =20)
addbt = Button(root,text="+", command=sumbtn, padx=80, pady= 20, bg = "YELLOW", activeforeground= "BLUE", activebackground = "RED")
equalbt= Button(root, text="=", command= equalbtn, padx= 40, pady= 20)
clearbt= Button(root, text="clear", command= clearbtn, padx= 80, pady = 20)

#put buttons on the screen
b1.grid(row=3,column=0)

b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=2)
b5.grid(row=2,column=1)
b6.grid(row=2,column=0)
b7.grid(row=1,column=2)
b8.grid(row=1,column=1)
b9.grid(row=1,column=0)
b0.grid(row=4,column=0)
addbt.grid(row= 4, column =1, columnspan= 2)
equalbt.grid(row= 5, column =2, columnspan = 2)
clearbt.grid(row= 5, column=0, columnspan = 2)



root.mainloop()
