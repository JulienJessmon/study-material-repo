# import required modules
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from customtkinter import *
from PIL import Image

cred = credentials.Certificate(
    r"C:\Users\Admin\PycharmProjects\MiniProject\study-material-repo-firebase-adminsdk-bj0om-7cddb30570.json")
# your path will be different based on where you store your private key
firebase_admin.initialize_app(cred)
db = firestore.client()

user_img_data = Image.open('Images/User1.png')
password_img_data = Image.open('Images/password1.png')
side_img_data = Image.open('Images/bg.png')
logo_img_data = Image.open('Images/logo.png')

user_img = CTkImage(dark_image=user_img_data, light_image=user_img_data, size=(17, 17))
password_img = CTkImage(dark_image=password_img_data, light_image=password_img_data, size=(17, 17))
side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 300))
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(50, 50))


def next_page(current_page, next_page):
    current_page.pack_forget()
    next_page.pack(expand=True, fill='both')


def set_text(text):  # function to set error text
    error_label.configure(text=text)


def login():
    username = id_entry.get()
    password = password_entry.get()
    if username != "" and password != "":
        docs = db.collection('userCollection').stream()
        document_list = [doc for doc in docs]
        flag = 0
        for doc in document_list:
            doc_data = doc.to_dict()
            us1 = doc_data.get('Username')
            ps1 = doc_data.get('Password')

            if username == us1 and password == ps1:
                print("Logged in")
                flag = 1
                next_page(login_page,menu_frame)
                menu_frame.pack(expand=True, fill='both')
                # exit(0)   exit the function if login is successful

        if flag == 0:
            print("Wrong username or password, try again")
            id_entry.delete(0, END)
            password_entry.delete(0, END)
            set_text("Wrong username or password, try again")
            login()


def user_details_add():  # function to add user
    flag = 0
    username = id_entry.get()
    password = password_entry.get()
    if username != "" and password != "":
        if (password.islower() is False) and (password.isalnum() is False) and (password.isspace() is False) and (
                len(password) >= 8):
            has_number = False
            for char in password:
                if not char.isnumeric():
                    has_number = True
                    break
            if has_number is True:
                flag = 1
            elif has_number is False:
                set_text(
                    "A minimum 8 characters password contains a \ncombination of uppercase and lowercase letter \nand "
                    "number are required")
                id_entry.delete(0, END)
                password_entry.delete(0, END)
                user_details_add()
        if flag == 1:
            data = {
                'Username': username,
                'Password': password
            }

            doc_ref = db.collection('userCollection').document()
            doc_ref.set(data)

            print('DocumentID: ', doc_ref.id)  # purely for knowing it works, don't need it in the code
        if flag == 0:
            set_text(
                "A minimum 8 characters password contains a \ncombination of uppercase and lowercase letter \nand "
                "number are required")
            id_entry.delete(0, END)
            password_entry.delete(0, END)
            user_details_add()
    id_entry.delete(0, END)
    password_entry.delete(0, END)


# GUI Code
# window
window = CTk()
window.title('Study Material Repository')
window.geometry('600x500')
window.minsize(600, 500)
set_appearance_mode('light')

# Login page
login_page = CTkFrame(master=window)
login_page.pack(expand=True, fill='both')
side_img_label = CTkLabel(master=login_page, text="", image=side_img)
side_img_label.pack(expand=True, side="left")

right_frame = CTkFrame(master=login_page, height=500, width=300, fg_color="#ffffff")
right_frame.pack(expand=True, side='right', fill='both')

login_frame = CTkFrame(master=right_frame, height=500, width=300, fg_color="#ffffff")
login_frame.propagate(False)
login_frame.pack(expand=True)

logo_img_label = CTkLabel(master=login_frame, text="", image=logo_img)
logo_img_label.pack(pady=10)

title_label = CTkLabel(master=login_frame, text='Log in', text_color='#1f61a5', anchor='w', justify='left',
                       font=("Arial Bold", 24))
title_label.pack(anchor="w", pady=(50, 5), padx=(25, 0))

id_label = CTkLabel(master=login_frame, text='  User ID', text_color="#1f61a5", anchor="w", justify="left",
                    font=("Arial Bold", 14), image=user_img, compound="left")
id_label.pack(anchor="w", pady=(38, 0), padx=(25, 0))
id_entry = CTkEntry(master=login_frame, width=225, fg_color="#EEEEEE", border_color="#1f61a5", border_width=1,
                    text_color="#000000")
id_entry.pack(anchor="w", padx=(25, 0))

password_label = CTkLabel(master=login_frame, text='  Password', text_color="#1f61a5", anchor="w", justify="left",
                          font=("Arial Bold", 14), image=password_img, compound="left")
password_label.pack(anchor="w", pady=(38, 0), padx=(25, 0))
password_entry = CTkEntry(master=login_frame, show='*', width=225, fg_color="#EEEEEE", border_color="#1f61a5",
                          border_width=1, text_color="#000000")
password_entry.pack(anchor="w", padx=(25, 0))

error_label = CTkLabel(master=login_frame, text="", text_color="#FF0000")
error_label.pack(anchor="w", padx=(25, 0))

login_button = CTkButton(master=login_frame, text="Login", fg_color="#1f61a5", hover_color="#19429d",
                         font=("Arial Bold", 12), text_color="#ffffff", width=225, command=login)
login_button.pack(anchor="w", pady=(40, 0), padx=(25, 0))

# Menu
menu_frame = CTkFrame(master=window)
menu_title_label = CTkLabel(master=menu_frame, text='Welcome', text_color='#1f61a5', anchor='w', justify='left',
                            font=("Arial Bold", 24))
menu_title_label.pack()

# run
window.mainloop()
