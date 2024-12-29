import tkinter as tk

# create main window
root=tk.Tk()
root.title("WELCOME TO RANDOM PASSWORD GENERATOR") # SET TITLE OF THE WINDOW
root.geometry("300x200") # set the size of the window.(width*height)
root.configure(bg="lightblue")


# create widgets
label1=tk.Label(root,text="RANDOM PASSWORD GENERATOR",
font=("Arial",14),  # this is for font style
fg="black",   #adds font colour to the text
bg="red",       # adds background colour to the text
padx="1000" ,        # padding in x direction
pady="1",          # padding in y direction
borderwidth="1",       # Border thickness
relief="solid"       # Border style: flat, raised, sunken, groove, ridge
)
label1.pack()

def button_on_click(): 
    label1.config(text="button was clicked")

button=tk.Button(root,text="click me",command=button_on_click)
button.pack()







# label.pack(paddy=5)

# # Function to change label text when the button is clicked
# def on_button_click():
#     label.config(text="button clicked")


# # add button
# button=tk.Button(root,text="click me",command=on_button_click)
# button.pack(paddy=5)

# # start the app
root.mainloop()