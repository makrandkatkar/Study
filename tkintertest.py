from tkinter import *
def show(data_list):
    data_list=data_list[0:4]
    root = Tk()
    frame=Frame(root)
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)
    frame.grid(row=0, column=0, sticky=N+S+E+W)
    grid=Frame(frame)
    grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
    Grid.rowconfigure(frame, 7, weight=1)
    Grid.columnconfigure(frame, 0, weight=1)
    btn = Button(frame,text ="data",wraplength=100)
    btn.grid(column=0, row=0, sticky=N+S+E+W)
    mk=0
    nextbutton=0
    for i in data_list:

        print("i:",i)
        if mk == 3:
            nextbutton=nextbutton+1
            mk=0
        if mk == 0:
            btn = Button(frame,text =i,wraplength=100)
            btn.grid(column=nextbutton, row=mk+1, sticky=N+S+E+W)
        mk =mk+1
    # for x in range(10):
    #   Grid.columnconfigure(frame, x, weight=1)

    # for y in range(5):
    #   Grid.rowconfigure(frame, y, weight=1)
    root.mainloop()