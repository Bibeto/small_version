from tkinter import * 
from components import * 



enter_quantity_help="""Put text here
"""



class Enter_quantity(Frame): 
    def __init__(self ,parent ,root):
        Frame.__init__(self ,parent ,background="white")

        # Return button to precedent frame and next frame button
        frameReturn=Frame(self ,background="white")
        frameReturn.place_configure(relx=0.01 ,rely=0.01)
        
        self.return_image=PhotoImage(file= Path("Images/")/"return_button80x67.png")
        self.return_button=Button(frameReturn ,image=self.return_image ,borderwidth=0 ,background="white" ,relief="groove")
        self.return_button.pack(side="left")
         

        # # Part for the entry of the quantity of the component 
        frameQuantity=Frame(self ,background="white")
        frameQuantity.place_configure(relx=0.005 ,rely=0.35)

        quantityText=Label(frameQuantity ,background="white" ,font=("Calibri" , 11) ,text="Quantité :" ,foreground="#478dca" )
        quantityText.pack(side="left" )

        self.quantity=StringVar()
        quantityEntry=Entry(frameQuantity ,borderwidth=2 ,font=("Calibri" , 12) ,textvariable=self.quantity ,width=20)
        quantityEntry.pack(side="left" ,padx=5)

        self.quantityAdd=Button(frameQuantity ,borderwidth=1 ,font=("Calibri" , 11) ,height=2 ,width=8 ,text="augmenter" ,background="white" ,foreground="green" )
        self.quantityAdd.pack(side="left" ,padx=10)

        self.quantityReduce=Button(frameQuantity ,borderwidth=1 ,font=("Calibri" , 11) ,height=2 ,width=8 ,text="réduire" ,background="white" ,foreground="red" )
        self.quantityReduce.pack(side="left" ,padx=10)

        quantityDelete=Button(frameQuantity ,borderwidth=1 ,font=("Calibri" , 11) ,height=2 ,width=8 ,text="supprimer" ,background="white" ,foreground="red" )
        quantityDelete.pack(side="left" ,padx=10)

        # # Part for the interact box , this shows the details concerning the component
        frameInteraction=Frame(self ,background="white")
        frameInteraction.place_configure(relx=0.05 ,rely=0.6)

        self.userInteraction=interactBox(frameInteraction ,hei=5)
        self.userInteraction.pack(side="left")
        self.userInteraction.displayMessage("Je suis Bibot \nVeuillez insérer le code à barre " ,"blue")


        # # Part for the entry of the barcode and its subsquent validation
        frameBarCode=Frame(self ,background="white")
        frameBarCode.place_configure(relx=0.2 ,rely=0.1)

        self.entry=entry_code(frameBarCode)

        self.timesScanned=0                           #shows me the number of times scanned for a single component

        self.selectedBarcode=""


  
    def menu_bar(self ,root): 
        menuBar=Menu(root )
        
        def displayHelp(): 
            window=Toplevel(root ,background="white")
            window.focus()

            details=Text(window ,background="white" ,height=10 ,width=43 ,borderwidth=4 )
            details.pack(side="top")

            details.insert("insert" ,enter_quantity_help)
            details["state"]="disabled"

            exitButton=Button(window ,text="Ok" ,borderwidth=2 ,font=("Calibri" , 11) ,width=8 ,command=lambda : window.destroy() ,background="white")
            exitButton.pack(pady=10)

            window.mainloop()

        Help=Menu(menuBar ,tearoff=0)
        Help.add_command(label="How to use..." ,command=displayHelp)
        menuBar.add_cascade(label="Help" ,menu=Help)


        root.config(menu=menuBar)