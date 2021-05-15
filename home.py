#!/usr/bin/env python3
from tkinter import messagebox ,PhotoImage ,Button ,Frame ,Menu ,Label ,Toplevel  

from components import *
from os import path



font_text = ("Calibri" , 10 )

explanation_info_window="""Put text here 
"""

application_details="""This application was developed by Bibeto
you can find me here 
https://github.com/Bibeto
"""

class Home(Frame): 
    def __init__(self ,parent ,root):
        Frame.__init__(self ,parent ,background="white")

        self.info_photo=PhotoImage(file= Path("Images/")/"info35x35.png")
        info=Button(self ,image=self.info_photo ,borderwidth=0 ,background="white" ,width=33 ,height=33 ,command=lambda : messagebox.showinfo("information" ,explanation_info_window) )
        info.place(relx=0.9 ,rely=0.02)

        self.Input_button=Button(self ,text="Update" ,font=font_text ,background="white" ,activebackground="white" ,borderwidth=1 ,width=16 ,height=6 )
        self.Input_button.place(relx=0.1 ,rely=0.52)

        self.Output_button=Button(self ,text="Browse" ,font=font_text ,background="white" ,activebackground="white" ,borderwidth=1 ,width=16 ,height=6 )
        self.Output_button.place(relx=0.39 ,rely=0.52)

        self.Settings_button=Button(self ,text="Settings" ,font=font_text ,background="white" ,activebackground="white" ,borderwidth=1 ,width=16 ,height=6 )
        self.Settings_button.place(relx=0.68 ,rely=0.52)
             

        
    #Menubar at the top : main components edit , help  and about
    def menu_bar(self ,root): 
        menuBar=Menu(root)

        def displayDetails() :
            window=Toplevel(root ,background="white")
            window.focus()
            window.resizable(width=False ,height=False)

            details=Text(window ,background="white" ,height=9 ,width=42 ,borderwidth=4 )
            details.pack(side="top")

            details.insert("insert" ,application_details)
            details["state"]="disabled"

            exitButton=Button(window ,text="Ok" ,borderwidth=2 ,font=("Calibri" , 11) ,width=8 ,command=lambda : window.destroy() ,background="white")
            exitButton.pack(pady=10)

            window.mainloop()

        about=Menu(menuBar ,tearoff=0 )
        about.add_command(label="Information" ,font=("Calibri" , 10 ) ,command=displayDetails )
        menuBar.add_cascade(label="About..." ,menu=about)

        root.config(menu=menuBar)