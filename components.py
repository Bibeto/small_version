#!/usr/bin/env python3
from tkinter import Entry ,StringVar ,Label ,Button ,Text ,Frame
from tkinter.ttk import Treeview ,Scrollbar ,Combobox 

from os import remove ,rename ,listdir ,mkdir 
from pathlib import Path


# limiting the size of the string entered in an Entry
def limitSize(var ,size): 
    if(len(var.get())>size) : 
        var.set(var.get()[:size])

# This function makes sure a StringVar has only integers 
def verify_integer(var): 
    value=var.get()
    if(value!=""): 
        try : int(value[len(value)-1])
        except ValueError : var.set(value[:len(value)-1])


class entry_code(Entry): 
    def __init__(self ,parent): 
        Entry.__init__(self ,parent ,borderwidth=2 ,font=("Calibri" , 12) ,width=28  )
        self.pack_configure(side="left" ,padx=15)
        self.barcode=StringVar(value="")
        self["textvariable"]=self.barcode

        def on_focusout(event):
            if(self.get()==""):
                self.delete(0 ,"end")
                self.insert(0, 'Scanner le code à barre')
                self.config(fg = 'grey')

        def on_entry_click(event):
            if(self.get()=="Scanner le code à barre"):
                self.delete(0, "end") 
                self.insert(0, '') 
                self.config(fg = 'black')
            

        self.insert(0, 'Scanner le code à barre')
        self.config(fg = 'grey')

        self.bind('<FocusIn>' ,on_entry_click )
        self.bind('<FocusOut>',on_focusout )
        self.barcode.trace("w" ,lambda *args : limitSize(self.barcode ,28))


        # # Two buttons to validate choice and delete the string in the entry

        self.vCode=Button(parent ,borderwidth=1 ,font=("Calibri" , 11) ,height=2 ,width=8 ,text="valider" ,background="white" ,foreground="green" ) 
        self.vCode.pack(side="left" ,padx=15)

        dCode=Button(parent ,borderwidth=1 ,font=("Calibri" , 11) ,height=2 ,width=8 ,text="supprimer" ,background="white" ,foreground="red" )
        dCode.pack(side="left" ,padx=15)

        

        # deleting the data input in the entry fpr barcode
        dCode["command"]= lambda : self.delete(0 ,"end")


        
class entry_chariot: 
    def __init__(self ,parent):      

        def shiftFocus(var ,nextEntry): 
            value=StringVar.get(var)
            if(len(value)==2): 
                Entry.focus_set(nextEntry)   

        #Beginning of placement of the same component 
        beginPlacementFrame=Frame(parent ,background="white")
        beginPlacementFrame.pack()

        self.chB=StringVar()
        self.lineB=StringVar()
        self.columnB=StringVar()

        ChariotBegin=Label(beginPlacementFrame ,font=("Calibri" , 11) ,background="white" ,text="Début : Ch" ,foreground="#478dca")
        ChariotBegin.pack(side="left")

        self.numChariotBegin=Entry(beginPlacementFrame ,borderwidth=2 ,font=("Calibri" , 10) ,width=2 ,textvariable=self.chB)
        self.numChariotBegin.pack(side="left" ,padx=10) 
        self.chB.trace("w" ,lambda *args : limitSize(self.chB ,2))
        self.chB.trace("w" ,lambda *args : verify_integer(self.chB))
        

        lineBegin=Label(beginPlacementFrame ,font=("Calibri" , 11) ,background="white" ,text="L" ,foreground="#478dca")
        lineBegin.pack(side="left" ,padx=10)
        
        self.numLineBegin=Entry(beginPlacementFrame ,borderwidth=2 ,font=("Calibri" , 10) ,width=2 ,textvariable=self.lineB)
        self.numLineBegin.pack(side="left" ,padx=10)
        self.lineB.trace("w" ,lambda *args : limitSize(self.lineB ,2))
        self.lineB.trace("w" ,lambda *args : verify_integer(self.lineB ))

        columnBegin=Label(beginPlacementFrame ,font=("Calibri" , 11) ,background="white" ,text="C" ,foreground="#478dca")
        columnBegin.pack(side="left" ,padx=10)
        
        self.numColumnBegin=Entry(beginPlacementFrame ,borderwidth=2 ,font=("Calibri" , 10) ,width=2 ,textvariable=self.columnB)
        self.numColumnBegin.pack(side="left" ,padx=10) 
        self.columnB.trace("w" ,lambda *args : limitSize(self.columnB ,2))
        self.columnB.trace("w" ,lambda *args : verify_integer(self.columnB ))

        # # shift focus from a certain entry to another if it's full

        self.chB.trace("w" ,lambda *args : shiftFocus(self.chB ,self.numLineBegin))
        self.lineB.trace("w" ,lambda *args : shiftFocus(self.lineB ,self.numColumnBegin))

        #End of placement of the same component 
        endPlacementFrame=Frame(parent ,background="white")
        endPlacementFrame.pack(pady=30)
        
        self.chE=StringVar()
        self.lineE=StringVar()
        self.columnE=StringVar()


        chariotEnd=Label(endPlacementFrame ,font=("Calibri" , 11) ,background="white" ,text="Fin(optionnel*) : Ch" ,foreground="#478dca")
        chariotEnd.pack(side="left" ,padx=5)
        

        self.numChariotEnd=Entry(endPlacementFrame ,borderwidth=2 ,font=("Calibri" , 10) ,width=2 ,textvariable=self.chE )
        self.numChariotEnd.pack(side="left" ,padx=5)
        self.chE.trace("w" ,lambda *args : limitSize(self.chE ,2))
        self.chE.trace("w" ,lambda *args : verify_integer(self.chE))

        lineEnd=Label(endPlacementFrame ,font=("Calibri" , 11) ,background="white" ,text="L" ,foreground="#478dca")
        lineEnd.pack(side="left" ,padx=10)
        
        self.numLineEnd=Entry(endPlacementFrame ,borderwidth=2 ,font=("Calibri" , 10) ,width=2 ,textvariable=self.lineE)
        self.numLineEnd.pack(side="left" ,padx=5)
        self.lineE.trace("w" ,lambda *args : limitSize(self.lineE ,2))
        self.lineE.trace("w" ,lambda *args : verify_integer(self.lineE))
        
        columnEnd=Label(endPlacementFrame ,font=("Calibri" , 11) ,background="white" ,text="C" ,foreground="#478dca")
        columnEnd.pack(side="left" ,padx=10)
        
        self.numColumnEnd=Entry(endPlacementFrame ,borderwidth=2 ,font=("Calibri" , 10) ,width=2 ,textvariable=self.columnE)
        self.numColumnEnd.pack(side="left" ,padx=5)
        self.columnE.trace("w" ,lambda *args : limitSize(self.columnE ,2))
        self.columnE.trace("w" ,lambda *args : verify_integer(self.columnE))

        # # shift focus of a certain entry to the next one if it's full
        
        self.chE.trace("w" ,lambda *args : shiftFocus(self.chE ,self.numLineEnd))
        self.lineE.trace("w" ,lambda *args : shiftFocus(self.lineE ,self.numColumnEnd))


    def del_entryChariot(self): 
        #delete Beginning placement
        self.numChariotBegin.delete(0 ,"end")
        self.numLineBegin.delete(0 ,"end")
        self.numColumnBegin.delete(0 ,"end")
        
        #delete End placement
        self.numChariotEnd.delete(0 ,"end")
        self.numLineEnd.delete(0 ,"end")
        self.numColumnEnd.delete(0 ,"end")

