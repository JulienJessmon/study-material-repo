import tkinter as tk
import firebase_admin
import pyrebase
import requests
from PIL import Image
from customtkinter import *
from firebase_admin import credentials, firestore, storage

cred = credentials.Certificate(
    r"C:\Users\Admin\PycharmProjects\MiniProject\study-material-repo-firebase-adminsdk-bj0om-7cddb30570.json")
# your path will be different based on where you store your private key
firebase_admin.initialize_app(cred, {
    "apiKey": "AIzaSyCtubeFcnQtDDC0Algoy09TvtvgjJyRojA",
    "authDomain": "study-material-repo.firebaseapp.com",
    "projectId": "study-material-repo",
    'storageBucket': "study-material-repo.appspot.com",
    "messagingSenderId": "291006521607",
    "appId": "1:291006521607:web:7196317a36dcf6f0e365a2",
    "measurementId": "G-6EGQ548K06",
    "databaseURL": ""
})
db = firestore.client()
bucket = storage.bucket()
config = {
    "apiKey": "AIzaSyCtubeFcnQtDDC0Algoy09TvtvgjJyRojA",
    "authDomain": "study-material-repo.firebaseapp.com",
    "projectId": "study-material-repo",
    "storageBucket": "study-material-repo.appspot.com",
    "messagingSenderId": "291006521607",
    "appId": "1:291006521607:web:7196317a36dcf6f0e365a2",
    "measurementId": "G-6EGQ548K06",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

CSE_subjects = {
    '1st year': ['PHT 100', 'PHT 110', 'MAT 101', 'EST 100', 'EST 120', 'HUT 101', 'CYT 100', 'EST 110', 'MAT 102',
                 'EST 102', 'EST 130', 'HUT 102'],
    '2nd year': ['MAT 203', 'CST 201', 'CST 203', 'MNC 202', 'EST 200', 'HUT 200', 'MAT 206', 'CST 202', 'CST 204',
                 'CST 206', 'EST 200', 'HUT 200', 'MNC 202'],
    '3rd year': ['CST 303', 'CST 305', 'CST 307', 'CST 309', 'MCN 301', 'CST 301', 'CST 302', 'CST 304', 'CST 306',
                 'CST 322', 'CST 332', 'HUT 300'],
    '4th year': [''],
}

user_img_data = Image.open('Images/User1.png')
password_img_data = Image.open('Images/password1.png')
side_img_data = Image.open('Images/bg.png')
logo_img_data = Image.open('Images/logo.png')
search_img_data = Image.open('Images/search.png')
upload_img_data = Image.open('Images/upload.png')
upvote_img_data = Image.open('Images/upvote.png')
download_img_data = Image.open('Images/download.png')

user_img = CTkImage(dark_image=user_img_data, light_image=user_img_data, size=(17, 17))
password_img = CTkImage(dark_image=password_img_data, light_image=password_img_data, size=(17, 17))
side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 300))
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(50, 50))
search_img = CTkImage(dark_image=search_img_data, light_image=search_img_data, size=(17, 17))
upload_img = CTkImage(dark_image=upload_img_data, light_image=upload_img_data, size=(17, 17))
upvote_img = CTkImage(dark_image=upvote_img_data, light_image=upvote_img_data, size=(17, 17))
download_img = CTkImage(dark_image=download_img_data, light_image=download_img_data, size=(17, 17))

current_notes_search_dir = ''
current_videos_search_dir = ''
current_qb_search_dir = ''
file_names = []


def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path


def upload_pdf_using_dialog(material_type):
    if material_type == 'notes':
        file_name = notes_upload_filename_entry.get()
        course = notes_upload_course_box.get()
        branch = notes_upload_branch_box.get()
        year = notes_upload_year_box.get()
        subject = notes_upload_subject_box.get()
        module = notes_upload_module_box.get()
        if all({file_name, course, branch, year, subject, module}):
            pdf_path = select_pdf_file()
            if pdf_path:
                with open(pdf_path, "rb") as f:
                    pdf_data = f.read()
                    storage.child(f"pdfs/{course}/{branch}/{year}/{subject}/{module}/" + file_name).put(pdf_data)
                    print("PDF uploaded successfully!")
                    notes_upload_error_label.configure(text='PDF uploaded successfully!')
                    notes_upload_filename_entry.delete(0, END)
                    notes_upload_course_box.set("")
                    notes_upload_branch_box.set("")
                    notes_upload_year_box.set("")
                    notes_upload_subject_box.set("")
                    notes_upload_module_box.set("")
        else:
            notes_upload_error_label.configure(text='Fill all fields!')
        db.collection("pdfData").add({
            "filename": file_name,
            "upvotes": 0,
            "uploadedBy": loggedInUser,
            "downloads": 0
        })
    elif material_type == 'qb':
        file_name = qb_upload_filename_entry.get()
        course = qb_upload_course_box.get()
        branch = qb_upload_branch_box.get()
        year = qb_upload_year_box.get()
        subject = qb_upload_subject_box.get()
        module = qb_upload_module_box.get()
        if all({file_name, course, branch, year, subject, module}):
            pdf_path = select_pdf_file()
            if pdf_path:
                with open(pdf_path, "rb") as f:
                    pdf_data = f.read()
                    storage.child(f"qbs/{course}/{branch}/{year}/{subject}/{module}/" + file_name).put(pdf_data)
                    print("PDF uploaded successfully!")
                    qb_upload_error_label.configure(text='PDF uploaded successfully!')
                    qb_upload_filename_entry.delete(0, END)
                    qb_upload_course_box.set("")
                    qb_upload_branch_box.set("")
                    qb_upload_year_box.set("")
                    qb_upload_subject_box.set("")
                    qb_upload_module_box.set("")
        else:
            qb_upload_error_label.configure(text='Fill all fields!')
        db.collection("qbData").add({
            "filename": file_name,
            "upvotes": 0,
            "uploadedBy": loggedInUser,
            "downloads": 0
        })


