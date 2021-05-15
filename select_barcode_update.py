#!/usr/bin/env python3
from tkinter import * 


from components import *



select_barcode_update_help="""Put text here
"""

class Select_barcode_update(Frame): 
    def __init__(self , parent ,root): 
        Frame.__init__(self ,parent ,background="white")

        

        # Return and next buttons to transition from precedent to next frame and vice versa
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
        
        # # Part for the entry of the barcode and its subsquent validation
        frameBarCode=Frame(self ,background="white")
        frameBarCode.place_configure(relx=0.005 ,rely=0.4)

        self.entry=entry_code(frameBarCode)

        self.barcodeChosen=""


        # # Part for the interact box 
        frameInteraction=Frame(self ,background="white")
        frameInteraction.place_configure(relx=0.05 ,rely=0.63)

        self.userInteraction=interactBox(frameInteraction ,hei=5)
        self.userInteraction.pack(side="left")
        self.userInteraction.displayMessage("Je suis Bibot \nVeuillez insérer le code à barre " ,"blue")


        
    def update_interactBox(self ,component ,li): 
        mess="Composant : {}".format(component)
        mess+= "\nCoordonnées Début Ch : {}  - L : {}  - C : {} ".format(li[0] ,li[1] ,li[2] )
        mess+= "\nCoordonnées Fin Ch : {}  - L : {}  - C : {} ".format(li[3] ,li[4] ,li[5])
        mess+="\nQuantité actuel : {}    Quantité objectif : {}".format(li[6] ,li[7])
        self.userInteraction.displayMessage(mess ,"blue")
                     
    def menu_bar(self ,root): 
        menuBar=Menu(root)
        
        def displayHelp(): 
            window=Toplevel(root ,background="white")
            window.focus()
            window.resizable(width=False ,height=False)

            details=Text(window ,background="white" ,height=14 ,width=40 ,borderwidth=4 )
            details.pack(side="top")

            details.insert("insert" ,select_barcode_update_help)
            details["state"]="disabled"

            exitButton=Button(window ,text="Ok" ,borderwidth=2 ,font=("Calibri" , 11) ,width=8 ,command=lambda : window.destroy() ,background="white")
            exitButton.pack(pady=10)

            window.mainloop()

        Help=Menu(menuBar ,tearoff=0)
        Help.add_command(label="How to use..." ,command=displayHelp)
        menuBar.add_cascade(label="Help" ,menu=Help)


        root.config(menu=menuBar)