class interactBox(Text): 
    def __init__(self ,parent ,wid=50 ,hei=3): 
        Text.__init__(self ,parent ,width=wid ,height=hei ,borderwidth=2 ,font=("Calibri" , 11) )
        
    
    def displayMessage(self ,mess ,color): 
        if(color=="blue"): 
            self["state"]="normal"
            self["background"]="#7b8994"
            self["foreground"]="white"
            self.delete("1.0" ,"end")
            self.insert("insert" ,"   |'_'|   {}".format(mess)) 
            self["state"]="disabled"
        if(color=="red"):
            self["state"]="normal"
            self["background"]="red"
            self["foreground"]="white"
            self.delete("1.0" ,"end")
            self.insert("insert" ,"   |'~'|   {}".format(mess)) 
            self["state"]="disabled"
          
        

            


class listOfProducts(Combobox): 
    def __init__(self ,parent):
        selectText=Label(parent ,text="Sélectionner une liste des composants" ,font=("Calibri" , 11) ,background="white")  
        selectText.pack(side="top" ,pady=25)

        self.dataBaseSelected=StringVar()
        Combobox.__init__(self, parent ,width=25 ,state="readonly" ,textvariable=self.dataBaseSelected)
        self.pack(side="top" ,pady=25)

        


        
#this function returns the equivalent of a stringVar in numerals or None if it's an empty stringVar
def convert_to_int(value): 
    if(StringVar.get(value)==""): return None
    else : return int(StringVar.get(value))
        
# function to see if the barcode reference in the entry is existent, 
# that is taken in account of incorrect caracters included before or after the reference
def resemble(text ,original): 
    if(original==""): 
        if(text==""): return True
        else : return False
    else : 
        if(text==""): return False 
        else : 
            if(original in text): return True
            else : return False 


# This function makes the file naming correspondent to windows and Linux based OS restrictions for file naming 
def entryNameConstraints(var): 
    restrictedList=('<' ,'>' ,':' ,'"' ,'/' ,'\\' ,'|' ,'?' ,'*' ,'.' ,'\n') 
    value=var.get() 
    if(len(value)>40): 
        StringVar.set(var ,value[:41])
    if(value !=""):
        if(value[len(value)-1] in restrictedList) :
            value=value[:len(value)-1]
            StringVar.set(var ,value)

# # This function clears spaces before and after file names 
def clear_spaces(var): 
    value=StringVar.get(var)
    if(value!=""): 
        while(value[len(value)-1]==' ') :
            value=value[:len(value)-1]
            if (value=="") : break 
    if(value!=""):
        while(value[0]==' '): 
            value=value[1:]
            if (value=="") : break 
    StringVar.set(var ,value)