def select_destination_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path


def download_pdf(filename):
    pdf_ref = storage.child(f"{filename}")

    try:
        url = pdf_ref.get_url(None)
        response = requests.get(url)
        response.raise_for_status()
        destination_folder = select_destination_folder()
        os.makedirs(destination_folder, exist_ok=True)
        file_path = os.path.join(destination_folder, os.path.basename(filename) + ".pdf")

        with open(file_path, "wb") as f:
            f.write(response.content)

        print("PDF downloaded successfully to:", file_path)
    except requests.exceptions.RequestException as e:
        print("Error downloading PDF:", e)


def show_tabs(tab_name):
    menu_tabs.pack(expand=True, fill='both')
    main_menu.pack_forget()
    menu_tabs.set(tab_name)


def next_page(current_page, next_page_frame):
    current_page.pack_forget()
    next_page_frame.pack(expand=True, fill='both')


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
                global loggedInUser
                loggedInUser = username
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


def show_notes_filter_subjects(self):
    year = notes_search_year_box.get()
    table = []
    for item in CSE_subjects[year]:
        table.append(item)
    notes_search_subject_box.configure(values=table)
    notes_search_subject_box.set("")
    notes_search_module_box.set("")


def show_notes_upload_subjects(self):
    year = notes_upload_year_box.get()
    table = []
    for item in CSE_subjects[year]:
        table.append(item)
    notes_upload_subject_box.configure(values=table)
    notes_upload_subject_box.set("")
    notes_upload_module_box.set("")


def show_videos_filter_subjects(self):
    year = videos_search_year_box.get()
    table = []
    for item in CSE_subjects[year]:
        table.append(item)
    videos_search_subject_box.configure(values=table)
    videos_search_subject_box.set("")
    videos_search_module_box.set("")


def show_videos_upload_subjects(self):
    year = videos_upload_year_box.get()
    table = []
    for item in CSE_subjects[year]:
        table.append(item)
    videos_upload_subject_box.configure(values=table)
    videos_upload_subject_box.set("")
    videos_upload_module_box.set("")


def show_qb_filter_subjects(self):
    year = qb_search_year_box.get()
    table = []
    for item in CSE_subjects[year]:
        table.append(item)
    qb_search_subject_box.configure(values=table)
    qb_search_subject_box.set("")
    qb_search_module_box.set("")


def show_qb_upload_subjects(self):
    year = qb_upload_year_box.get()
    table = []
    for item in CSE_subjects[year]:
        table.append(item)
    qb_upload_subject_box.configure(values=table)
    qb_upload_subject_box.set("")
    qb_upload_module_box.set("")


def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.configure(show='*')
        show_password_box.configure(text='Show Password')
    else:
        password_entry.configure(show='')
        show_password_box.configure(text='Hide Password')


# Display Frame content

