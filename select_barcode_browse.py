#!/usr/bin/env python3
from tkinter import * 

from components import * 



select_barcode_browse_help="""Put text here 
"""

class Select_barcode_browse(Frame): 
    def __init__(self , parent ,root): 
        Frame.__init__(self ,parent ,background="white")

        

        # Return button to precedent frame 
        frameReturn=Frame(self ,background="white")
        frameReturn.place_configure(relx=0.01 ,rely=0.05)
        
        self.return_image=PhotoImage(file= Path("Images/")/"return_button80x67.png")
        self.return_button=Button(frameReturn ,image=self.return_image ,borderwidth=0 ,background="white" ,relief="groove")
        self.return_button.pack(side="left")
         
        
        # # Part for the entry of the barcode and its subsquent validation
        frameBarCode=Frame(self ,background="white")
        frameBarCode.place_configure(relx=0.005 ,rely=0.4)

        self.entry=entry_code(frameBarCode)

        # # Part for the interact box 
        frameInteraction=Frame(self ,background="white")
        frameInteraction.place_configure(relx=0.05 ,rely=0.63)

        self.userInteraction=interactBox(frameInteraction ,hei=5)
        self.userInteraction.pack(side="left")
        self.userInteraction.displayMessage("Je suis Bibot \nVeuillez insérer le code à barre " ,"blue")

  
                     
    def menu_bar(self ,root): 
        menuBar=Menu(root)
        
        def displayHelp(): 
            window=Toplevel(root ,background="white")
            window.focus()
            window.resizable(width=False ,height=False)

            details=Text(window ,background="white" ,height=10 ,width=40 ,borderwidth=4 )
            details.pack(side="top")

            details.insert("insert" ,select_barcode_browse_help)
            details["state"]="disabled"

            exitButton=Button(window ,text="Ok" ,borderwidth=2 ,font=("Calibri" , 11) ,width=8 ,command=lambda : window.destroy() ,background="white")
            exitButton.pack(pady=10)

            window.mainloop()

        Help=Menu(menuBar ,tearoff=0)
        Help.add_command(label="How to use..." ,command=displayHelp)
        menuBar.add_cascade(label="Help" ,menu=Help)


        root.config(menu=menuBar)