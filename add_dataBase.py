from tkinter import * 
from components import * 


from pathlib import Path
from os import listdir 



add_dataBase_help="""Put text here
"""

class Add_dataBase(Frame): 
    def __init__(self ,parent ,root): 
        Frame.__init__(self ,parent ,background="white")

        # # Return button to home frame and next frame button
        frameReturn=Frame(self ,background="white")
        frameReturn.place_configure(relx=0.01 ,rely=0.01)
        
        self.return_image=PhotoImage(file= Path("Images/")/"return_button80x67.png")
        self.return_button=Button(frameReturn ,image=self.return_image ,borderwidth=0 ,background="white" )
        self.return_button.pack(side="left")
         

        # # Part for the little text at the top 
        frameText=Frame(self ,background="white")
        frameText.place_configure(relx=0.32 ,rely=0.01 )
       
        selectText=Label(frameText ,text="Ajouter une liste de composants" ,font=("Calibri" , 10) ,background="white")  
        selectText.pack_configure(side="top" ,pady=30)

        # # Part for the name of the dataBase file generated
        frameAddName=Frame(self ,background="white")
        frameAddName.place_configure(relx=0.005 ,rely=0.29)

        nameText=Label(frameAddName ,text="Nom de la liste     : " ,font=("Calibri" , 10 ) ,background="white" )
        nameText.pack(side="left" ,pady=10)

        self.name=StringVar()
        nameEntry=Entry(frameAddName ,width=40 ,borderwidth=2 ,textvariable=self.name )
        nameEntry.pack(side="left" ,pady=10)

        # # Part for the quantity of the given product(a product is a list of components)
        frameAddQuantity=Frame(self ,background="white")
        frameAddQuantity.place_configure(relx=0.005 ,rely=0.44 )

        quantityText=Label(frameAddQuantity ,text="Quantité produit  : " ,font=("Calibri" , 10 ) ,background="white")
        quantityText.pack(side="left" ,pady=10)

        self.quant=StringVar()
        nameEntry=Entry(frameAddQuantity ,width=40 ,borderwidth=2 ,textvariable=self.quant)
        nameEntry.pack(side="left" ,pady=10)
        self.quantity=None

 

        # # Part for the path of the excel file needed to generate the dataBase file
        frameAddPath=Frame(self ,background="white")
        frameAddPath.place_configure(relx=0.005 ,rely=0.59 )

        pathText=Label(frameAddPath ,text="Chemin                   : " ,font=("Calibri" ,10) ,background="white")
        pathText.pack(side="left" ,pady=10)

        self.pathXlFile=StringVar()
        pathEntry=Entry(frameAddPath ,width=40 ,borderwidth=2 ,textvariable=self.pathXlFile)
        pathEntry.pack(side="left" ,pady=10)


        # # part for validation of the new dataBase file
        frameValidation=Frame(self ,background="white")
        frameValidation.place_configure(relx=0.37 ,rely=0.8)

        vDataBase=Button(frameValidation ,borderwidth=1 ,font=("Calibri" , 11) ,width=15 ,height=2 ,text="valider" ,background="white" ,foreground="green") 
        vDataBase.pack(side="left")


        # # Part for the interact box 
        frameInteraction=Frame(self ,background="white")
        frameInteraction.place_configure(relx=0.74 ,rely=0.15)

        self.userInteraction=interactBox(frameInteraction ,wid=17 ,hei=12)
        self.userInteraction.pack(side="left")
        self.userInteraction.displayMessage("Je suis             Bibot \nVeuillez insérer le code à barre " ,"blue")



    def menu_bar(self ,root): 
        menuBar=Menu(root )
        
        def displayHelp(): 
            window=Toplevel(root ,background="white")
            window.focus()
            window.resizable(width=False ,height=False)

            details=Text(window ,background="white" ,height=9 ,width=43 ,borderwidth=4 )
            details.pack(side="top")

            details.insert("insert" ,add_dataBase_help)
            details["state"]="disabled"

            exitButton=Button(window ,text="Ok" ,borderwidth=2 ,font=("Calibri" , 11) ,width=8 ,command=lambda : window.destroy() ,background="white")
            exitButton.pack(pady=10)

            window.mainloop()

        Help=Menu(menuBar ,tearoff=0)
        Help.add_command(label="How to use..." ,command=displayHelp)
        menuBar.add_cascade(label="Help" ,menu=Help)


        root.config(menu=menuBar)