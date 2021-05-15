# This work was done by https://github.com/Bibeto
# I m in no way a UI expert 
# This is just a personal project 

# Well a little bit of context 
# This is a "shell" of an old project I did
# so be warned the naming is a bit hard to understand 
# This file is the main file to run 
# The overall project contains 3 parts 
# Update, browse, settings 
# They are three buttons that give us access to many frames  


from tkinter import Tk ,Frame
from tkinter import messagebox
from components import *


from home import Home
from select_dataBase import Select_dataBase
from select_barcode_browse import Select_barcode_browse
from select_barcode_update import Select_barcode_update
from enter_placement import Enter_placement
from enter_quantity import Enter_quantity
from select_delete_dataBase import Select_delete_dataBase
from add_dataBase import Add_dataBase

class App(Tk):
    def __init__(self ,*args ,**kwargs):
        Tk.__init__(self)
        Tk.title(self ,"Bibeto's App")
        self.geometry("620x260+30+0")

        self.container=Frame(self)
        self.container.pack(side="top" ,fill="both" ,expand=True)
        self.container.grid_rowconfigure(0 ,weight=1)
        self.container.grid_columnconfigure(0 ,weight=1)
        

        self.protocol("WM_DELETE_WINDOW", lambda :  self.exit_handler() )

    def show_frame(self ,frame): 
        frame.tkraise()

        menu=frame.menu_bar(self)
    
    def exit_handler(self):
       if messagebox.askokcancel("Bibeto's app", "Sure you want to quit ?" ) : 
            self.destroy()
            
        

# The root window 
myApp=App()


# home frame
homeFrame=Home(myApp.container ,App)
homeFrame.grid(row=0 ,column=0 ,sticky="nsew")


# declaring the frames for the update 
enter_placement_frame=Enter_placement(myApp.container ,App)
enter_placement_frame.grid(row=0 ,column=0 ,sticky="nsew")

select_barcode_update_frame=Select_barcode_update(myApp.container ,App)
select_barcode_update_frame.grid(row=0 ,column=0 ,sticky="nsew")

select_dataBase_update_frame=Select_dataBase(myApp.container ,App)
select_dataBase_update_frame.grid(row=0 ,column=0 ,sticky="nsew")

# declaring the frames for browse
select_barcode_browse_frame=Select_barcode_browse(myApp.container ,App)
select_barcode_browse_frame.grid(row=0 ,column=0 ,sticky="nsew")

select_dataBase_browse_frame=Select_dataBase(myApp.container ,App)
select_dataBase_browse_frame.grid(row=0 ,column=0 ,sticky="nsew")


# declare the frames for Settings 
select_delete_dataBase_frame=Select_delete_dataBase(myApp.container ,App)
select_delete_dataBase_frame.grid(row=0 ,column=0 ,sticky="nsew")

enter_quantity_frame=Enter_quantity(myApp.container ,App)
enter_quantity_frame.grid(row=0 ,column=0 ,sticky="nsew")

add_dataBase_frame=Add_dataBase(myApp.container ,App)
add_dataBase_frame.grid(row=0 ,column=0 ,sticky="nsew")


myApp.show_frame(homeFrame)


# # # # This part is for transition from frame to another 
# # # # I m doing the transitioning here because the object frames exist here 
# # # Home frame buttons commands

homeFrame.Output_button["command"]=lambda : myApp.show_frame(select_dataBase_browse_frame)
homeFrame.Input_button["command"]=lambda : myApp.show_frame(select_dataBase_update_frame)
homeFrame.Settings_button["command"]= lambda : myApp.show_frame(select_delete_dataBase_frame)



# # # Setttings button frames
# Transition from Home to select_delete_dataBase and vice versa
select_delete_dataBase_frame.return_button["command"]=lambda : myApp.show_frame(homeFrame)
select_delete_dataBase_frame.next_button["command"]=lambda : myApp.show_frame(add_dataBase_frame)
# Transition from add_dataBase_frame to select_delete_dataBase with an update 
add_dataBase_frame.return_button["command"]=lambda : myApp.show_frame(select_delete_dataBase_frame) 

# # # Browse button frames
# Transition from Home to select_dataBase_frame for browse button
select_dataBase_browse_frame.return_button["command"]=lambda : myApp.show_frame(homeFrame) 
select_dataBase_browse_frame.next_button["command"]=lambda : myApp.show_frame(select_barcode_browse_frame)
# Transition from select_barcode_browse_frame to select_dataBase_browse_frame
select_barcode_browse_frame.return_button["command"]=lambda : myApp.show_frame(select_dataBase_browse_frame)

# # # Update button frames 
# Transition from Home to select_dataBase_frame for update button
select_dataBase_update_frame.return_button["command"]=lambda : myApp.show_frame(homeFrame)  
select_dataBase_update_frame.next_button["command"]=lambda : myApp.show_frame(select_barcode_update_frame)
# Transition from select_barcode_update_frame to select_database_frame
select_barcode_update_frame.return_button["command"]=lambda : myApp.show_frame(select_dataBase_update_frame)
select_barcode_update_frame.next_button["command"]=lambda   : myApp.show_frame(enter_placement_frame)
# Transition from enter_placement_frame to and forth 
enter_placement_frame.return_button["command"]=lambda : myApp.show_frame(select_barcode_update_frame)
enter_placement_frame.next_button["command"]=lambda : myApp.show_frame(enter_quantity_frame)
# # Transition from enter_quantity_frame to enter_placement_frame 
enter_quantity_frame.return_button["command"]=lambda : myApp.show_frame(enter_placement_frame)


myApp.mainloop()