def display_note_menu(material_type):
    if material_type == 'notes':
        for frame in notes_display_frame.winfo_children():
            frame.destroy()
    elif material_type == 'videos':
        for frame in videos_display_frame.winfo_children():
            frame.destroy()
    elif material_type == 'qb':
        for frame in qb_display_frame.winfo_children():
            frame.destroy()
    for name in file_names:
        if material_type == 'notes':
            display_name = name.replace(current_notes_search_dir + "/", "")
            parent_frame = notes_display_frame
            frame = CTkFrame(master=parent_frame, height=100, fg_color='#e4e5f1')
            frame.pack(fill='x', pady=5)
            display_title = CTkLabel(master=frame, text=display_name, fg_color='transparent', font=("Arial Bold", 14),
                                     text_color='#1f61a5')
            display_title.pack(side=LEFT, pady=5, padx=5)
            display_download_button = CTkButton(master=frame, width=40, height=40, text='', image=download_img,
                                                command=lambda n=name: download_pdf(n))
            display_download_button.pack(side=RIGHT, pady=5, padx=5)
            display_upvote_button = CTkButton(master=frame, width=40, height=40, text='', fg_color='#D30000',
                                              hover_color='#7C0A02', image=upvote_img)
            display_upvote_button.pack(side=RIGHT, pady=5, padx=5)
        elif material_type == 'qb':
            display_name = name.replace(current_qb_search_dir + "/", "")
            parent_frame = qb_display_frame
            frame = CTkFrame(master=parent_frame, height=100, fg_color='#e4e5f1')
            frame.pack(fill='x', pady=5)
            display_title = CTkLabel(master=frame, text=display_name, fg_color='transparent', font=("Arial Bold", 14),
                                     text_color='#1f61a5')
            display_title.pack(side=LEFT, pady=5, padx=5)
            display_download_button = CTkButton(master=frame, width=40, height=40, text='', image=download_img,
                                                command=lambda n=name: download_pdf(n))
            display_download_button.pack(side=RIGHT, pady=5, padx=5)
            display_upvote_button = CTkButton(master=frame, width=40, height=40, text='', fg_color='#D30000',
                                              hover_color='#7C0A02', image=upvote_img)
            display_upvote_button.pack(side=RIGHT, pady=5, padx=5)
        elif material_type == 'videos':
            display_name = name.replace(current_videos_search_dir + "/", "")
            parent_frame = videos_display_frame
            frame = CTkFrame(master=parent_frame, height=100, fg_color='#e4e5f1')
            frame.pack(fill='x', pady=5)
            display_title = CTkLabel(master=frame, text=display_name, fg_color='transparent', font=("Arial Bold", 14),
                                     text_color='#1f61a5')
            display_title.pack(side=LEFT, pady=5, padx=5)
            display_download_button = CTkButton(master=frame, width=40, height=40, text='', image=download_img,
                                                command=lambda n=name: download_video(n)) #Add video download function here
            display_download_button.pack(side=RIGHT, pady=5, padx=5)
            display_upvote_button = CTkButton(master=frame, width=40, height=40, text='', fg_color='#D30000',
                                              hover_color='#7C0A02', image=upvote_img)
            display_upvote_button.pack(side=RIGHT, pady=5, padx=5)


def list_files_in_folder(folder_path):
    folder = bucket.list_blobs(prefix=folder_path)
    file_names = [blob.name for blob in folder if blob.name.endswith('/') == False]
    return file_names


def search_subjects(material_type):
    global file_names
    if material_type == 'notes':
        course = notes_search_course_box.get()
        branch = notes_search_branch_box.get()
        year = notes_search_year_box.get()
        subject = notes_search_subject_box.get()
        module = notes_search_module_box.get()
        if all({course, branch, year, subject, module}):
            folder_path = f"pdfs/{course}/{branch}/{year}/{subject}/{module}"
            global current_notes_search_dir
            current_notes_search_dir = folder_path
            notes_search_error_label.configure(text='')
            file_names = list_files_in_folder(current_notes_search_dir)
            display_note_menu(material_type)
        else:
            notes_search_error_label.configure(text='Set all fields!')
    elif material_type == 'qb':
        course = qb_search_course_box.get()
        branch = qb_search_branch_box.get()
        year = qb_search_year_box.get()
        subject = qb_search_subject_box.get()
        module = qb_search_module_box.get()
        if all({course, branch, year, subject, module}):
            folder_path = f"qbs/{course}/{branch}/{year}/{subject}/{module}"
            global current_qb_search_dir
            current_qb_search_dir = folder_path
            qb_search_error_label.configure(text='')
            file_names = list_files_in_folder(current_qb_search_dir)
            display_note_menu(material_type)
        else:
            notes_search_error_label.configure(text='Set all fields!')
    elif material_type == 'videos':
        course = videos_search_course_box.get()
        branch = videos_search_branch_box.get()
        year = videos_search_year_box.get()
        subject = videos_search_subject_box.get()
        module = videos_search_module_box.get()
        if all({course, branch, year, subject, module}):
            folder_path = f"videos/{course}/{branch}/{year}/{subject}/{module}"
            global current_videos_search_dir
            current_videos_search_dir = folder_path
            videos_search_error_label.configure(text='')
            file_names = list_files_in_folder(current_videos_search_dir)
            display_note_menu(material_type)
        else:
            notes_search_error_label.configure(text='Set all fields!')


def select_video_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', 1)
    root.update_idletasks()
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
    root.destroy()
    return file_path


