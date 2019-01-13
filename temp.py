from tkinter import *
window = Tk() 
choice =0 
data =0
seprator="*********************************************************************"
window.title("Welcome ARINC Debug Widdow") 
lbl = Label(window, text=seprator,font=("Helvetica", 10)) 
lbl.grid(column=0, row=0)
temp=0
# window.geometry('380x400')

# container = Frame(window, bg = "yellow")
# container.pack(expand = True, fill = "both")
# drawArea = Canvas(container, bg = "red")
# drawArea.pack()
lista=["flat, groove, raised, ridge, solid,  sunken"]
def printlist(name_list):
    mk=25
    # global temp
    # for a in range:
    #     lbl[a].destroy()

    for index,i in enumerate(name_list):
        lbl = Label(window, text=i,font=("Helvetica", 10), bd=10,padx=5,relief="sunken") 
        lbl.grid(column=mk-index, row=6)
    # temp=index

def getlist(option):
    if option == 1:
        name_list=["makarand","suresh","katkar","katkarwadi","satara","aghashjhdfhsdhgdfgbsrbgiurbtbg"]
    else:
        name_list=["cvb","mnb","dfg","sdf","asd"]
    return(name_list)


def print_it (void):
    global choice
    choice=int(variable.get())
    print(choice)

txt = Entry(window,width=20)
 
txt.grid(column=0, row=2)
# txt.focus()

def new_data(): 
    # lbl.configure(text="Button was clicked !!")
    print("entered data is "+ txt.get())
    data=int(txt.get())
    if (data==1):
        mylist=getlist(1)
    elif(data==2):
        mylist=getlist(2)
    else:
        print("protection part of code needs to be implemented if user give invalid data")
    print("mylist:",mylist)
    printlist(mylist)


btn = Button(window, text="Refresh", command=new_data)
btn.grid(column=1, row=2)

# if choice is not :

# if data == 1:
#     name_list=["makarand","suresh","katkar","katkarwadi","satara"]
# else:
#     name_list=["cvb","mnb","dfg","sdf","asd"]


##########################################
# for index,i in enumerate (name_list):
#     chk_state = BooleanVar() 
#     chk_state.set(True) #set check state 
#     chk = Checkbutton(window, text=i, var=chk_state) 
#     chk.grid(column=0, row=index+3)
#     print(chk)
 #########################################
# variable = StringVar(window)
# variable.set(name_list[0]) # default value
# w = OptionMenu(window, variable,*name_list, command=print_it)
# print("choice:", choice)
# w.grid(column=0, row=3)
window.mainloop()