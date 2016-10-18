from tkinter import *


root = Tk()



def display(answer1, todisplay):
	
	answer1.grid_forget()
	answer1["text"] = answer1["text"]+todisplay
	answer1.grid(row =0, columnspan = 5, sticky = E)	


def calc(answer):
	answer.grid_forget()
	answer["text"]=str(eval(answer["text"]))
	answer.grid(row =0, columnspan = 5, sticky = E)
	
def deleteall(answer):
	answer.grid_forget()
	answer["text"]=""
	answer.grid(row =0, columnspan = 5, sticky = E)



# *************** MAKING LAYOUT********************



answer = Label(root, text = "")
button_0 = Button(root, text ="0",width =4)
button_1 = Button(root, text ="1",width =4)
button_2 = Button(root, text ="2",width =4)
button_3 = Button(root, text ="3",width =4)
button_4 = Button(root, text ="4",width =4)
button_5 = Button(root, text ="5",width =4)
button_6 = Button(root, text ="6",width =4)
button_7 = Button(root, text ="7",width =4)
button_8 = Button(root, text ="8",width =4)
button_9 = Button(root, text ="9",width =4)
button_dot = Button(root, text =".",width =4)
button_openbracket = Button(root, text ="(",width =2)
button_closebeacket = Button(root, text =")",width =2)
button_equal = Button(root, text ="=", width  =2)
button_divide = Button(root, text ="/",width =2)
button_multiply = Button(root, text ="x",width =2)
button_subtract = Button(root, text ="-",width =2)
button_add = Button(root, text ="+",width =4)
button_deletall = Button(root, text ="CE", width =2)

answer.grid(row =0, columnspan = 5)
button_7.grid(row = 1, column =0)
button_8.grid(row = 1, column =1)
button_9.grid(row = 1, column =2)
button_divide.grid(row = 1, column =3)
button_deletall.grid(row=1, column=4)
button_4.grid(row = 2, column =0)
button_5.grid(row = 2, column =1)
button_6.grid(row = 2, column =2)
button_multiply.grid(row =2, column=3)
button_openbracket.grid(row=2, column=4)
button_1.grid(row = 3, column =0)
button_2.grid(row = 3, column =1)
button_3.grid(row = 3, column =2)
button_subtract.grid(row=3, column=3)
button_closebeacket.grid(row=3, column=4)
button_0.grid(row=4, column=0)
button_dot.grid(row=4, column = 1)
#button_percent.grid(row=4, column = 2)
button_add.grid(row=4, column =2)
button_equal.grid(row=4, column=3)




#********************BINDING BUTTONS***********************




button_0.bind("<Button-1>", lambda x: display(answer,"0"))
button_1.bind("<Button-1>", lambda x: display(answer,"1"))
button_2.bind("<Button-1>", lambda x: display(answer,"2"))
button_3.bind("<Button-1>", lambda x: display(answer,"3"))
button_4.bind("<Button-1>", lambda x: display(answer,"4"))
button_5.bind("<Button-1>", lambda x: display(answer,"5"))
button_6.bind("<Button-1>", lambda x: display(answer,"6"))
button_7.bind("<Button-1>", lambda x: display(answer,"7"))
button_8.bind("<Button-1>", lambda x: display(answer,"8"))
button_9.bind("<Button-1>", lambda x: display(answer,"9"))
button_openbracket.bind("<Button-1>", lambda x: display(answer,"("))
button_dot.bind("<Button-1>", lambda x: display(answer,"."))
button_add.bind("<Button-1>", lambda x: display(answer,"+"))
button_subtract.bind("<Button-1>", lambda x: display(answer,"-"))
button_multiply.bind("<Button-1>", lambda x: display(answer,"*"))
button_closebeacket.bind("<Button-1>", lambda x: display(answer,")"))
button_divide.bind("<Button-1>", lambda x: display(answer,"/"))
button_equal.bind("<Button-1>", lambda x: calc(answer))
button_deletall.bind("<Button-1>", lambda x: deleteall(answer))





root.mainloop()