def upload_video():
    file_name = videos_upload_filename_entry.get()
    course = videos_upload_course_box.get()
    branch = videos_upload_branch_box.get()
    year = videos_upload_year_box.get()
    subject = videos_upload_subject_box.get()
    module = videos_upload_module_box.get()
    if all({file_name, course, branch, year, subject, module}):
        video_path = select_video_file()
        if video_path:
            with open(video_path, "rb") as f:
                video_data = f.read()
                storage.child(f"videos/{course}/{branch}/{year}/{subject}/{module}/" + file_name).put(video_data)
                print("Video uploaded successfully!")
                videos_upload_error_label.configure(text="Video uploaded successfully!")
                db.collection("videoData").add({
                    "filename": file_name,
                    "upvotes": 0,
                    "uploadedBy": loggedInUser,  # remove the "" after testing
                    "downloads": 0
                })
                videos_upload_filename_entry.delete(0, END)
                videos_upload_course_box.set("")
                videos_upload_branch_box.set("")
                videos_upload_year_box.set("")
                videos_upload_subject_box.set("")
                videos_upload_module_box.set("")
        else:
            print("File selection canceled.")
    else:
        videos_upload_error_label.configure(text="Set all fields")
        print("Please provide all the required information.")


def download_video(filename):
    pdf_ref = storage.child(f"{filename}")

    try:
        url = pdf_ref.get_url(None)
        response = requests.get(url)
        response.raise_for_status()
        destination_folder = select_destination_folder()
        os.makedirs(destination_folder, exist_ok=True)
        file_path = os.path.join(destination_folder, os.path.basename(filename) + ".mp4")

        with open(file_path, "wb") as f:
            f.write(response.content)

        print("Video downloaded successfully to:", file_path)
    except requests.exceptions.RequestException as e:
        print("Error downloading Video:", e)


# GUI Code
# window

window = CTk(fg_color='#fafafa')
window.title('Study Material Repository')
window.geometry('800x500')
window.minsize(800, 500)
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
id_label.pack(anchor="w", pady=(20, 0), padx=(25, 0))
id_entry = CTkEntry(master=login_frame, width=225, fg_color="#EEEEEE", border_color="#1f61a5", border_width=1,
                    text_color="#000000")
id_entry.pack(anchor="w", padx=(25, 0))

password_label = CTkLabel(master=login_frame, text='  Password', text_color="#1f61a5", anchor="w", justify="left",
                          font=("Arial Bold", 14), image=password_img, compound="left")
password_label.pack(anchor="w", pady=(20, 0), padx=(25, 0))
password_entry = CTkEntry(master=login_frame, show='*', width=225, fg_color="#EEEEEE", border_color="#1f61a5",
                          border_width=1, text_color="#000000")
password_entry.pack(anchor="w", padx=(25, 0))
show_password_box = CTkCheckBox(master=login_frame, text="Show Password", border_width=1, checkbox_width=20,
                                checkbox_height=20, command=lambda: toggle_password())
show_password_box.pack(anchor="w", padx=(25, 0), pady=10)
error_label = CTkLabel(master=login_frame, text="", text_color="#FF0000")
error_label.pack(anchor="w", padx=(25, 0))

login_button = CTkButton(master=login_frame, text="Login", fg_color="#1f61a5", hover_color="#19429d",
                         font=("Arial Bold", 12), text_color="#ffffff", width=225, command=lambda: login())
login_button.pack(anchor="w", pady=(20, 0), padx=(25, 0))

# Main Menu
main_menu = CTkFrame(master=window)

# Buttons menu
main_menu_title = CTkLabel(master=main_menu, text="Choose Tab")
main_menu_title.pack()

buttons_menu = CTkFrame(master=main_menu)
buttons_menu.pack(pady=20)

notes_button = CTkButton(master=buttons_menu, text='Notes', command=lambda: show_tabs('Notes'))
notes_button.pack(pady=20, padx=15)
qb_button = CTkButton(master=buttons_menu, text='Question Banks', command=lambda: show_tabs('Question Banks'))
qb_button.pack(pady=20, padx=15)
videos_button = CTkButton(master=buttons_menu, text='Videos', command=lambda: show_tabs('Videos'))
videos_button.pack(pady=20, padx=15)
qna_button = CTkButton(master=buttons_menu, text='Q & A', command=lambda: show_tabs('Q & A'))
qna_button.pack(pady=20, padx=15)

# Tabs
menu_tabs = CTkTabview(master=window, fg_color='#fafafa', segmented_button_fg_color='#fafafa')

notes_tab = menu_tabs.add('Notes')
qb_tab = menu_tabs.add('Question Banks')
video_tab = menu_tabs.add('Videos')
qna_tab = menu_tabs.add('Q & A')

# Notes tab

