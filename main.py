import base64
import tkinter as tk

import firebase_admin
from PIL import Image
from customtkinter import *
from firebase_admin import credentials, firestore

cred = credentials.Certificate(
    r"D:\Desktop\Python\study-mat-repo\study-material-repo-firebase-adminsdk-bj0om-72965ed62f.json")  # your path will be different based on where you store your private key
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


def user_details_add():
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
                next_page(login_page, main_menu)
                main_menu.pack(expand=True, fill='both')
                # exit(0)   exit the function if login is successful

        if flag == 0:
            print("Wrong username or password, try again")
            id_entry.delete(0, END)
            password_entry.delete(0, END)
            set_text("Wrong username or password, try again")
            login()

def select_pdf_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path

def upload_pdf_using_dialog(filename, description):
    pdf_path = select_pdf_file()
    if pdf_path:
        with open(pdf_path, "rb") as f:
            pdf_data = f.read()
            pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')

        db.collection("pdfs").add({
            "filename": filename,
            "description": description,
            "pdf_data": pdf_base64
        })


def select_destination_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path


def download_pdf(pdf_id):
    destination_folder = select_destination_folder()
    if not destination_folder:
        print("No destination folder selected.")
        return

    doc_ref = db.collection("pdfs").document(pdf_id)
    doc = doc_ref.get()
    if doc.exists:
        pdf_data_base64 = doc.to_dict()["pdf_data"]
        pdf_data = base64.b64decode(pdf_data_base64)

        file_path = os.path.join(destination_folder, "downloaded_pdf.pdf")

        with open(file_path, "wb") as f:
            f.write(pdf_data)

        print(f"PDF downloaded successfully to: {file_path}")
    else:
        print("No such document!")


#  pdfs_id = "ZnceNJGoYhUflbKxMrpX"
#  download_pdf(pdfs_id)

def show_tabs(tab_name):
    menu_tabs.pack(expand=True, fill='both')
    main_menu.pack_forget()
    menu_tabs.set(tab_name)


def next_page(current_page, next_page_frame):
    current_page.pack_forget()
    next_page_frame.pack(expand=True, fill='both')


def set_text(text):  # function to set error text
    error_label.configure(text=text)

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
                         font=("Arial Bold", 12), text_color="#ffffff", width=225, command=lambda: login())
login_button.pack(anchor="w", pady=(40, 0), padx=(25, 0))

# Main Menu
main_menu = CTkFrame(master=window)

# Buttons menu
main_menu_title = CTkLabel(master=main_menu, text="Choose Tab", text_color='#1f61a5', anchor='w', justify='left',
                           font=("Arial Bold", 24))
main_menu_title.pack()

buttons_menu = CTkFrame(master=main_menu)
buttons_menu.pack(pady=20)

notes_button = CTkButton(master=buttons_menu, text='Notes', command=lambda: show_tabs('Notes'))
notes_button.pack(pady=20, padx=15)
qb_button = CTkButton(master=buttons_menu, text='Question Banks', command=lambda: show_tabs('Question Banks'))
qb_button.pack(pady=20, padx=15)
qna_button = CTkButton(master=buttons_menu, text='Q & A', command=lambda: show_tabs('Q & A'))
qna_button.pack(pady=20, padx=15)

# Tabs
menu_tabs = CTkTabview(master=window)

notes_tab = menu_tabs.add('Notes')
qb_tab = menu_tabs.add('Question Banks')
qna_tab = menu_tabs.add('Q & A')

# Notes tab
note_dropdown_menu = CTkFrame(master=notes_tab, height=500, width=200)
note_dropdown_menu.pack(side='left')

courses = ['', 'B.Tech', 'Other']
branches = ['', 'CSE', 'Other']
years = ['', '1st year', '2nd year', '3rd year', '4th year']
subjects = ['']
modules = ['', '1', '2', '3', '4', '5']

courses_box = CTkComboBox(master=note_dropdown_menu, values=courses).pack(pady=20, padx=10)
branches_box = CTkComboBox(master=note_dropdown_menu, values=branches).pack(pady=20, padx=10)
years_box = CTkComboBox(master=note_dropdown_menu, values=years).pack(pady=20, padx=10)
subjects_box = CTkComboBox(master=note_dropdown_menu, values=subjects).pack(pady=20, padx=10)
modules_box = CTkComboBox(master=note_dropdown_menu, values=modules).pack(pady=20, padx=10)

search_button = CTkButton(master=note_dropdown_menu, text='Search').pack(pady=20)

# qb tab
qb_dropdown_menu = CTkFrame(master=qb_tab, height=500, width=200)
qb_dropdown_menu.pack(side='left')
qb_courses_box = CTkComboBox(master=qb_dropdown_menu, values=courses).pack(pady=20, padx=10)
qb_branches_box = CTkComboBox(master=qb_dropdown_menu, values=branches).pack(pady=20, padx=10)
qb_years_box = CTkComboBox(master=qb_dropdown_menu, values=years).pack(pady=20, padx=10)
qb_subjects_box = CTkComboBox(master=qb_dropdown_menu, values=subjects).pack(pady=20, padx=10)
qb_modules_box = CTkComboBox(master=qb_dropdown_menu, values=modules).pack(pady=20, padx=10)

qb_search_button = CTkButton(master=qb_dropdown_menu, text='Search').pack(pady=20)

# run
window.mainloop()
