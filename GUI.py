from customtkinter import *
from PIL import Image

#  creating the window and setting size and mode
window = CTk()
window.title('Study Material Repository')
window.geometry('600x500')
window.minsize(600,500)
set_appearance_mode('light')

# declaring vars for image data and making image objects with size

user_img_data = Image.open('User1.png')
password_img_data = Image.open('password1.png')
side_img_data = Image.open('bg.png')
logo_img_data = Image.open('logo.png')

user_img = CTkImage(dark_image=user_img_data, light_image=user_img_data, size=(17, 17))
password_img = CTkImage(dark_image=password_img_data, light_image=password_img_data, size=(17, 17))
side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 300))
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(50,50))

# Label for images on the left side

side_img_label = CTkLabel(master=window, text="", image=side_img)
side_img_label.pack(expand=True, side="left")

# Frame for the stuff on the right side

right_frame = CTkFrame(master=window, height=500, width=300, fg_color="#ffffff")
right_frame.pack(expand=True, side='right', fill='both')

# Login frame to show the labels and entries

login_frame = CTkFrame(master=right_frame, height=500, width=300, fg_color="#ffffff")
login_frame.propagate(False)
login_frame.pack(expand=True)

# Logo

logo_img_label = CTkLabel(master=login_frame, text="", image=logo_img)
logo_img_label.pack(pady=10)

# Title that says Login

title_label = CTkLabel(master=login_frame, text='Login', text_color='#1f61a5',anchor='w', justify='left', font=("Arial Bold", 24))
title_label.pack(anchor="w", pady=(50, 5), padx=(25, 0))

# Label and entry for user id

id_label = CTkLabel(master=login_frame, text='  ID Number', text_color="#1f61a5", anchor="w", justify="left", font=("Arial Bold", 14), image=user_img, compound="left")
id_label.pack(anchor="w", pady=(38, 0), padx=(25, 0))
id_entry = CTkEntry(master=login_frame, width=225, fg_color="#EEEEEE", border_color="#1f61a5", border_width=1, text_color="#000000")
id_entry.pack(anchor="w", padx=(25, 0))

# label and entry for password

password_label = CTkLabel(master=login_frame, text='  Password', text_color="#1f61a5", anchor="w", justify="left", font=("Arial Bold", 14), image=password_img, compound="left")
password_label.pack(anchor="w", pady=(38, 0), padx=(25, 0))
password_entry = CTkEntry(master=login_frame,show='*', width=225, fg_color="#EEEEEE", border_color="#1f61a5", border_width=1, text_color="#000000")
password_entry.pack(anchor="w", padx=(25, 0))

#Login button

login_button = CTkButton(master=login_frame,text="Login", fg_color="#1f61a5", hover_color="#19429d", font=("Arial Bold", 12), text_color="#ffffff", width=225)
login_button.pack(anchor="w", pady=(40, 0), padx=(25, 0))

# run
window.mainloop()