notes_filter_menu_frame = CTkFrame(master=notes_tab, width=200, border_color='#484b6a', fg_color='#e4e5f1')
notes_filter_menu_frame.pack(side='left', fill='y')
notes_upload_menu_frame = CTkFrame(master=notes_tab, width=200, border_color='#484b6a', fg_color='#e4e5f1')
notes_upload_menu_frame.pack(side='right', fill='y')
notes_display_frame = CTkScrollableFrame(master=notes_tab, fg_color='#fafafa', scrollbar_button_color='#d2d3db')
notes_display_frame.pack(side='left', expand=True, fill='both')

filter_course_table = ['B.Tech']
filter_branch_table = ['CSE', 'Other']
filter_year_table = ['1st year', '2nd year', '3rd year', '4th year']
filter_subject_table = ['']
filter_module_table = ['1', '2', '3', '4', '5']

notes_filter_menu_title = CTkLabel(master=notes_filter_menu_frame, text='Filter', text_color='#1f61a5', anchor='w',
                                   justify='left', font=("Arial Bold", 18))
notes_filter_menu_title.pack(padx=10)
notes_search_course_label = CTkLabel(master=notes_filter_menu_frame, text='Course', width=200)
notes_search_course_label.pack(padx=10)
notes_search_course_box = CTkComboBox(master=notes_filter_menu_frame, border_color="#1f61a5",
                                      border_width=1, values=filter_course_table, state='readonly')
notes_search_course_box.pack(padx=10)
notes_search_branch_label = CTkLabel(master=notes_filter_menu_frame, text='Branch', width=200)
notes_search_branch_label.pack(padx=10)
notes_search_branch_box = CTkComboBox(master=notes_filter_menu_frame, border_color="#1f61a5",
                                      border_width=1, values=filter_branch_table, state='readonly')
notes_search_branch_box.pack(padx=10)
notes_search_year_label = CTkLabel(master=notes_filter_menu_frame, text='Year', width=200)
notes_search_year_label.pack(padx=10)
notes_search_year_box = CTkComboBox(master=notes_filter_menu_frame, border_color="#1f61a5",
                                    border_width=1, values=filter_year_table, state='readonly',
                                    command=show_notes_filter_subjects)
notes_search_year_box.pack(padx=10)
notes_search_subject_label = CTkLabel(master=notes_filter_menu_frame, text='Subject', width=200)
notes_search_subject_label.pack(padx=10)
notes_search_subject_box = CTkComboBox(master=notes_filter_menu_frame, border_color="#1f61a5",
                                       border_width=1, values=filter_subject_table, state='readonly')
notes_search_subject_box.pack(padx=10)
notes_search_module_label = CTkLabel(master=notes_filter_menu_frame, text='Module', width=200)
notes_search_module_label.pack(padx=10)
notes_search_module_box = CTkComboBox(master=notes_filter_menu_frame, border_color="#1f61a5",
                                      border_width=1, values=filter_module_table, state='readonly')
notes_search_module_box.pack(padx=10)
notes_search_button = CTkButton(master=notes_filter_menu_frame, text='  Search', image=search_img,
                                command=lambda: search_subjects('notes'))
notes_search_button.pack(pady=10)
notes_search_error_label = CTkLabel(master=notes_filter_menu_frame, text='', text_color="#FF0000")
notes_search_error_label.pack()

upload_course_table = ['B.Tech']
upload_branch_table = ['CSE', 'Other']
upload_year_table = ['1st year', '2nd year', '3rd year', '4th year']
upload_subject_table = ['']
upload_module_table = ['1', '2', '3', '4', '5']

notes_upload_menu_title = CTkLabel(master=notes_upload_menu_frame, text='Upload', text_color='#1f61a5', anchor='w',
                                   justify='left', font=("Arial Bold", 18))
notes_upload_menu_title.pack(padx=10)
notes_upload_filename_label = CTkLabel(master=notes_upload_menu_frame, text='File name', width=200)
notes_upload_filename_label.pack()
notes_upload_filename_entry = CTkEntry(master=notes_upload_menu_frame, border_color="#1f61a5",
                                       border_width=1, )
notes_upload_filename_entry.pack()
notes_upload_course_label = CTkLabel(master=notes_upload_menu_frame, text='Course', width=200)
notes_upload_course_label.pack(padx=10)
notes_upload_course_box = CTkComboBox(master=notes_upload_menu_frame, border_color="#1f61a5",
                                      border_width=1, state='readonly', values=upload_course_table)
notes_upload_course_box.pack(padx=10)
notes_upload_branch_label = CTkLabel(master=notes_upload_menu_frame, text='Branch', width=200)
notes_upload_branch_label.pack(padx=10)
notes_upload_branch_box = CTkComboBox(master=notes_upload_menu_frame, border_color="#1f61a5",
                                      border_width=1, state='readonly', values=upload_branch_table)
