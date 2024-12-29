# import random
# import string
# a=string.ascii_letters
# print(a)
# e=list(a)
# b=string.digits
# f=list(b)
# c=string.punctuation
# g=list(c)
# k=e+f+g








# for i in range(8):
#     random_choice1=random.choices(k)
#     random_choice=''.join(random_choice1)
#     print(random_choice,end="")




# list1=["1",2,3,'4',5,6,8,7,8]
# shuffling=random.shuffle(list1)
# print(list1)

# import tkinter as tk

# # Create the main window
# root = tk.Tk()
# root.title("Simple Tkinter App")
# root.geometry("300x200")  # Set window size (width x height)

# # Add a label
# label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14))
# label.pack(pady=10)  # Add padding around the label

# # Function to change label text when the button is clicked
# def on_button_click():
#     label.config(text="Button Clicked!")

# # Add a button
# button = tk.Button(root, text="Click Me", command=on_button_click)
# button.pack(pady=5)

# # Run the application
# root.mainloop()

from colorama import Fore, Style

print(Style.BRIGHT + "This is bold text" + Style.RESET_ALL)
print("Normal text")






