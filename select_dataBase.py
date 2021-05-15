#!/usr/bin/env python3
from tkinter import * 
from components import * 





select_dataBase_help="""Put text here
"""

class Select_dataBase(Frame): 
    def __init__(self ,parent ,root): 
        Frame.__init__(self ,parent ,background="white")

        # # Return button to home frame and next frame button
        frameReturn=Frame(self ,background="white")
        frameReturn.place_configure(relx=0.01 ,rely=0.05)
        
        self.return_image=PhotoImage(file= Path("Images/")/"return_button80x67.png")
        self.return_button=Button(frameReturn ,image=self.return_image ,borderwidth=0 ,background="white" ,relief="groove")
        self.return_button.pack(side="left")
         
        frameNext=Frame(self ,background="white")
        frameNext.place_configure(relx=0.855 ,rely=0.05)
         
        self.next_image=PhotoImage(file= Path("Images/")/"next_button80x67.png")
        self.next_button=Button(frameNext ,image=self.next_image ,borderwidth=0 ,background="white" ,relief="groove") 
        self.next_button.pack(side="left")

        # # List of dataBases in the Combobox
        frameListOfDB=Frame(self ,background="white")
        frameListOfDB.place_configure(relx=0.25 ,rely=0.08)
        
        self.listOfDB=listOfProducts(frameListOfDB)  

        self.vDataFile=Button(frameListOfDB ,borderwidth=1 ,font=("Calibri" , 11) ,width=15 ,height=3 ,text="valider" ,background="white" ,foreground="green") 
        self.vDataFile.pack(side="top" ,pady=20)

        # self.vDataFile["command"]=lambda : function()
 


    def menu_bar(self ,root): 
        menuBar=Menu(root )
        
        def displayHelp(): 
            window=Toplevel(root ,background="white")
            window.focus()
            window.resizable(width=False ,height=False)

            details=Text(window ,background="white" ,height=6 ,width=38 ,borderwidth=4 )
            details.pack(side="top")

            details.insert("insert" ,select_dataBase_help)
            details["state"]="disabled"

            exitButton=Button(window ,text="Ok" ,borderwidth=2 ,font=("Calibri" , 11) ,width=8 ,command=lambda : window.destroy() ,background="white")
            exitButton.pack(pady=10)

            window.mainloop()

        Help=Menu(menuBar ,tearoff=0)
        Help.add_command(label="How to use..." ,command=displayHelp)
        menuBar.add_cascade(label="Help" ,menu=Help)


        root.config(menu=menuBar)