notes_upload_branch_box.pack(padx=10)
notes_upload_year_label = CTkLabel(master=notes_upload_menu_frame, text='Year', width=200)
notes_upload_year_label.pack(padx=10)
notes_upload_year_box = CTkComboBox(master=notes_upload_menu_frame, border_color="#1f61a5",
                                    border_width=1, values=upload_year_table, state='readonly',
                                    command=show_notes_upload_subjects)
notes_upload_year_box.pack(padx=10)
notes_upload_subject_label = CTkLabel(master=notes_upload_menu_frame, text='Subject', width=200)
notes_upload_subject_label.pack(padx=10)
notes_upload_subject_box = CTkComboBox(master=notes_upload_menu_frame, border_color="#1f61a5",
                                       border_width=1, state='readonly', values=upload_subject_table)
notes_upload_subject_box.pack(padx=10)
notes_upload_module_label = CTkLabel(master=notes_upload_menu_frame, text='Module', width=200)
notes_upload_module_label.pack(padx=10)
notes_upload_module_box = CTkComboBox(master=notes_upload_menu_frame, border_color="#1f61a5",
                                      border_width=1, state='readonly', values=upload_module_table)
notes_upload_module_box.pack(padx=10)
notes_upload_button = CTkButton(master=notes_upload_menu_frame, text='  Upload', image=upload_img,
                                command=lambda: upload_pdf_using_dialog('notes'))
notes_upload_button.pack(pady=10)
notes_upload_error_label = CTkLabel(master=notes_upload_menu_frame, text='', text_color="#FF0000")
notes_upload_error_label.pack()


# qb tab
qb_filter_menu_frame = CTkFrame(master=qb_tab, width=200, border_color='#484b6a', fg_color='#e4e5f1')
qb_filter_menu_frame.pack(side='left', fill='y')
qb_upload_menu_frame = CTkFrame(master=qb_tab, width=200, border_color='#484b6a', fg_color='#e4e5f1')
qb_upload_menu_frame.pack(side='right', fill='y')
qb_display_frame = CTkScrollableFrame(master=qb_tab, fg_color='#fafafa', scrollbar_button_color='#d2d3db')
qb_display_frame.pack(side='left', expand=True, fill='both')

filter_course_table = ['B.Tech']
filter_branch_table = ['CSE', 'Other']
filter_year_table = ['1st year', '2nd year', '3rd year', '4th year']
filter_subject_table = ['']
filter_module_table = ['1', '2', '3', '4', '5']

qb_filter_menu_title = CTkLabel(master=qb_filter_menu_frame, text='Filter', text_color='#1f61a5', anchor='w',
                                    justify='left', font=("Arial Bold", 18))
qb_filter_menu_title.pack(padx=10)
qb_search_course_label = CTkLabel(master=qb_filter_menu_frame, text='Course', width=200)
qb_search_course_label.pack(padx=10)
qb_search_course_box = CTkComboBox(master=qb_filter_menu_frame, border_color="#1f61a5",
                                       border_width=1, values=filter_course_table, state='readonly')
qb_search_course_box.pack(padx=10)
qb_search_branch_label = CTkLabel(master=qb_filter_menu_frame, text='Branch', width=200)
qb_search_branch_label.pack(padx=10)
qb_search_branch_box = CTkComboBox(master=qb_filter_menu_frame, border_color="#1f61a5",
                                       border_width=1, values=filter_branch_table, state='readonly')
qb_search_branch_box.pack(padx=10)
qb_search_year_label = CTkLabel(master=qb_filter_menu_frame, text='Year', width=200)
qb_search_year_label.pack(padx=10)
qb_search_year_box = CTkComboBox(master=qb_filter_menu_frame, border_color="#1f61a5",
                                     border_width=1, values=filter_year_table, state='readonly',
                                     command=show_qb_filter_subjects)
qb_search_year_box.pack(padx=10)
qb_search_subject_label = CTkLabel(master=qb_filter_menu_frame, text='Subject', width=200)
qb_search_subject_label.pack(padx=10)
qb_search_subject_box = CTkComboBox(master=qb_filter_menu_frame, border_color="#1f61a5",
                                        border_width=1, values=filter_subject_table, state='readonly')
qb_search_subject_box.pack(padx=10)
qb_search_module_label = CTkLabel(master=qb_filter_menu_frame, text='Module', width=200)
qb_search_module_label.pack(padx=10)
qb_search_module_box = CTkComboBox(master=qb_filter_menu_frame, border_color="#1f61a5",
                                       border_width=1, values=filter_module_table, state='readonly')
qb_search_module_box.pack(padx=10)
qb_search_button = CTkButton(master=qb_filter_menu_frame, text='  Search', image=search_img,
                                 command=lambda: search_subjects('qb'))
qb_search_button.pack(pady=10)
qb_search_error_label = CTkLabel(master=qb_filter_menu_frame, text='', text_color="#FF0000")
qb_search_error_label.pack()

