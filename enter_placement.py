#!/usr/bin/env python3
from tkinter import * 
from components import *


enter_placement_help="""Put text here 
"""



class Enter_placement(Frame): 
    def __init__(self ,parent ,root):
        Frame.__init__(self ,parent ,background="white")

        # Return button to precedent frame and next frame button
        frameReturn=Frame(self ,background="white")
        frameReturn.place_configure(relx=0.01 ,rely=0.01)
        
        self.return_image=PhotoImage(file= Path("Images/")/"return_button80x67.png")
        self.return_button=Button(frameReturn ,image=self.return_image ,borderwidth=0 ,background="white" ,relief="groove")
        self.return_button.pack(side="left")
         
        frameNext=Frame(self ,background="white")
        frameNext.place_configure(relx=0.855 ,rely=0.01)
         
        self.next_image=PhotoImage(file= Path("Images/")/"next_button80x67.png")
        self.next_button=Button(frameNext ,image=self.next_image ,borderwidth=0 ,background="white" ,relief="groove") 
        self.next_button.pack(side="left")

        # # Part for the entry of the placement of the component 
        placementFrame=Frame(self ,background="white")
        placementFrame.place_configure(relx=0.005 ,rely=0.4)

        self.placementEntry=entry_chariot(placementFrame)

        frameButtons=Frame(self ,background="white")
        frameButtons.place_configure(relx=0.25 ,rely=0.8)

        self.vEmplacement=Button(frameButtons ,borderwidth=1 ,font=("Calibri" , 11) ,height=2 ,width=10 ,text="valider" ,background="white" ,foreground="green" )
        self.vEmplacement.pack(side="left" ,padx=20)

        dEmplacement=Button(frameButtons ,borderwidth=1 ,font=("Calibri" , 11) ,height=2 ,width=10 ,text="supprimer" ,background="white" ,foreground="red" )
        dEmplacement.pack(side="left" ,padx=20)

        # # Part for the interact box 
        frameInteraction=Frame(self ,background="white")
        frameInteraction.place_configure(relx=0.57 ,rely=0.28)

        self.userInteraction=interactBox(frameInteraction ,wid=28 ,hei=7)
        self.userInteraction.pack(side="left")
        self.userInteraction.displayMessage("Je suis Bibot \nVeuillez insérer l'emplacement du composant" ,"blue")


  
    def menu_bar(self ,root): 
        menuBar=Menu(root )
        
        def displayHelp(): 
            window=Toplevel(root ,background="white")
            window.focus()
            window.resizable(width=False ,height=False)

            details=Text(window ,background="white" ,height=14 ,width=43 ,borderwidth=4 )
            details.pack(side="top")

            details.insert("insert" ,enter_placement_help)
            details["state"]="disabled"

            exitButton=Button(window ,text="Ok" ,borderwidth=2 ,font=("Calibri" , 11) ,width=8 ,command=lambda : window.destroy() ,background="white")
            exitButton.pack(pady=10)

            window.mainloop()

        Help=Menu(menuBar ,tearoff=0)
        Help.add_command(label="How to use..." ,command=displayHelp)
        menuBar.add_cascade(label="Help" ,menu=Help)


        root.config(menu=menuBar)