upload_course_table = ['B.Tech']
upload_branch_table = ['CSE', 'Other']
upload_year_table = ['1st year', '2nd year', '3rd year', '4th year']
upload_subject_table = ['']
upload_module_table = ['1', '2', '3', '4', '5']

qb_upload_menu_title = CTkLabel(master=qb_upload_menu_frame, text='Upload', text_color='#1f61a5', anchor='w',
                                    justify='left', font=("Arial Bold", 18))
qb_upload_menu_title.pack(padx=10)
qb_upload_filename_label = CTkLabel(master=qb_upload_menu_frame, text='File name', width=200)
qb_upload_filename_label.pack()
qb_upload_filename_entry = CTkEntry(master=qb_upload_menu_frame, border_color="#1f61a5",
                                        border_width=1, )
qb_upload_filename_entry.pack()
qb_upload_course_label = CTkLabel(master=qb_upload_menu_frame, text='Course', width=200)
qb_upload_course_label.pack(padx=10)
qb_upload_course_box = CTkComboBox(master=qb_upload_menu_frame, border_color="#1f61a5",
                                       border_width=1, state='readonly', values=upload_course_table)
qb_upload_course_box.pack(padx=10)
qb_upload_branch_label = CTkLabel(master=qb_upload_menu_frame, text='Branch', width=200)
qb_upload_branch_label.pack(padx=10)
qb_upload_branch_box = CTkComboBox(master=qb_upload_menu_frame, border_color="#1f61a5",
                                       border_width=1, state='readonly', values=upload_branch_table)
qb_upload_branch_box.pack(padx=10)
qb_upload_year_label = CTkLabel(master=qb_upload_menu_frame, text='Year', width=200)
qb_upload_year_label.pack(padx=10)
qb_upload_year_box = CTkComboBox(master=qb_upload_menu_frame, border_color="#1f61a5",
                                     border_width=1, values=upload_year_table, state='readonly',
                                     command=show_qb_upload_subjects)
qb_upload_year_box.pack(padx=10)
qb_upload_subject_label = CTkLabel(master=qb_upload_menu_frame, text='Subject', width=200)
qb_upload_subject_label.pack(padx=10)
qb_upload_subject_box = CTkComboBox(master=qb_upload_menu_frame, border_color="#1f61a5",
                                        border_width=1, state='readonly', values=upload_subject_table)
qb_upload_subject_box.pack(padx=10)
qb_upload_module_label = CTkLabel(master=qb_upload_menu_frame, text='Module', width=200)
qb_upload_module_label.pack(padx=10)
qb_upload_module_box = CTkComboBox(master=qb_upload_menu_frame, border_color="#1f61a5",
                                       border_width=1, state='readonly', values=upload_module_table)
qb_upload_module_box.pack(padx=10)
qb_upload_button = CTkButton(master=qb_upload_menu_frame, text='  Upload', image=upload_img,
                                 command=lambda: upload_pdf_using_dialog('qb'))
qb_upload_button.pack(pady=10)
qb_upload_error_label = CTkLabel(master=qb_upload_menu_frame, text='', text_color="#FF0000")
qb_upload_error_label.pack()


# videos tab
videos_filter_menu_frame = CTkFrame(master=video_tab, width=200, border_color='#484b6a', fg_color='#e4e5f1')
videos_filter_menu_frame.pack(side='left', fill='y')
videos_upload_menu_frame = CTkFrame(master=video_tab, width=200, border_color='#484b6a', fg_color='#e4e5f1')
videos_upload_menu_frame.pack(side='right', fill='y')
videos_display_frame = CTkScrollableFrame(master=video_tab, fg_color='#fafafa', scrollbar_button_color='#d2d3db')
videos_display_frame.pack(side='left', expand=True, fill='both')

filter_course_table = ['B.Tech']
filter_branch_table = ['CSE', 'Other']
filter_year_table = ['1st year', '2nd year', '3rd year', '4th year']
filter_subject_table = ['']
filter_module_table = ['1', '2', '3', '4', '5']

videos_filter_menu_title = CTkLabel(master=videos_filter_menu_frame, text='Filter', text_color='#1f61a5', anchor='w',
                                    justify='left', font=("Arial Bold", 18))
videos_filter_menu_title.pack(padx=10)
videos_search_course_label = CTkLabel(master=videos_filter_menu_frame, text='Course', width=200)
videos_search_course_label.pack(padx=10)
videos_search_course_box = CTkComboBox(master=videos_filter_menu_frame, border_color="#1f61a5",
                                       border_width=1, values=filter_course_table, state='readonly')
videos_search_course_box.pack(padx=10)
videos_search_branch_label = CTkLabel(master=videos_filter_menu_frame, text='Branch', width=200)
videos_search_branch_label.pack(padx=10)
videos_search_branch_box = CTkComboBox(master=videos_filter_menu_frame, border_color="#1f61a5",
                                       border_width=1, values=filter_branch_table, state='readonly')
videos_search_branch_box.pack(padx=10)
videos_search_year_label = CTkLabel(master=videos_filter_menu_frame, text='Year', width=200)
videos_search_year_label.pack(padx=10)
videos_search_year_box = CTkComboBox(master=videos_filter_menu_frame, border_color="#1f61a5",
                                     border_width=1, values=filter_year_table, state='readonly',
                                     command=show_videos_filter_subjects)
videos_search_year_box.pack(padx=10)
videos_search_subject_label = CTkLabel(master=videos_filter_menu_frame, text='Subject', width=200)
videos_search_subject_label.pack(padx=10)
videos_search_subject_box = CTkComboBox(master=videos_filter_menu_frame, border_color="#1f61a5",
                                        border_width=1, values=filter_subject_table, state='readonly')
videos_search_subject_box.pack(padx=10)
videos_search_module_label = CTkLabel(master=videos_filter_menu_frame, text='Module', width=200)
videos_search_module_label.pack(padx=10)
videos_search_module_box = CTkComboBox(master=videos_filter_menu_frame, border_color="#1f61a5",
                                       border_width=1, values=filter_module_table, state='readonly')
videos_search_module_box.pack(padx=10)
videos_search_button = CTkButton(master=videos_filter_menu_frame, text='  Search', image=search_img,
                                 command=lambda: search_subjects('videos'))
videos_search_button.pack(pady=10)
videos_search_error_label = CTkLabel(master=videos_filter_menu_frame, text='', text_color="#FF0000")
videos_search_error_label.pack()

upload_course_table = ['B.Tech']
upload_branch_table = ['CSE', 'Other']
upload_year_table = ['1st year', '2nd year', '3rd year', '4th year']
upload_subject_table = ['']
upload_module_table = ['1', '2', '3', '4', '5']

videos_upload_menu_title = CTkLabel(master=videos_upload_menu_frame, text='Upload', text_color='#1f61a5', anchor='w',
                                    justify='left', font=("Arial Bold", 18))
videos_upload_menu_title.pack(padx=10)
videos_upload_filename_label = CTkLabel(master=videos_upload_menu_frame, text='File name', width=200)
videos_upload_filename_label.pack()
videos_upload_filename_entry = CTkEntry(master=videos_upload_menu_frame, border_color="#1f61a5",
                                        border_width=1, )
videos_upload_filename_entry.pack()
videos_upload_course_label = CTkLabel(master=videos_upload_menu_frame, text='Course', width=200)
videos_upload_course_label.pack(padx=10)
videos_upload_course_box = CTkComboBox(master=videos_upload_menu_frame, border_color="#1f61a5",
                                       border_width=1, state='readonly', values=upload_course_table)
videos_upload_course_box.pack(padx=10)
videos_upload_branch_label = CTkLabel(master=videos_upload_menu_frame, text='Branch', width=200)
videos_upload_branch_label.pack(padx=10)
videos_upload_branch_box = CTkComboBox(master=videos_upload_menu_frame, border_color="#1f61a5",
                                       border_width=1, state='readonly', values=upload_branch_table)
videos_upload_branch_box.pack(padx=10)
videos_upload_year_label = CTkLabel(master=videos_upload_menu_frame, text='Year', width=200)
videos_upload_year_label.pack(padx=10)
videos_upload_year_box = CTkComboBox(master=videos_upload_menu_frame, border_color="#1f61a5",
                                     border_width=1, values=upload_year_table, state='readonly',
                                     command=show_videos_upload_subjects)
videos_upload_year_box.pack(padx=10)
videos_upload_subject_label = CTkLabel(master=videos_upload_menu_frame, text='Subject', width=200)
videos_upload_subject_label.pack(padx=10)
videos_upload_subject_box = CTkComboBox(master=videos_upload_menu_frame, border_color="#1f61a5",
                                        border_width=1, state='readonly', values=upload_subject_table)
videos_upload_subject_box.pack(padx=10)
videos_upload_module_label = CTkLabel(master=videos_upload_menu_frame, text='Module', width=200)
videos_upload_module_label.pack(padx=10)
videos_upload_module_box = CTkComboBox(master=videos_upload_menu_frame, border_color="#1f61a5",
                                       border_width=1, state='readonly', values=upload_module_table)
videos_upload_module_box.pack(padx=10)
videos_upload_button = CTkButton(master=videos_upload_menu_frame, text='  Upload', image=upload_img,
                                 command=lambda: upload_video())
videos_upload_button.pack(pady=10)
videos_upload_error_label = CTkLabel(master=videos_upload_menu_frame, text='', text_color="#FF0000")
videos_upload_error_label.pack()

# run
window.mainloop()
