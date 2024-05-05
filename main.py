import tkinter as tk
import firebase_admin
import pyrebase
import requests
from PIL import Image
from customtkinter import *
from firebase_admin import credentials, firestore, storage

cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "study-material-repo",
    "private_key_id": "72965ed62fea3b57a31aad84dd730b0c75e3f462",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDYFifzg95n7akc\nVMpAD/TYcVQGmHrpWvhBvWIJj/NVXD3NzX1WcmNVGvIIKTdrANJzljw7/udt7OLO\nkV90wnsB3Ki8n3AhhxvVy0tOR6WN9esSj2cKY8JqG/JzUGB1RlSL4EVF6lt+EuXz\n8w76n13YT33NlUvKmEo/akRJmUPAm1aiqXly144sn7n8N61Ys7s5s0l0RbRJ4qWB\n557W3ArkA5zdg/hQgM+OB6t957SWOqDEREYBK/tLOgfIs6giT0P3W/T6wBlY3nbj\nEWxRJbHCFauQ7FsBUrXAJfKeXtYgpcoKfdp/RUE2W2q+Y9ps91+4ZEJf+E1GfA1r\nkBGKKr3NAgMBAAECggEALVQif9UJDeSfPbv0rFEck93cGkEYwYRtgP7dBrP9f8nI\nhjhFw2FeAH+VR4x73VSwEQKyMoSzoA3Z+yqoK0pTuu2CsQTCJSpeNrA9ZRem/TtZ\n20wdOaL5KMChkLqK7Xb6K9h5N6QkmrMUrWKuoPjW2xY7xek8W6ysIJbmacj+mzOn\n4HuR+Ok1yNdGkqvgCT3BkNmTD3MCZMcXWE2hnxxQ5VzZIiAGfVN8ud3ZYxh+2XjC\nW2TG0fQko6aS487X702wSuUyf60Fu5rm+uNHqmu3jobGrtCOck8j3Gm07RHHGpEY\nqr3v+iDGwUz9YRRCkrx3CqsPARdNaebfAaj+lCfqMQKBgQD8l80zWTj3il09/DwH\nv2QzQmoM7q6pG9gPqvWb0L9jhmD2dYZUVd/NQW1ef+4mUeMRWBAtC1TTHUo9f/HE\nu15AxBxZIaGLageYr7beOtHSR/lETmkcHwcI4tFg1fpe2wjXOd5h965c8uV/CyGe\ncnJqT7VoxHzY0WDxNMC35iwa3QKBgQDbAExs+OTY6ka0JNg9SQURg6xu8Wo5rSZv\njAq6bd2tOTUqpTbk30LFR7orwRS4cKPRPvEuy0hGR6OqdBNIJRb/fjVa6LDi6vpB\ni0rUEkU37Y5uY9qsDt5Z/DLMV2ZR9TeDqcW/USjVQz8f19GkkcdmDjlPQ0bvA4/z\naOV6H16nsQKBgD8T8Yx3JYC7rtlB2gPdSbp7RVyBZmCYsXYILVmB4amK7z/czXTW\nFRN+2T8WF3S+UkQMh82X3NDzqYx+HPQSDlGCJ8oiWeMk0UzR5IrOiYNHsfna0ujQ\n3sLbUYorJWD2tdh5fQ1d+s7/YUw+jWCyF9xwl07Ycoz6jIjvsYi7FByJAoGBANSE\ntKVm3kS1C4mS25iVPGrjmThL42Y25b6Han3BUcXgZvyMOPnewd/JnBsLkjztabsL\nVmavc+JncKZfX7q561hhtAsVFVoO5m0ma6XiWPNN/tKW6cPf5dvyxaTQB4Xu7UFC\nRZhDfNl/GUmgWFtX7+TUVr7ZLYORtGZj25QnzuXxAoGActiJG3xd5wMC+M+aST5b\nVwVxZYZ0MwsLG+inR9j8K4W66tj4NV4Spw5855WP9dnapLFf8JDtkk1KrKhnbT8j\nUSffMHoWUCjX9F73NkVYGRR/qyvXTeyV0jjGErgbNMIpNTweRopIsD1SyZo8cCOC\nynuhkACNWezhuLyT7KDAf80=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-bj0om@study-material-repo.iam.gserviceaccount.com",
    "client_id": "103543428192303652993",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-bj0om%40study-material-repo.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
})
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

script_directory = os.path.dirname(os.path.realpath(__file__))
images_directory = os.path.join(script_directory, 'Images')

if not os.path.exists(images_directory):
    # print("Error: Images directory not found.")
    raise FileNotFoundError()

os.chdir(script_directory)

CSE_subjects = {
    '1st year': ['Engineering Physics A - PHT 100', 'Engineering Physics B - PHT 110',
                 'Linear Algebra and Calculus - MAT 101', 'Engineering Mechanics - EST 100',
                 'Basics of Civil and Mechanical Engineering - EST 120', 'Life Skills - HUT 101',
                 'Engineering Chemistry - CYT 100', 'Engineering Graphics - EST 110',
                 'Vector Calculus, Differential Equations and Transforms - MAT 102',
                 'Programming in C - EST 102', 'Basics of Electrical and Electronics Engineering - EST 130',
                 'Professionsal Communication - HUT 102'],
    '2nd year': ['Discrete Mathematical Structures - MAT 203', 'Data Structures - CST 201',
                 'Logic System Design - CST 203', 'Sustainable Engineering - MNC 202',
                 'Design and Engineering - EST 200', 'Professional Ethics - HUT 200',
                 'Object Oriented Programming Using Java - CST 205', 'Graph Theory - MAT 206',
                 'Computer Organization and Architecture - CST 202', 'Database Management System - CST 204',
                 'Operating System - CST 206', 'Constitution of India - MNC 202'],
    '3rd year': ['Computer Networks - CST 303', 'System Software - CST 305',
                 'Microprocessors and Microcontrollers - CST 307', 'Management of Software Systems - CST 309',
                 'Disaster Management - MCN 301', 'Formal Languages and Automata Theory - CST 301',
                 'Compiler Design - CST 302', 'Computer Graphics and Image Processing - CST 304',
                 'Algorithm Analysis and Design - CST 306',
                 'Data Analytics - CST 322', 'Foundations of Security in Computing - CST 332',
                 'Industrial Economics and Foreign Trade - HUT 300'],
    '4th year': [''],
}

img_dir = os.path.abspath(os.path.join(os.getcwd(), 'Images'))

user_img_data = Image.open(os.path.join(img_dir, 'User1.png'))
password_img_data = Image.open(os.path.join(img_dir, 'password1.png'))
side_img_data = Image.open(os.path.join(img_dir, 'bg.png'))
logo_img_data = Image.open(os.path.join(img_dir, 'logo.png'))
search_img_data = Image.open(os.path.join(img_dir, 'search.png'))
upload_img_data = Image.open(os.path.join(img_dir, 'upload.png'))
upvote_img_data = Image.open(os.path.join(img_dir, 'upvote.png'))
downvote_img_data = Image.open(os.path.join(img_dir, 'downvote.png'))
download_img_data = Image.open(os.path.join(img_dir, 'download.png'))

user_img = CTkImage(dark_image=user_img_data, light_image=user_img_data, size=(17, 17))
password_img = CTkImage(dark_image=password_img_data, light_image=password_img_data, size=(17, 17))
side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(400, 400))
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(50, 50))
search_img = CTkImage(dark_image=search_img_data, light_image=search_img_data, size=(17, 17))
upload_img = CTkImage(dark_image=upload_img_data, light_image=upload_img_data, size=(17, 17))
upvote_img = CTkImage(dark_image=upvote_img_data, light_image=upvote_img_data, size=(17, 17))
downvote_img = CTkImage(dark_image=downvote_img_data, light_image=downvote_img_data, size=(17, 17))
download_img = CTkImage(dark_image=download_img_data, light_image=download_img_data, size=(17, 17))

current_search_dir = ''
current_notes_search_dir = ''
current_videos_search_dir = ''
current_qb_search_dir = ''
notes_file_names_teacher = []
notes_file_names_student = []
qb_file_names_teacher = []
qb_file_names_student = []
videos_file_names_teacher = []
videos_file_names_student = []
file_names = []
admin_logged = False

loggedInUser = ''
loggedInUserID = ''
current_user_type = ''

collection_ref = db.collection('qna')
dict_ids = {}
dict_qns = {}
list_qns = []
a = {}
r = 0
current_q = ""


def upvote_ans(id,up_count_display,down_count_display):
    doc_ref = db.collection('answerData').document(id)
    user_doc_ref = db.collection('userCollection').document(loggedInUserID)
    user_doc = user_doc_ref.get()
    if 'upvotedAns' in user_doc.to_dict():
        new_value = str(id)
        upvoted_array_field = user_doc.to_dict()['upvotedAns']
        downvoted_array_field = user_doc.to_dict()['downvotedAns']
        if new_value in upvoted_array_field:
            upvoted_array_field.remove(new_value)
            new_upvotes = doc_ref.get().to_dict().get('upvotes', 0) - 1
            new_downvotes = doc_ref.get().to_dict().get('downvotes', 0)
        else:
            if new_value in downvoted_array_field:
                downvoted_array_field.remove(new_value)
                new_downvotes = doc_ref.get().to_dict().get('downvotes', 0) - 1
            else:
                new_downvotes = doc_ref.get().to_dict().get('downvotes', 0)
            upvoted_array_field.append(new_value)
            new_upvotes = doc_ref.get().to_dict().get('upvotes', 0) + 1
        user_doc_ref.update({'upvotedAns': upvoted_array_field, 'downvotedAns': downvoted_array_field})
        doc_ref.update({'upvotes': new_upvotes, 'downvotes': new_downvotes})
        up_count_display.configure(text=str(new_upvotes))
        down_count_display.configure(text=str(new_downvotes))


def downvote_ans(id,up_count_display,down_count_display):
    doc_ref = db.collection('answerData').document(id)
    user_doc_ref = db.collection('userCollection').document(loggedInUserID)
    user_doc = user_doc_ref.get()
    if 'downvotedAns' in user_doc.to_dict():
        new_value = str(id)
        downvoted_array_field = user_doc.to_dict()['downvotedAns']
        upvoted_array_field = user_doc.to_dict()['upvotedAns']
        if new_value in downvoted_array_field:
            downvoted_array_field.remove(new_value)
            new_downvotes = doc_ref.get().to_dict().get('downvotes', 0) - 1
            new_upvotes = doc_ref.get().to_dict().get('upvotes', 0)
        else:
            if new_value in upvoted_array_field:
                upvoted_array_field.remove(new_value)
                new_upvotes = doc_ref.get().to_dict().get('upvotes', 0) - 1
            else:
                new_upvotes = doc_ref.get().to_dict().get('upvotes', 0)
            downvoted_array_field.append(new_value)
            new_downvotes = doc_ref.get().to_dict().get('downvotes', 0) + 1
        user_doc_ref.update({'upvotedAns': upvoted_array_field, 'downvotedAns': downvoted_array_field})
        doc_ref.update({'upvotes': new_upvotes, 'downvotes': new_downvotes})
        up_count_display.configure(text=str(new_upvotes))
        down_count_display.configure(text=str(new_downvotes))


def empty_frame(frame):  # Empties a frame
    for widget in frame.winfo_children():
        widget.destroy()


# Example usage
def answer_gui(rframe):  # function to show answer in GUI....needs modification
    dialog = CTkInputDialog(text="Enter data:", title="Test")
    data = dialog.get_input()
    if data:
        CTkLabel(master=rframe)


def getqns():  # gets qns and stores them in dict_qns and list_qns..dictids has id and serial number
    qns = collection_ref.stream()
    query = collection_ref.get()
    document_ids = [doc.id for doc in query]
    i = 0
    for qn_doc in qns:
        qn_data = qn_doc.to_dict()

        question = qn_data.get('qn', '')
        dict_qns[document_ids[i]] = question
        dict_ids[i + 1] = document_ids[i]
        i += 1
        list_qns.append(question)


def post_qn(q):  # posts qn into firebase
    doc_ref = db.collection('qna').document()
    doc_ref.set({'qn': q, 'ans': ''})
    getqns()


def get_ans(id):  # gets answer from firebase based on doc id...returns as list
    # print(id)
    doc_ref = db.collection('qna').document(id)
    ans_snapshot = doc_ref.get()
    if ans_snapshot.exists:
        try:
            data = ans_snapshot.get('ans')
            if data and isinstance(data, list):
                '''for answer in data:
                    print(answer)'''
                return (data)
        except KeyError:
            print("Error")  # Show error in frame
    else:
        print('failed')
        return []


def answer_qn():  # Answer a qn
    c = current_q
    for i in dict_ids:
        if dict_ids[i] == c:
            ID = dict_ids[i]
            break
    a = get_ans(ID)
    answer = ranstextbox.get()
    ranstextbox.delete(0, END)
    empty_frame(raframe)
    ans_doc_ref = db.collection('answerData').document()
    ans_doc_ref.set(
        {
            'uploadedBy': loggedInUser,
            'ans': answer,
            'upvotes': 0,
            'downvotes': 0
        }
    )
    if a == None:
        a = [ans_doc_ref.id]
    else:
        a.append(ans_doc_ref.id)
    q_doc_ref = db.collection('qna').document(ID)
    q_doc_ref.update({'ans': a})
    for i in a:
        doc_ref = db.collection('answerData').document(i)
        doc = doc_ref.get()
        ans = doc.to_dict()['ans']
        name = doc.to_dict()['uploadedBy']
        upvotes = doc.to_dict()['upvotes']
        downvotes = doc.to_dict()['downvotes']
        message_frame = CTkFrame(master=raframe, fg_color='#e4e5f1')
        message_frame.pack(padx=5, pady=5, side=TOP, anchor=NW)
        message_text_frame = CTkFrame(master=message_frame, fg_color='#e4e5f1')
        message_text_frame.pack(padx=5, pady=5, side='left')
        CTkLabel(master=message_text_frame, text=name, font=('Arial Bold', 12), text_color='#1f61a5').pack(
            side=TOP, anchor=NW)
        CTkLabel(master=message_text_frame, font=('Arial Bold', 10), text=ans).pack(side='left', anchor=NW)
        message_downvote_frame = CTkFrame(master=message_frame, fg_color='#e4e5f1')
        message_upvote_frame = CTkFrame(master=message_frame, fg_color='#e4e5f1')
        message_downvote_frame.pack(side='right', padx=10, pady=5)
        upvote_count_display = CTkLabel(master=message_upvote_frame, text=upvotes, font=('Arial Bold', 10),
                                        text_color='#1f61a5')
        downvote_count_display = CTkLabel(master=message_downvote_frame, text=downvotes, font=('Arial Bold', 10),
                                          text_color='#1f61a5')
        CTkButton(master=message_downvote_frame, width=20, height=20, text='', hover_color='#7C0A02',
                  image=downvote_img, command=lambda id=i, upcount_display=upvote_count_display,
                                                     downcount_display=downvote_count_display: downvote_ans(i,
                                                                                                            upcount_display,
                                                                                                            downcount_display)).pack(
            side=TOP)

        downvote_count_display.pack(side=BOTTOM)
        message_upvote_frame.pack(side='right', padx=10, pady=5)
        CTkButton(master=message_upvote_frame, width=20, height=20, text='', hover_color='#7C0A02',
                  image=upvote_img, command=lambda id=i, upcount_display=upvote_count_display,
                                                   downcount_display=downvote_count_display: upvote_ans(id,
                                                                                                        upcount_display,
                                                                                                        downcount_display)).pack(
            side=TOP)
        upvote_count_display.pack(side=BOTTOM)

    # print(ans)'''


def fetch_data(qn, i):  # fetches data to put in rframe..qns and answers
    # print(rframe)
    # print(qn)
    scrolling_frame_1.pack_forget()
    post_button.pack_forget()
    back_button_frame.pack(fill="x")
    rframe.pack(side='right', fill='both', expand=True)
    empty_frame(raframe)
    global current_q
    for id, q in dict_qns.items():
        # print(id,q)
        if q == qn:
            current_q = id
            break
    rqframe.configure(text=qn)
    ans = get_ans(id)
    if ans is None:
        CTkLabel(master=raframe, text='No Answer Yet', text_color='#ff0000', anchor='e').pack(padx=10, pady=10)
    else:
        for i in ans:
            doc_ref = db.collection('answerData').document(i)
            doc = doc_ref.get()
            ans = doc.to_dict()['ans']
            name = doc.to_dict()['uploadedBy']
            upvotes = doc.to_dict()['upvotes']
            downvotes = doc.to_dict()['downvotes']
            message_frame = CTkFrame(master=raframe, fg_color='#e4e5f1')
            message_frame.pack(padx=5, pady=5, side=TOP, anchor=NW)
            message_text_frame = CTkFrame(master=message_frame, fg_color='#e4e5f1')
            message_text_frame.pack(padx=5, pady=5, side='left')
            CTkLabel(master=message_text_frame, text=name, font=('Arial Bold', 12), text_color='#1f61a5').pack(
                side=TOP, anchor=NW)
            CTkLabel(master=message_text_frame, font=('Arial Bold', 10), text=ans).pack(side='left', anchor=NW)
            message_downvote_frame = CTkFrame(master=message_frame, fg_color='#e4e5f1')
            message_upvote_frame = CTkFrame(master=message_frame, fg_color='#e4e5f1')
            message_downvote_frame.pack(side='right', padx=10, pady=5)
            upvote_count_display = CTkLabel(master=message_upvote_frame, text=upvotes, font=('Arial Bold', 10),
                                            text_color='#1f61a5')
            downvote_count_display = CTkLabel(master=message_downvote_frame, text=downvotes, font=('Arial Bold', 10),
                                              text_color='#1f61a5')
            CTkButton(master=message_downvote_frame, width=20, height=20, text='', hover_color='#7C0A02',
                      image=downvote_img, command=lambda id=i, upcount_display=upvote_count_display,
                                                         downcount_display=downvote_count_display: downvote_ans(i,
                                                                                                                upcount_display,
                                                                                                                downcount_display)).pack(
                side=TOP)

            downvote_count_display.pack(side=BOTTOM)
            message_upvote_frame.pack(side='right', padx=10, pady=5)
            CTkButton(master=message_upvote_frame, width=20, height=20, text='', hover_color='#7C0A02',
                      image=upvote_img, command=lambda id=i, upcount_display=upvote_count_display,
                                                       downcount_display=downvote_count_display: upvote_ans(id,
                                                                                                            upcount_display,
                                                                                                            downcount_display)).pack(
                side=TOP)
            upvote_count_display.pack(side=BOTTOM)


def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path


def upload_pdf_using_dialog():
    material_type = notes_upload_type_box.get()
    if material_type == 'Notes':
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
                    storage.child(
                        f"Notes/{course}/{branch}/{year}/{subject}/{module}/{current_user_type}/" + file_name).put(
                        pdf_data)
                    # print("PDF uploaded successfully!")
                    notes_upload_error_label.configure(text='PDF uploaded successfully!')
                    notes_upload_filename_entry.delete(0, END)
                    notes_upload_type_box.set("")
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
            "downvotes": 0,
            "uploadedBy": loggedInUser,
            "downloads": 0,
            "link": f"/Notes/{course}/{branch}/{year}/{subject}/{module}/{current_user_type}"
        })
    elif material_type == 'Question Banks':
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
                    storage.child(
                        f"Question Banks/{course}/{branch}/{year}/{subject}/{module}/{current_user_type}/" + file_name).put(
                        pdf_data)
                    # print("PDF uploaded successfully!")
                    notes_upload_error_label.configure(text='PDF uploaded successfully!')
                    notes_upload_filename_entry.delete(0, END)
                    notes_upload_type_box.set("")
                    notes_upload_course_box.set("")
                    notes_upload_branch_box.set("")
                    notes_upload_year_box.set("")
                    notes_upload_subject_box.set("")
                    notes_upload_module_box.set("")
        else:
            notes_upload_error_label.configure(text='Fill all fields!')
        db.collection("qbData").add({
            "filename": file_name,
            "upvotes": 0,
            "downvotes": 0,
            "uploadedBy": loggedInUser,
            "downloads": 0,
            "link": f"/Question Banks/{course}/{branch}/{year}/{subject}/{module}/{current_user_type}"
        })
    elif material_type == 'Videos':
        file_name = notes_upload_filename_entry.get()
        course = notes_upload_course_box.get()
        branch = notes_upload_branch_box.get()
        year = notes_upload_year_box.get()
        subject = notes_upload_subject_box.get()
        module = notes_upload_module_box.get()
        if all({file_name, course, branch, year, subject, module}):
            video_path = select_video_file()
            if video_path:
                with open(video_path, "rb") as f:
                    video_data = f.read()
                    storage.child(
                        f"Videos/{course}/{branch}/{year}/{subject}/{module}/{current_user_type}/" + file_name).put(
                        video_data)
                    # print("Video uploaded successfully!")
                    notes_upload_error_label.configure(text="Video uploaded successfully!")
                    db.collection("videoData").add({
                        "filename": file_name,
                        "upvotes": 0,
                        "downvotes": 0,
                        "uploadedBy": loggedInUser,  # remove the "" after testing
                        "downloads": 0,
                        "link": f"/Videos/{course}/{branch}/{year}/{subject}/{module}/{current_user_type}"
                    })
                    notes_upload_filename_entry.delete(0, END)
                    notes_upload_type_box.set("")
                    notes_upload_course_box.set("")
                    notes_upload_branch_box.set("")
                    notes_upload_year_box.set("")
                    notes_upload_subject_box.set("")
                    notes_upload_module_box.set("")
            # else:
            # print("File selection canceled.")
        else:
            notes_upload_error_label.configure(text="Fill all fields!")
            # print("Please provide all the required information.")


def select_destination_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path


def download_pdf(filename, note_type, id, count_frame):
    pdf_ref = storage.child(f"{filename}")
    if note_type == 'Notes':
        doc_ref = db.collection('pdfData').document(id)
    elif note_type == 'Question Banks':
        doc_ref = db.collection('qbData').document(id)
    elif note_type == 'Videos':
        doc_ref = db.collection('videoData').document(id)
    doc = doc_ref.get()
    downloads = doc.get('downloads')
    try:
        url = pdf_ref.get_url(None)
        response = requests.get(url)
        response.raise_for_status()
        destination_folder = select_destination_folder()
        os.makedirs(destination_folder, exist_ok=True)
        file_path = os.path.join(destination_folder, os.path.basename(filename) + ".pdf")

        with open(file_path, "wb") as f:
            f.write(response.content)
        downloads = downloads+1
        doc_ref.update({'downloads': downloads})
        count_frame.configure(text=str(downloads))
        # print("PDF downloaded successfully to:", file_path)
    except requests.exceptions.RequestException:
        # print("Error downloading PDF:", e)
        download_pdf(filename)


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
            ut1 = doc_data.get('UserType')

            if username == us1 and password == ps1:
                # print("Logged in")
                global loggedInUser
                global loggedInUserID
                global current_user_type
                loggedInUser = username
                loggedInUserID = doc.id
                current_user_type = ut1
                flag = 1
                set_text("")
                next_page(login_page, main_menu)
                logged_in_menu_container.pack(expand=True, fill='both')
                main_menu.pack(expand=True, fill='both')
                current_user_title.configure(text=loggedInUser)
                create_user_tab_check()
                break
                #exit(0)   #exit the function if login is successful

        if flag == 0:
            # print("Wrong username or password, try again")
            id_entry.delete(0, END)
            password_entry.delete(0, END)
            set_text("Wrong username or password, try again")
            login()


def logout():
    for frame in teacher_pdf_display.winfo_children():
        frame.destroy()
    for frame in student_pdf_display.winfo_children():
        frame.destroy()
    for frame in teacher_qb_display.winfo_children():
        frame.destroy()
    for frame in student_qb_display.winfo_children():
        frame.destroy()
    for frame in student_video_display.winfo_children():
        frame.destroy()
    for frame in student_video_display.winfo_children():
        frame.destroy()
    notes_search_course_box.set("")
    notes_search_branch_box.set("")
    notes_search_year_box.set("")
    notes_search_subject_box.set("")
    notes_search_module_box.set("")
    notes_upload_filename_entry.delete(0, END)
    notes_upload_type_box.set("")
    notes_upload_course_box.set("")
    notes_upload_branch_box.set("")
    notes_upload_year_box.set("")
    notes_upload_subject_box.set("")
    notes_upload_subject_box.set("")
    if notes_upload_menu_frame_container.winfo_ismapped():
        notes_upload_menu_frame_container.pack_forget()
    logged_in_menu_container.pack_forget()
    main_menu.pack_forget()
    menu_tabs.pack_forget()
    id_entry.delete(0, END)
    password_entry.delete(0, END)
    back_to_qframe()
    login_page.pack(expand=True, fill='both')


def user_details_add(signup_id_entry, signup_password_entry, signup_user_type_box,
                     signup_error_label):  # function to add user
    flag = 0
    username = signup_id_entry.get()
    password = signup_password_entry.get()
    user_type = signup_user_type_box.get()
    if all({username, password, user_type}):
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
                signup_error_label.configure(
                    text="A minimum 8 characters password contains a \ncombination of uppercase and lowercase letter \nand "
                         "number are required")
                signup_id_entry.delete(0, END)
                signup_password_entry.delete(0, END)
                user_details_add()
        if flag == 1:
            data = {
                'Username': username,
                'Password': password,
                'UserType': user_type,
                'upvotedNotes': [],
                'downvotedNotes': [],
                'upvotedAns': [],
                'downvotedAns': []
            }

            doc_ref = db.collection('userCollection').document()
            doc_ref.set(data)
            signup_error_label.configure(text="")

            # print('DocumentID: ', doc_ref.id)  # purely for knowing it works, don't need it in the code
        if flag == 0:
            signup_error_label.configure(
                text="A minimum 8 characters password contains a \ncombination of uppercase and lowercase letter \nand "
                     "number are required")
            signup_id_entry.delete(0, END)
            signup_password_entry.delete(0, END)
            user_details_add()
    else:
        signup_error_label.configure(
            text="Set all required fields")
    signup_id_entry.delete(0, END)
    signup_password_entry.delete(0, END)


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


def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.configure(show='*')
        show_password_box.configure(text='Show Password')
    else:
        password_entry.configure(show='')
        show_password_box.configure(text='Hide Password')


def signup_toggle_password(signup_password_entry, signup_show_password_box):
    if signup_password_entry.cget('show') == '':
        signup_password_entry.configure(show='*')
        signup_show_password_box.configure(text='Show Password')
    else:
        signup_password_entry.configure(show='')
        signup_show_password_box.configure(text='Hide Password')


def check_and_add_field(collection_name, document_id, field_name):
    doc_ref = db.collection(collection_name).document(document_id)
    doc = doc_ref.get()

    if doc.exists:
        if field_name not in doc.to_dict():
            doc_ref.update({field_name: []})
    else:
        doc_ref.set({field_name: []})


def get_note_value(note_type, user_type, note_name):
    check_link = f'/{note_type}/' + current_search_dir + f'{user_type}'
    if note_type == 'Notes':
        docs = db.collection('pdfData').stream()
    elif note_type == 'Question Banks':
        docs = db.collection('qbData').stream()
    elif note_type == 'Videos':
        docs = db.collection('videoData').stream()
    document_list = [doc for doc in docs]
    for doc in document_list:
        doc_data = doc.to_dict()
        doc_link = doc_data.get('link')
        doc_name = doc_data.get('filename')
        if doc_link == check_link and doc_name == note_name:
            doc_upvotes = doc_data.get('upvotes')
            doc_downvotes = doc_data.get('downvotes')
            doc_downloads = doc_data.get('downloads')
            doc_uploader = doc_data.get('uploadedBy')
            doc_id = doc.id
            return doc_upvotes,doc_downvotes,doc_downloads,doc_uploader,doc_id
            break

def downvote_note(note_type, up_count_display, down_count_display, id):
    if note_type == 'Notes':
        doc_ref = db.collection('pdfData').document(id)
        user_doc_ref = db.collection('userCollection').document(loggedInUserID)
        user_doc = user_doc_ref.get()
        if 'downvotedNotes' in user_doc.to_dict():
            new_value = str(id)
            upvoted_array_field = user_doc.to_dict()['upvotedNotes']
            downvoted_array_field = user_doc.to_dict()['downvotedNotes']
            if new_value in downvoted_array_field:
                downvoted_array_field.remove(new_value)
                new_downvotes = doc_ref.get().to_dict().get('downvotes', 0) - 1
                new_upvotes = doc_ref.get().to_dict().get('upvotes', 0)
            else:
                if new_value in upvoted_array_field:
                    upvoted_array_field.remove(new_value)
                    new_upvotes = doc_ref.get().to_dict().get('upvotes', 0) - 1
                else:
                    new_upvotes = doc_ref.get().to_dict().get('upvotes', 0)
                downvoted_array_field.append(new_value)
                new_downvotes = doc_ref.get().to_dict().get('downvotes', 0) + 1
            user_doc_ref.update({'upvotedNotes': upvoted_array_field, 'downvotedNotes': downvoted_array_field})
            doc_ref.update({'upvotes': new_upvotes, 'downvotes': new_downvotes})
            down_count_display.configure(text=str(new_downvotes))
            up_count_display.configure(text=str(new_upvotes))
        else:
            new_array = [str(id)]
            user_doc_ref.update({'downvotedNotes': new_array})
            new_downvotes = doc_ref.get().to_dict().get('downvotes', 0) + 1
            new_upvotes = doc_ref.get().to_dict().get('upvotes', 0)
            doc_ref.update({'upvotes': new_downvotes})
            down_count_display.configure(text=str(new_downvotes))
            up_count_display.configure(text=str(new_upvotes))
    elif note_type == 'Question Banks':
        doc_ref = db.collection('qbData').document(id)
        user_doc_ref = db.collection('userCollection').document(loggedInUserID)
        user_doc = user_doc_ref.get()
        if 'downvotedNotes' in user_doc.to_dict():
            new_value = str(id)
            upvoted_array_field = user_doc.to_dict()['upvotedNotes']
            downvoted_array_field = user_doc.to_dict()['downvotedNotes']
            if new_value in downvoted_array_field:
                downvoted_array_field.remove(new_value)
                new_downvotes = doc_ref.get().to_dict().get('downvotes', 0) - 1
                new_upvotes = doc_ref.get().to_dict().get('upvotes', 0)
            else:
                if new_value in upvoted_array_field:
                    upvoted_array_field.remove(new_value)
                    new_upvotes = doc_ref.get().to_dict().get('upvotes', 0) - 1
                else:
                    new_upvotes = doc_ref.get().to_dict().get('upvotes', 0)
                downvoted_array_field.append(new_value)
                new_downvotes = doc_ref.get().to_dict().get('downvotes', 0) + 1
            user_doc_ref.update({'upvotedNotes': upvoted_array_field, 'downvotedNotes': downvoted_array_field})
            doc_ref.update({'upvotes': new_upvotes, 'downvotes': new_downvotes})
            down_count_display.configure(text=str(new_downvotes))
            up_count_display.configure(text=str(new_upvotes))
        else:
            new_array = [str(id)]
            user_doc_ref.update({'downvotedNotes': new_array})
            new_downvotes = doc_ref.get().to_dict().get('downvotes', 0) + 1
            new_upvotes = doc_ref.get().to_dict().get('upvotes', 0)
            doc_ref.update({'upvotes': new_downvotes})
            down_count_display.configure(text=str(new_downvotes))
            up_count_display.configure(text=str(new_upvotes))
    elif note_type == 'Videos':
        doc_ref = db.collection('videoData').document(id)
        user_doc_ref = db.collection('userCollection').document(loggedInUserID)
        user_doc = user_doc_ref.get()
        if 'downvotedNotes' in user_doc.to_dict():
            new_value = str(id)
            upvoted_array_field = user_doc.to_dict()['upvotedNotes']
            downvoted_array_field = user_doc.to_dict()['downvotedNotes']
            if new_value in downvoted_array_field:
                downvoted_array_field.remove(new_value)
                new_downvotes = doc_ref.get().to_dict().get('downvotes', 0) - 1
                new_upvotes = doc_ref.get().to_dict().get('upvotes', 0)
            else:
                if new_value in upvoted_array_field:
                    upvoted_array_field.remove(new_value)
                    new_upvotes = doc_ref.get().to_dict().get('upvotes', 0) - 1
                else:
                    new_upvotes = doc_ref.get().to_dict().get('upvotes', 0)
                downvoted_array_field.append(new_value)
                new_downvotes = doc_ref.get().to_dict().get('downvotes', 0) + 1
            user_doc_ref.update({'upvotedNotes': upvoted_array_field, 'downvotedNotes': downvoted_array_field})
            doc_ref.update({'upvotes': new_upvotes, 'downvotes': new_downvotes})
            down_count_display.configure(text=str(new_downvotes))
            up_count_display.configure(text=str(new_upvotes))
        else:
            new_array = [str(id)]
            user_doc_ref.update({'downvotedNotes': new_array})
            new_downvotes = doc_ref.get().to_dict().get('downvotes', 0) + 1
            new_upvotes = doc_ref.get().to_dict().get('upvotes', 0)
            doc_ref.update({'upvotes': new_downvotes})
            down_count_display.configure(text=str(new_downvotes))
            up_count_display.configure(text=str(new_upvotes))

def upvote_note(note_type, up_count_display, down_count_display, id):
    if note_type == 'Notes':
        doc_ref = db.collection('pdfData').document(id)
        user_doc_ref = db.collection('userCollection').document(loggedInUserID)
        user_doc = user_doc_ref.get()
        if 'upvotedNotes' in user_doc.to_dict():
            new_value = str(id)
            upvoted_array_field = user_doc.to_dict()['upvotedNotes']
            downvoted_array_field = user_doc.to_dict()['downvotedNotes']
            if new_value in upvoted_array_field:
                upvoted_array_field.remove(new_value)
                new_upvotes = doc_ref.get().to_dict().get('upvotes', 0) - 1
                new_downvotes = doc_ref.get().to_dict().get('downvotes', 0)
            else:
                if new_value in downvoted_array_field:
                    downvoted_array_field.remove(new_value)
                    new_downvotes = doc_ref.get().to_dict().get('downvotes', 0) - 1
                else:
                    new_downvotes = doc_ref.get().to_dict().get('downvotes', 0)
                upvoted_array_field.append(new_value)
                new_upvotes = doc_ref.get().to_dict().get('upvotes', 0) + 1
            user_doc_ref.update({'upvotedNotes': upvoted_array_field, 'downvotedNotes': downvoted_array_field})
            doc_ref.update({'upvotes': new_upvotes,'downvotes': new_downvotes})
            up_count_display.configure(text=str(new_upvotes))
            down_count_display.configure(text=str(new_downvotes))
        else:
            new_array = [str(id)]
            user_doc_ref.update({'upvotedNotes': new_array})
            new_upvotes = doc_ref.get().to_dict().get('upvotes', 0) + 1
            new_downvotes = doc_ref.get().to_dict().get('downvotes', 0)
            doc_ref.update({'upvotes': new_upvotes})
            up_count_display.configure(text=str(new_upvotes))
            down_count_display.configure(text=str(new_downvotes))
    elif note_type == 'Question Banks':
        doc_ref = db.collection('qbData').document(id)
        user_doc_ref = db.collection('userCollection').document(loggedInUserID)
        user_doc = user_doc_ref.get()
        if 'upvotedNotes' in user_doc.to_dict():
            new_value = str(id)
            upvoted_array_field = user_doc.to_dict()['upvotedNotes']
            downvoted_array_field = user_doc.to_dict()['downvotedNotes']
            if new_value in upvoted_array_field:
                upvoted_array_field.remove(new_value)
                new_upvotes = doc_ref.get().to_dict().get('upvotes', 0) - 1
                new_downvotes = doc_ref.get().to_dict().get('downvotes', 0)
            else:
                if new_value in downvoted_array_field:
                    downvoted_array_field.remove(new_value)
                    new_downvotes = doc_ref.get().to_dict().get('downvotes', 0) - 1
                else:
                    new_downvotes = doc_ref.get().to_dict().get('downvotes', 0)
                upvoted_array_field.append(new_value)
                new_upvotes = doc_ref.get().to_dict().get('upvotes', 0) + 1
            user_doc_ref.update({'upvotedNotes': upvoted_array_field, 'downvotedNotes': downvoted_array_field})
            doc_ref.update({'upvotes': new_upvotes,'downvotes': new_downvotes})
            up_count_display.configure(text=str(new_upvotes))
            down_count_display.configure(text=str(new_downvotes))
        else:
            new_array = [str(id)]
            user_doc_ref.update({'upvotedNotes': new_array})
            new_upvotes = doc_ref.get().to_dict().get('upvotes', 0) + 1
            new_downvotes = doc_ref.get().to_dict().get('downvotes', 0)
            doc_ref.update({'upvotes': new_upvotes})
            up_count_display.configure(text=str(new_upvotes))
            down_count_display.configure(text=str(new_downvotes))
    elif note_type == 'Videos':
        doc_ref = db.collection('videoData').document(id)
        user_doc_ref = db.collection('userCollection').document(loggedInUserID)
        user_doc = user_doc_ref.get()
        if 'upvotedNotes' in user_doc.to_dict():
            new_value = str(id)
            upvoted_array_field = user_doc.to_dict()['upvotedNotes']
            downvoted_array_field = user_doc.to_dict()['downvotedNotes']
            if new_value in upvoted_array_field:
                upvoted_array_field.remove(new_value)
                new_upvotes = doc_ref.get().to_dict().get('upvotes', 0) - 1
                new_downvotes = doc_ref.get().to_dict().get('downvotes', 0)
            else:
                if new_value in downvoted_array_field:
                    downvoted_array_field.remove(new_value)
                    new_downvotes = doc_ref.get().to_dict().get('downvotes', 0) - 1
                else:
                    new_downvotes = doc_ref.get().to_dict().get('downvotes', 0)
                upvoted_array_field.append(new_value)
                new_upvotes = doc_ref.get().to_dict().get('upvotes', 0) + 1
            user_doc_ref.update({'upvotedNotes': upvoted_array_field, 'downvotedNotes': downvoted_array_field})
            doc_ref.update({'upvotes': new_upvotes,'downvotes': new_downvotes})
            up_count_display.configure(text=str(new_upvotes))
            down_count_display.configure(text=str(new_downvotes))
        else:
            new_array = [str(id)]
            user_doc_ref.update({'upvotedNotes': new_array})
            new_upvotes = doc_ref.get().to_dict().get('upvotes', 0) + 1
            new_downvotes = doc_ref.get().to_dict().get('downvotes', 0)
            doc_ref.update({'upvotes': new_upvotes})
            up_count_display.configure(text=str(new_upvotes))
            down_count_display.configure(text=str(new_downvotes))




# Display Frame content
def display_note_menu():
    for frame in teacher_pdf_display.winfo_children():
        frame.destroy()
    for frame in student_pdf_display.winfo_children():
        frame.destroy()
    for frame in teacher_qb_display.winfo_children():
        frame.destroy()
    for frame in student_qb_display.winfo_children():
        frame.destroy()
    for frame in student_video_display.winfo_children():
        frame.destroy()
    for frame in student_video_display.winfo_children():
        frame.destroy()
    for name in notes_file_names_teacher:
        display_name = name.replace("Notes/" + current_search_dir + "Teacher/", "")
        parent_frame = teacher_pdf_display
        try:
            note_upvotes, note_downvotes, note_downloads, note_uploader, note_id = get_note_value('Notes', 'Teacher',
                                                                                    display_name)
        except:
            frame = CTkFrame(master=parent_frame, height=100, fg_color='#fafafa')
            frame.pack(fill='x', pady=5)
            uploader_name_title = CTkLabel(master=frame, text='No notes uploaded', font=("Arial Bold", 14),
                                           text_color='#1f61a5')
            uploader_name_title.pack(side=TOP, padx=5)
            break
        frame = CTkFrame(master=parent_frame, height=100, fg_color='#fafafa')
        frame.pack(fill='x', pady=5)
        title_frame = CTkFrame(master=frame, fg_color='#fafafa')
        title_frame.pack(side=LEFT, pady=5, padx=5)
        uploader_name_title = CTkLabel(master=title_frame, text=str(note_uploader), font=("Arial Bold", 10),
                                               text_color='#1f61a5')
        uploader_name_title.pack(side=TOP, padx=5, anchor=W)
        display_title = CTkLabel(master=title_frame, text=display_name, fg_color='transparent', font=("Arial Bold", 14),
                                         text_color='#1f61a5')
        display_title.pack(side=TOP, padx=5, anchor=W)
        download_frame = CTkFrame(master=frame, fg_color='#ffffff')
        download_frame.pack(side=RIGHT, pady=5, padx=5)
        display_download_count = CTkLabel(master=download_frame, text=str(note_downloads), font=("Arial Bold", 14),
                                          text_color='#1f61a5')
        display_download_button = CTkButton(master=download_frame, width=40, height=40, text='', image=download_img,
                                                    command=lambda n=name,id=note_id,count_frame = display_download_count: download_pdf(n,'Notes',id, count_frame))
        display_download_button.pack(pady=(5, 0), padx=5, side=TOP)
        display_download_count.pack(side=BOTTOM)
        downvote_frame = CTkFrame(master=frame, fg_color='#ffffff')
        downvote_frame.pack(side=RIGHT, pady=5, padx=5)
        upvote_frame = CTkFrame(master=frame, fg_color='#ffffff')
        upvote_frame.pack(side=RIGHT, pady=5, padx=5)
        display_downvote_count = CTkLabel(master=downvote_frame, text=str(note_downvotes), font=("Arial Bold", 14),
                                          text_color='#1f61a5')
        display_upvote_count = CTkLabel(master=upvote_frame, text=str(note_upvotes), font=("Arial Bold", 14),
                                                text_color='#1f61a5')
        display_downvote_button = CTkButton(master=downvote_frame, width=40, height=40, text='', image=downvote_img, command=lambda down_count_display=display_downvote_count,up_count_display=display_upvote_count, id=note_id:downvote_note('Notes', up_count_display, down_count_display, id))
        display_downvote_button.pack(side=TOP, pady=(5, 0), padx=5)
        display_downvote_count.pack(side=BOTTOM)

        display_upvote_button = CTkButton(master=upvote_frame, width=40, height=40, text='', image=upvote_img,
                                                  command=lambda down_count_display=display_downvote_count,up_count_display=display_upvote_count,id=note_id: upvote_note('Notes', up_count_display, down_count_display, id))
        display_upvote_button.pack(side=TOP, pady=(5, 0), padx=5)
        display_upvote_count.pack(side=BOTTOM)
    for name in notes_file_names_student:
        display_name = name.replace("Notes/" + current_search_dir + "Student/", "")
        parent_frame = student_pdf_display
        try:
            note_upvotes, note_downvotes, note_downloads, note_uploader, note_id = get_note_value('Notes', 'Student',
                                                                                                  display_name)
        except:
            frame = CTkFrame(master=parent_frame, height=100, fg_color='#fafafa')
            frame.pack(fill='x', pady=5)
            uploader_name_title = CTkLabel(master=frame, text='No notes uploaded', font=("Arial Bold", 14),
                                           text_color='#1f61a5')
            uploader_name_title.pack(side=TOP, padx=5)
            break
        frame = CTkFrame(master=parent_frame, height=100, fg_color='#fafafa')
        frame.pack(fill='x', pady=5)
        title_frame = CTkFrame(master=frame, fg_color='#fafafa')
        title_frame.pack(side=LEFT, pady=5, padx=5)
        uploader_name_title = CTkLabel(master=title_frame, text=str(note_uploader), font=("Arial Bold", 10),
                                       text_color='#1f61a5')
        uploader_name_title.pack(side=TOP, padx=5, anchor=W)
        display_title = CTkLabel(master=title_frame, text=display_name, fg_color='transparent', font=("Arial Bold", 14),
                                 text_color='#1f61a5')
        display_title.pack(side=TOP, padx=5, anchor=W)
        download_frame = CTkFrame(master=frame, fg_color='#ffffff')
        download_frame.pack(side=RIGHT, pady=5, padx=5)
        display_download_count = CTkLabel(master=download_frame, text=str(note_downloads), font=("Arial Bold", 14),
                                          text_color='#1f61a5')
        display_download_button = CTkButton(master=download_frame, width=40, height=40, text='', image=download_img,
                                            command=lambda n=name,id=note_id,count_frame = display_download_count: download_pdf(n,'Notes',id, count_frame))
        display_download_button.pack(pady=(5, 0), padx=5, side=TOP)
        display_download_count.pack(side=BOTTOM)
        downvote_frame = CTkFrame(master=frame, fg_color='#ffffff')
        downvote_frame.pack(side=RIGHT, pady=5, padx=5)
        upvote_frame = CTkFrame(master=frame, fg_color='#ffffff')
        upvote_frame.pack(side=RIGHT, pady=5, padx=5)
        display_downvote_count = CTkLabel(master=downvote_frame, text=str(note_downvotes), font=("Arial Bold", 14),
                                          text_color='#1f61a5')
        display_upvote_count = CTkLabel(master=upvote_frame, text=str(note_upvotes), font=("Arial Bold", 14),
                                        text_color='#1f61a5')
        display_downvote_button = CTkButton(master=downvote_frame, width=40, height=40, text='', image=downvote_img,
                                            command=lambda down_count_display=display_downvote_count,
                                                           up_count_display=display_upvote_count,
                                                           id=note_id: downvote_note('Notes', up_count_display,
                                                                                     down_count_display, id))
        display_downvote_button.pack(side=TOP, pady=(5, 0), padx=5)
        display_downvote_count.pack(side=BOTTOM)

        display_upvote_button = CTkButton(master=upvote_frame, width=40, height=40, text='', image=upvote_img,
                                          command=lambda down_count_display=display_downvote_count,
                                                         up_count_display=display_upvote_count, id=note_id: upvote_note(
                                              'Notes', up_count_display, down_count_display, id))
        display_upvote_button.pack(side=TOP, pady=(5, 0), padx=5)
        display_upvote_count.pack(side=BOTTOM)
    for name in qb_file_names_teacher:
        display_name = name.replace("Question Banks/" + current_search_dir + "Teacher/", "")
        parent_frame = teacher_qb_display
        try:
            note_upvotes, note_downvotes, note_downloads, note_uploader, note_id = get_note_value('Question Banks', 'Teacher',
                                                                                                  display_name)
        except:
            frame = CTkFrame(master=parent_frame, height=100, fg_color='#fafafa')
            frame.pack(fill='x', pady=5)
            uploader_name_title = CTkLabel(master=frame, text='No notes uploaded', font=("Arial Bold", 14),
                                           text_color='#1f61a5')
            uploader_name_title.pack(side=TOP, padx=5)
            break
        frame = CTkFrame(master=parent_frame, height=100, fg_color='#fafafa')
        frame.pack(fill='x', pady=5)
        title_frame = CTkFrame(master=frame, fg_color='#fafafa')
        title_frame.pack(side=LEFT, pady=5, padx=5)
        uploader_name_title = CTkLabel(master=title_frame, text=str(note_uploader), font=("Arial Bold", 10),
                                       text_color='#1f61a5')
        uploader_name_title.pack(side=TOP, padx=5, anchor=W)
        display_title = CTkLabel(master=title_frame, text=display_name, fg_color='transparent', font=("Arial Bold", 14),
                                 text_color='#1f61a5')
        display_title.pack(side=TOP, padx=5, anchor=W)
        download_frame = CTkFrame(master=frame, fg_color='#ffffff')
        download_frame.pack(side=RIGHT, pady=5, padx=5)
        display_download_count = CTkLabel(master=download_frame, text=str(note_downloads), font=("Arial Bold", 14),
                                          text_color='#1f61a5')
        display_download_button = CTkButton(master=download_frame, width=40, height=40, text='', image=download_img,
                                            command=lambda n=name,id=note_id,count_frame = display_download_count: download_pdf(n,'Question Banks',id, count_frame))
        display_download_button.pack(pady=(5, 0), padx=5, side=TOP)
        display_download_count.pack(side=BOTTOM)
        downvote_frame = CTkFrame(master=frame, fg_color='#ffffff')
        downvote_frame.pack(side=RIGHT, pady=5, padx=5)
        upvote_frame = CTkFrame(master=frame, fg_color='#ffffff')
        upvote_frame.pack(side=RIGHT, pady=5, padx=5)
        display_downvote_count = CTkLabel(master=downvote_frame, text=str(note_downvotes), font=("Arial Bold", 14),
                                          text_color='#1f61a5')
        display_upvote_count = CTkLabel(master=upvote_frame, text=str(note_upvotes), font=("Arial Bold", 14),
                                        text_color='#1f61a5')
        display_downvote_button = CTkButton(master=downvote_frame, width=40, height=40, text='', image=downvote_img,
                                            command=lambda down_count_display=display_downvote_count,
                                                           up_count_display=display_upvote_count,
                                                           id=note_id: downvote_note('Question Banks', up_count_display,
                                                                                     down_count_display, id))
        display_downvote_button.pack(side=TOP, pady=(5, 0), padx=5)
        display_downvote_count.pack(side=BOTTOM)

        display_upvote_button = CTkButton(master=upvote_frame, width=40, height=40, text='', image=upvote_img,
                                          command=lambda down_count_display=display_downvote_count,
                                                         up_count_display=display_upvote_count, id=note_id: upvote_note(
                                              'Question Banks', up_count_display, down_count_display, id))
        display_upvote_button.pack(side=TOP, pady=(5, 0), padx=5)
        display_upvote_count.pack(side=BOTTOM)
    for name in qb_file_names_student:
        display_name = name.replace("Question Banks/" + current_search_dir + "Student/", "")
        parent_frame = student_qb_display
        try:
            note_upvotes, note_downvotes, note_downloads, note_uploader, note_id = get_note_value('Question Banks',
                                                                                                  'Student',
                                                                                                  display_name)
        except:
            frame = CTkFrame(master=parent_frame, height=100, fg_color='#fafafa')
            frame.pack(fill='x', pady=5)
            uploader_name_title = CTkLabel(master=frame, text='No notes uploaded', font=("Arial Bold", 14),
                                           text_color='#1f61a5')
            uploader_name_title.pack(side=TOP, padx=5)
            print(display_name)
            break
        frame = CTkFrame(master=parent_frame, height=100, fg_color='#fafafa')
        frame.pack(fill='x', pady=5)
        title_frame = CTkFrame(master=frame, fg_color='#fafafa')
        title_frame.pack(side=LEFT, pady=5, padx=5)
        uploader_name_title = CTkLabel(master=title_frame, text=str(note_uploader), font=("Arial Bold", 10),
                                       text_color='#1f61a5')
        uploader_name_title.pack(side=TOP, padx=5, anchor=W)
        display_title = CTkLabel(master=title_frame, text=display_name, fg_color='transparent', font=("Arial Bold", 14),
                                 text_color='#1f61a5')
        display_title.pack(side=TOP, padx=5, anchor=W)
        download_frame = CTkFrame(master=frame, fg_color='#ffffff')
        download_frame.pack(side=RIGHT, pady=5, padx=5)
        display_download_count = CTkLabel(master=download_frame, text=str(note_downloads), font=("Arial Bold", 14),
                                          text_color='#1f61a5')
        display_download_button = CTkButton(master=download_frame, width=40, height=40, text='', image=download_img,
                                            command=lambda n=name,id=note_id,count_frame = display_download_count: download_pdf(n,'Question Banks',id, count_frame))
        display_download_button.pack(pady=(5, 0), padx=5, side=TOP)
        display_download_count.pack(side=BOTTOM)
        downvote_frame = CTkFrame(master=frame, fg_color='#ffffff')
        downvote_frame.pack(side=RIGHT, pady=5, padx=5)
        upvote_frame = CTkFrame(master=frame, fg_color='#ffffff')
        upvote_frame.pack(side=RIGHT, pady=5, padx=5)
        display_downvote_count = CTkLabel(master=downvote_frame, text=str(note_downvotes), font=("Arial Bold", 14),
                                          text_color='#1f61a5')
        display_upvote_count = CTkLabel(master=upvote_frame, text=str(note_upvotes), font=("Arial Bold", 14),
                                        text_color='#1f61a5')
        display_downvote_button = CTkButton(master=downvote_frame, width=40, height=40, text='', image=downvote_img,
                                            command=lambda down_count_display=display_downvote_count,
                                                           up_count_display=display_upvote_count,
                                                           id=note_id: downvote_note('Question Banks', up_count_display,
                                                                                     down_count_display, id))
        display_downvote_button.pack(side=TOP, pady=(5, 0), padx=5)
        display_downvote_count.pack(side=BOTTOM)

        display_upvote_button = CTkButton(master=upvote_frame, width=40, height=40, text='', image=upvote_img,
                                          command=lambda down_count_display=display_downvote_count,
                                                         up_count_display=display_upvote_count, id=note_id: upvote_note(
                                              'Question Banks', up_count_display, down_count_display, id))
        display_upvote_button.pack(side=TOP, pady=(5, 0), padx=5)
        display_upvote_count.pack(side=BOTTOM)
    for name in videos_file_names_teacher:
        display_name = name.replace("Videos/" + current_search_dir + "Teacher/", "")
        parent_frame = teacher_video_display
        try:
            note_upvotes, note_downvotes, note_downloads, note_uploader, note_id = get_note_value('Videos',
                                                                                                  'Teacher',
                                                                                                  display_name)
        except:
            frame = CTkFrame(master=parent_frame, height=100, fg_color='#fafafa')
            frame.pack(fill='x', pady=5)
            uploader_name_title = CTkLabel(master=frame, text='No notes uploaded', font=("Arial Bold", 14),
                                           text_color='#1f61a5')
            uploader_name_title.pack(side=TOP, padx=5)
            break
        frame = CTkFrame(master=parent_frame, height=100, fg_color='#fafafa')
        frame.pack(fill='x', pady=5)
        title_frame = CTkFrame(master=frame, fg_color='#fafafa')
        title_frame.pack(side=LEFT, pady=5, padx=5)
        uploader_name_title = CTkLabel(master=title_frame, text=str(note_uploader), font=("Arial Bold", 10),
                                       text_color='#1f61a5')
        uploader_name_title.pack(side=TOP, padx=5, anchor=W)
        display_title = CTkLabel(master=title_frame, text=display_name, fg_color='transparent', font=("Arial Bold", 14),
                                 text_color='#1f61a5')
        display_title.pack(side=TOP, padx=5, anchor=W)
        download_frame = CTkFrame(master=frame, fg_color='#ffffff')
        download_frame.pack(side=RIGHT, pady=5, padx=5)
        display_download_count = CTkLabel(master=download_frame, text=str(note_downloads), font=("Arial Bold", 14),
                                          text_color='#1f61a5')
        display_download_button = CTkButton(master=download_frame, width=40, height=40, text='', image=download_img,
                                            command=lambda n=name,id=note_id,count_frame = display_download_count: download_pdf(n,'Videos',id, count_frame))
        display_download_button.pack(pady=(5, 0), padx=5, side=TOP)
        display_download_count.pack(side=BOTTOM)
        downvote_frame = CTkFrame(master=frame, fg_color='#ffffff')
        downvote_frame.pack(side=RIGHT, pady=5, padx=5)
        upvote_frame = CTkFrame(master=frame, fg_color='#ffffff')
        upvote_frame.pack(side=RIGHT, pady=5, padx=5)
        display_downvote_count = CTkLabel(master=downvote_frame, text=str(note_downvotes), font=("Arial Bold", 14),
                                          text_color='#1f61a5')
        display_upvote_count = CTkLabel(master=upvote_frame, text=str(note_upvotes), font=("Arial Bold", 14),
                                        text_color='#1f61a5')
        display_downvote_button = CTkButton(master=downvote_frame, width=40, height=40, text='', image=downvote_img,
                                            command=lambda down_count_display=display_downvote_count,
                                                           up_count_display=display_upvote_count,
                                                           id=note_id: downvote_note('Videos', up_count_display,
                                                                                     down_count_display, id))
        display_downvote_button.pack(side=TOP, pady=(5, 0), padx=5)
        display_downvote_count.pack(side=BOTTOM)

        display_upvote_button = CTkButton(master=upvote_frame, width=40, height=40, text='', image=upvote_img,
                                          command=lambda down_count_display=display_downvote_count,
                                                         up_count_display=display_upvote_count, id=note_id: upvote_note(
                                              'Videos', up_count_display, down_count_display, id))
        display_upvote_button.pack(side=TOP, pady=(5, 0), padx=5)
        display_upvote_count.pack(side=BOTTOM)
    for name in videos_file_names_student:
        display_name = name.replace("Videos/" + current_search_dir + "Student/", "")
        parent_frame = student_video_display
        try:
            note_upvotes, note_downvotes, note_downloads, note_uploader, note_id = get_note_value('Videos',
                                                                                                  'Student',
                                                                                                  display_name)
        except:
            frame = CTkFrame(master=parent_frame, height=100, fg_color='#fafafa')
            frame.pack(fill='x', pady=5)
            uploader_name_title = CTkLabel(master=frame, text='No notes uploaded', font=("Arial Bold", 14),
                                           text_color='#1f61a5')
            uploader_name_title.pack(side=TOP, padx=5)
            break
        frame = CTkFrame(master=parent_frame, height=100, fg_color='#fafafa')
        frame.pack(fill='x', pady=5)
        title_frame = CTkFrame(master=frame, fg_color='#fafafa')
        title_frame.pack(side=LEFT, pady=5, padx=5)
        uploader_name_title = CTkLabel(master=title_frame, text=str(note_uploader), font=("Arial Bold", 10),
                                       text_color='#1f61a5')
        uploader_name_title.pack(side=TOP, padx=5, anchor=W)
        display_title = CTkLabel(master=title_frame, text=display_name, fg_color='transparent', font=("Arial Bold", 14),
                                 text_color='#1f61a5')
        display_title.pack(side=TOP, padx=5, anchor=W)
        download_frame = CTkFrame(master=frame, fg_color='#ffffff')
        download_frame.pack(side=RIGHT, pady=5, padx=5)
        display_download_count = CTkLabel(master=download_frame, text=str(note_downloads), font=("Arial Bold", 14),
                                          text_color='#1f61a5')
        display_download_button = CTkButton(master=download_frame, width=40, height=40, text='', image=download_img,
                                            command=lambda n=name,id=note_id,count_frame = display_download_count: download_pdf(n,'Videos',id, count_frame))
        display_download_button.pack(pady=(5, 0), padx=5, side=TOP)
        display_download_count.pack(side=BOTTOM)
        downvote_frame = CTkFrame(master=frame, fg_color='#ffffff')
        downvote_frame.pack(side=RIGHT, pady=5, padx=5)
        upvote_frame = CTkFrame(master=frame, fg_color='#ffffff')
        upvote_frame.pack(side=RIGHT, pady=5, padx=5)
        display_downvote_count = CTkLabel(master=downvote_frame, text=str(note_downvotes), font=("Arial Bold", 14),
                                          text_color='#1f61a5')
        display_upvote_count = CTkLabel(master=upvote_frame, text=str(note_upvotes), font=("Arial Bold", 14),
                                        text_color='#1f61a5')
        display_downvote_button = CTkButton(master=downvote_frame, width=40, height=40, text='', image=downvote_img,
                                            command=lambda down_count_display=display_downvote_count,
                                                           up_count_display=display_upvote_count,
                                                           id=note_id: downvote_note('Videos', up_count_display,
                                                                                     down_count_display, id))
        display_downvote_button.pack(side=TOP, pady=(5, 0), padx=5)
        display_downvote_count.pack(side=BOTTOM)

        display_upvote_button = CTkButton(master=upvote_frame, width=40, height=40, text='', image=upvote_img,
                                          command=lambda down_count_display=display_downvote_count,
                                                         up_count_display=display_upvote_count, id=note_id: upvote_note(
                                              'Videos', up_count_display, down_count_display, id))
        display_upvote_button.pack(side=TOP, pady=(5, 0), padx=5)
        display_upvote_count.pack(side=BOTTOM)


def list_files_in_folder(folder_path):
    folder = bucket.list_blobs(prefix=folder_path)
    file_names = [blob.name for blob in folder if blob.name.endswith('/') == False]
    return file_names


def search_subjects():
    global current_search_dir
    global notes_file_names_teacher
    global qb_file_names_teacher
    global videos_file_names_teacher
    global notes_file_names_student
    global qb_file_names_student
    global videos_file_names_student

    course = notes_search_course_box.get()
    branch = notes_search_branch_box.get()
    year = notes_search_year_box.get()
    subject = notes_search_subject_box.get()
    module = notes_search_module_box.get()
    if all({course, branch, year, subject, module}):
        current_search_dir = f'{course}/{branch}/{year}/{subject}/{module}/'
        notes_file_names_teacher = list_files_in_folder('Notes/' + current_search_dir + "Teacher")
        notes_file_names_student = list_files_in_folder('Notes/' + current_search_dir + "Student")
        qb_file_names_teacher = list_files_in_folder('Question Banks/' + current_search_dir + "Teacher")
        qb_file_names_student = list_files_in_folder('Question Banks/' + current_search_dir + "Student")
        videos_file_names_teacher = list_files_in_folder('Videos/' + current_search_dir + "Teacher")
        videos_file_names_student = list_files_in_folder('Videos/' + current_search_dir + "Student")
        display_note_menu()


def select_video_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', 1)
    root.update_idletasks()
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
    root.destroy()
    return file_path


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

        # print("Video downloaded successfully to:", file_path)
    except requests.exceptions.RequestException:
        # print("Error downloading Video:", e)
        download_video(filename)


def upload_menu_toggle():
    if notes_upload_menu_frame_container.winfo_ismapped():
        notes_upload_menu_frame_container.pack_forget()
    else:
        notes_upload_menu_frame_container.pack(side='right', fill='y')


# GUI Code
# window

window = CTk(fg_color='#e7e7f4')
window.title('Study Material Repository')
window.geometry('800x550')
window.minsize(800, 550)
set_appearance_mode('light')

# Login page
login_page = CTkFrame(master=window, fg_color='#e7e7f4')
login_page.pack(expand=True, fill='both')
side_img_label = CTkLabel(master=login_page, text="", image=side_img)
side_img_label.pack(expand=True, side="left")

right_frame = CTkFrame(master=login_page, height=500, width=300, fg_color="#ffffff")
right_frame.pack(side='right', fill='both', padx=20, pady=20)

login_frame = CTkFrame(master=right_frame, height=500, width=300, fg_color="#ffffff")
login_frame.pack(padx=20, pady=20)

logo_img_label = CTkLabel(master=login_frame, text="", image=logo_img)
logo_img_label.pack(pady=10)

title_label = CTkLabel(master=login_frame, text='Log in', text_color='#1f61a5', anchor='w', justify='left',
                       font=("Arial Bold", 24))
title_label.pack(anchor="w", expand=True, pady=20)

id_label = CTkLabel(master=login_frame, text='  User ID', text_color="#1f61a5", anchor="w", justify="left",
                    font=("Arial Bold", 14), image=user_img, compound="left")
id_label.pack(anchor="w", expand=True, pady=(15, 0))
id_entry = CTkEntry(master=login_frame, corner_radius=25, width=225, fg_color="#EEEEEE", border_color="#1f61a5",
                    border_width=1,
                    text_color="#000000")
id_entry.pack(anchor="w", expand=True)

password_label = CTkLabel(master=login_frame, text='  Password', text_color="#1f61a5", anchor="w", justify="left",
                          font=("Arial Bold", 14), image=password_img, compound="left")
password_label.pack(anchor="w", expand=True, pady=(15, 0))
password_entry = CTkEntry(master=login_frame, corner_radius=25, show='*', width=225, fg_color="#EEEEEE",
                          border_color="#1f61a5",
                          border_width=1, text_color="#000000")
password_entry.pack(anchor="w", expand=True)
show_password_box = CTkCheckBox(master=login_frame, text="Show Password", border_width=1, checkbox_width=20,
                                checkbox_height=20, command=lambda: toggle_password())
show_password_box.pack(anchor="w", padx=(25, 0), pady=10)
error_label = CTkLabel(master=login_frame, text="", text_color="#FF0000")
error_label.pack(anchor="w", expand=True)

login_button = CTkButton(master=login_frame, text="Login", fg_color="#1f61a5", hover_color="#19429d", corner_radius=25,
                         font=("Arial Bold", 12), text_color="#ffffff", width=225, command=lambda: login())
login_button.pack(anchor="w", expand=True)

# Main Menu
logged_in_menu_container = CTkFrame(master=window, fg_color='#ffffff')
main_menu = CTkFrame(master=logged_in_menu_container, fg_color='#e7e7f4')
top_menu = CTkFrame(master=logged_in_menu_container, fg_color='#3b8ed0', height=30)
top_menu.pack(fill='x')
logout_button = CTkButton(master=top_menu, fg_color='#ffffff', text_color='#3b8ed0', text='Logout',
                          font=("Arial Bold", 12), corner_radius=25, command=lambda: logout())
logout_button.pack(side='right', padx=5, pady=5)
current_user_title = CTkLabel(master=top_menu, font=("Arial Bold", 14), text_color="#fafafa", anchor="w",
                              justify="left", text="  Username", image=user_img, compound='left')
current_user_title.pack(side='left', padx=20)

# Buttons menu
main_menu_title = CTkLabel(master=main_menu, text="Choose Tab",font=("Arial Bold", 16),text_color='#1f61a5')
main_menu_title.pack()

buttons_menu = CTkFrame(master=main_menu,fg_color='#ffffff')
buttons_menu.pack(pady=(0,20))

notes_button = CTkButton(master=buttons_menu, corner_radius=25, text='Notes', font=("Arial Bold", 12),
                         command=lambda: show_tabs('Notes'))
notes_button.pack(pady=20, padx=15)
qna_button = CTkButton(master=buttons_menu, corner_radius=25, text='Q & A', font=("Arial Bold", 12),
                       command=lambda: show_tabs('Q & A'))
qna_button.pack(pady=20, padx=15)
profile_button = CTkButton(master=buttons_menu, corner_radius=25, text='Profile', font=("Arial Bold", 12),
                           command=lambda: show_tabs('Profile'))
profile_button.pack(pady=20, padx=15)

# Tabs
menu_tabs = CTkTabview(master=logged_in_menu_container, fg_color='#e7e7f4', segmented_button_fg_color='#e7e7f4',
                       corner_radius=12)

notes_tab = menu_tabs.add('Notes')
qna_tab = menu_tabs.add('Q & A')
profile_tab = menu_tabs.add('Profile')

# Notes tab

notes_filter_menu_frame = CTkFrame(master=notes_tab, width=200, border_color='#484b6a', fg_color='#ffffff')
notes_filter_menu_frame.pack(side='left', fill='y', padx=10)
notes_upload_menu_frame_container = CTkFrame(master=notes_tab, width=200, border_color='#484b6a', fg_color='#ffffff')
notes_upload_menu_frame = CTkScrollableFrame(master=notes_upload_menu_frame_container, fg_color='#ffffff')
notes_upload_menu_frame.pack(expand=True, fill='both')

notes_display_frame = CTkFrame(master=notes_tab, fg_color='#fafafa')
notes_display_frame.pack(side='left', expand=True, fill='both', padx=10)

notes_display_tabs = CTkTabview(master=notes_display_frame, fg_color='#f1f1f9', corner_radius=12, height=10,
                                segmented_button_fg_color='#f1f1f9')
notes_display_tabs.pack(expand=True, fill='both', side='top', padx=10, pady=10)

teacher_tab = notes_display_tabs.add("Teacher")
student_tab = notes_display_tabs.add("Student")

teacher_tabs = CTkTabview(master=teacher_tab, fg_color='#e1e1f0', corner_radius=12, segmented_button_fg_color='#e1e1f0')
teacher_tabs.pack(expand=True, fill='both')

teacher_pdf_tab = teacher_tabs.add('Notes')
teacher_qb_tab = teacher_tabs.add('Question Banks')
teacher_video_tab = teacher_tabs.add('Videos')

teacher_pdf_display = CTkScrollableFrame(master=teacher_pdf_tab, fg_color='#e1e1f0')
teacher_pdf_display.pack(expand=True, fill='both')
teacher_qb_display = CTkScrollableFrame(master=teacher_qb_tab, fg_color='#e1e1f0')
teacher_qb_display.pack(expand=True, fill='both')
teacher_video_display = CTkScrollableFrame(master=teacher_video_tab, fg_color='#e1e1f0')
teacher_video_display.pack(expand=True, fill='both')

student_tabs = CTkTabview(master=student_tab, fg_color='#e1e1f0', corner_radius=12, segmented_button_fg_color='#e1e1f0')
student_tabs.pack(expand=True, fill='both')

student_pdf_tab = student_tabs.add('Notes')
student_qb_tab = student_tabs.add('Question Banks')
student_video_tab = student_tabs.add('Videos')

student_pdf_display = CTkScrollableFrame(master=student_pdf_tab, fg_color='#e1e1f0')
student_pdf_display.pack(expand=True, fill='both')
student_qb_display = CTkScrollableFrame(master=student_qb_tab, fg_color='#e1e1f0')
student_qb_display.pack(expand=True, fill='both')
student_video_display = CTkScrollableFrame(master=student_video_tab, fg_color='#e1e1f0')
student_video_display.pack(expand=True, fill='both')

filter_course_table = ['B.Tech']
filter_branch_table = ['CSE']
filter_year_table = ['1st year', '2nd year', '3rd year', '4th year']
filter_subject_table = ['']
filter_module_table = ['1', '2', '3', '4', '5']

notes_filter_menu_title = CTkLabel(master=notes_filter_menu_frame, text='Filter', text_color='#1f61a5', anchor='w',
                                   justify='left', font=("Arial Bold", 18))
notes_filter_menu_title.pack(padx=10)
notes_search_course_label = CTkLabel(master=notes_filter_menu_frame, text='Course', width=200, font=("Arial Bold", 12),
                                     text_color='#1f61a5')
notes_search_course_label.pack(padx=10)
notes_search_course_box = CTkComboBox(master=notes_filter_menu_frame, border_color="#1f61a5",
                                      border_width=1, values=filter_course_table, state='readonly', fg_color="#EEEEEE",
                                      text_color="#000000", corner_radius=25)
notes_search_course_box.pack(padx=10)
notes_search_branch_label = CTkLabel(master=notes_filter_menu_frame, text='Branch', width=200, font=("Arial Bold", 12),
                                     text_color='#1f61a5')
notes_search_branch_label.pack(padx=10)
notes_search_branch_box = CTkComboBox(master=notes_filter_menu_frame, border_color="#1f61a5",
                                      border_width=1, values=filter_branch_table, state='readonly', fg_color="#EEEEEE",
                                      text_color="#000000", corner_radius=25)
notes_search_branch_box.pack(padx=10)
notes_search_year_label = CTkLabel(master=notes_filter_menu_frame, text='Year', width=200, font=("Arial Bold", 12),
                                   text_color='#1f61a5')
notes_search_year_label.pack(padx=10)
notes_search_year_box = CTkComboBox(master=notes_filter_menu_frame, border_color="#1f61a5",
                                    border_width=1, values=filter_year_table, state='readonly',
                                    command=show_notes_filter_subjects, fg_color="#EEEEEE", text_color="#000000",
                                    corner_radius=25)
notes_search_year_box.pack(padx=10)
notes_search_subject_label = CTkLabel(master=notes_filter_menu_frame, text='Subject', width=200,
                                      font=("Arial Bold", 12), text_color='#1f61a5')
notes_search_subject_label.pack(padx=10)
notes_search_subject_box = CTkComboBox(master=notes_filter_menu_frame, border_color="#1f61a5",
                                       border_width=1, values=filter_subject_table, state='readonly',
                                       fg_color="#EEEEEE", text_color="#000000", corner_radius=25)
notes_search_subject_box.pack(padx=10)
notes_search_module_label = CTkLabel(master=notes_filter_menu_frame, text='Module', width=200, font=("Arial Bold", 12),
                                     text_color='#1f61a5')
notes_search_module_label.pack(padx=10)
notes_search_module_box = CTkComboBox(master=notes_filter_menu_frame, border_color="#1f61a5",
                                      border_width=1, values=filter_module_table, state='readonly', fg_color="#EEEEEE",
                                      text_color="#000000", corner_radius=25)
notes_search_module_box.pack(padx=10)
notes_search_button = CTkButton(master=notes_filter_menu_frame, corner_radius=25, text='  Search', image=search_img,
                                font=("Arial Bold", 12),
                                command=lambda: search_subjects())
notes_search_button.pack(pady=10)
notes_search_error_label = CTkLabel(master=notes_filter_menu_frame, text='', text_color="#FF0000")
notes_search_error_label.pack()

upload_course_table = ['B.Tech']
upload_branch_table = ['CSE']
upload_year_table = ['1st year', '2nd year', '3rd year', '4th year']
upload_subject_table = ['']
upload_module_table = ['1', '2', '3', '4', '5']

notes_upload_menu_button = CTkButton(master=notes_display_frame, text='  Upload', image=upload_img, corner_radius=25,
                                     font=("Arial Bold", 12), command=lambda: upload_menu_toggle())
notes_upload_menu_button.pack(pady=10)

notes_upload_menu_title = CTkLabel(master=notes_upload_menu_frame, text='Upload', text_color='#1f61a5', anchor='w',
                                   justify='left', font=("Arial Bold", 18))
notes_upload_menu_title.pack(padx=10)
notes_upload_filename_label = CTkLabel(master=notes_upload_menu_frame, text='File name', width=200,
                                       font=("Arial Bold", 12), text_color='#1f61a5')
notes_upload_filename_label.pack()
notes_upload_filename_entry = CTkEntry(master=notes_upload_menu_frame, border_color="#1f61a5",
                                       border_width=1, fg_color="#EEEEEE", text_color="#000000", corner_radius=25)
notes_upload_filename_entry.pack()
file_types = ['Notes', 'Question Banks', 'Videos']
notes_upload_type_label = CTkLabel(master=notes_upload_menu_frame, text='File Type', width=200, font=("Arial Bold", 12),
                                   text_color='#1f61a5')
notes_upload_type_label.pack(padx=10)
notes_upload_type_box = CTkComboBox(master=notes_upload_menu_frame, border_color="#1f61a5",
                                    border_width=1, state='readonly', values=file_types, fg_color="#EEEEEE",
                                    text_color="#000000", corner_radius=25)
notes_upload_type_box.pack(padx=10)
notes_upload_course_label = CTkLabel(master=notes_upload_menu_frame, text='Course', width=200, font=("Arial Bold", 12),
                                     text_color='#1f61a5')
notes_upload_course_label.pack(padx=10)
notes_upload_course_box = CTkComboBox(master=notes_upload_menu_frame, border_color="#1f61a5",
                                      border_width=1, state='readonly', values=upload_course_table, fg_color="#EEEEEE",
                                      text_color="#000000", corner_radius=25)
notes_upload_course_box.pack(padx=10)

notes_upload_branch_label = CTkLabel(master=notes_upload_menu_frame, text='Branch', width=200, font=("Arial Bold", 12),
                                     text_color='#1f61a5')
notes_upload_branch_label.pack(padx=10)
notes_upload_branch_box = CTkComboBox(master=notes_upload_menu_frame, border_color="#1f61a5",
                                      border_width=1, state='readonly', values=upload_branch_table, fg_color="#EEEEEE",
                                      text_color="#000000", corner_radius=25)
notes_upload_branch_box.pack(padx=10)
notes_upload_year_label = CTkLabel(master=notes_upload_menu_frame, text='Year', font=("Arial Bold", 12),
                                   text_color='#1f61a5')
notes_upload_year_label.pack(padx=10)
notes_upload_year_box = CTkComboBox(master=notes_upload_menu_frame, border_color="#1f61a5",
                                    border_width=1, values=upload_year_table, state='readonly', fg_color="#EEEEEE",
                                    text_color="#000000", corner_radius=25,
                                    command=show_notes_upload_subjects)
notes_upload_year_box.pack(padx=10)
notes_upload_subject_label = CTkLabel(master=notes_upload_menu_frame, text='Subject', width=200,
                                      font=("Arial Bold", 12), text_color='#1f61a5')
notes_upload_subject_label.pack(padx=10)
notes_upload_subject_box = CTkComboBox(master=notes_upload_menu_frame, border_color="#1f61a5", fg_color="#EEEEEE",
                                       text_color="#000000", corner_radius=25,
                                       border_width=1, state='readonly', values=upload_subject_table)
notes_upload_subject_box.pack(padx=10)
notes_upload_module_label = CTkLabel(master=notes_upload_menu_frame, text='Module', width=200, font=("Arial Bold", 12),
                                     text_color='#1f61a5')
notes_upload_module_label.pack(padx=10)
notes_upload_module_box = CTkComboBox(master=notes_upload_menu_frame, border_color="#1f61a5", fg_color="#EEEEEE",
                                      text_color="#000000", corner_radius=25,
                                      border_width=1, state='readonly', values=upload_module_table)
notes_upload_module_box.pack(padx=10)
notes_upload_button = CTkButton(master=notes_upload_menu_frame, text='  Upload', corner_radius=25, image=upload_img,
                                font=("Arial Bold", 12),
                                command=lambda: upload_pdf_using_dialog())
notes_upload_button.pack(pady=10)
notes_upload_error_label = CTkLabel(master=notes_upload_menu_frame, text='', text_color="#FF0000")
notes_upload_error_label.pack()


# qna

def back_to_qframe():
    rframe.pack_forget()
    back_button_frame.pack_forget()
    ranstextbox.delete(0, END)
    scrolling_frame_1.pack(side='bottom', fill='both', expand=True)
    post_button.pack(pady=10)


def refresh_questions():
    for i in dict_ids:
        q = dict_qns[dict_ids[i]]
        frame = CTkFrame(master=scrolling_frame_1, fg_color='#e4e5f1')
        frame.pack(fill='x', pady=5, padx=5)
        CTkLabel(master=frame, text=q, anchor='w', text_color="#1f61a5", justify="left",
                 font=("Arial Bold", 14)).pack(side='left', padx=10, pady=10)

        b = CTkButton(master=frame, text='View', hover=True, corner_radius=25,
                      command=lambda text=q, id=i: fetch_data(text, id))
        ##b.bind("<Button-1>", lambda event, text=q: fetch_data(text))
        b.pack(side=RIGHT, padx=20, pady=5)
        b = CTkButton(master=scrolling_frame_1)


def button_click_event():
    # buttons in scrolling frame and their event handling
    global r
    dialog = CTkInputDialog(text="Enter Question:", title="Test")
    data = dialog.get_input()
    if data:
        doc_ref = db.collection('qna').document()
        doc_ref.set({'qn': data, 'ans': ''})
        getqns()
        refresh_questions()
        r += 1


qna_display_frame = CTkFrame(master=qna_tab, fg_color='#e7e7f4')
qna_display_frame.pack(expand=True, fill='both')
post_button = CTkButton(master=qna_display_frame, text='Post Question', corner_radius=50, hover=True,
                        command=button_click_event)
post_button.pack(pady=10)
rframe = CTkFrame(master=qna_display_frame, width=400, fg_color="#fafafa")

back_button_frame = CTkFrame(master=qna_display_frame, fg_color='#e7e7f4')
back_button = CTkButton(master=back_button_frame, text="Back", corner_radius=20, command=lambda: back_to_qframe())
back_button.pack(pady=10)
rqframe = CTkLabel(master=rframe, text="", fg_color='#fafafa', text_color="#1f61a5", justify="left",
                   font=("Arial Bold", 14), width=400)
rqframe.pack(fill='x')
raframe = CTkScrollableFrame(master=rframe, fg_color='#fafafa')
raframe.pack(expand=True, fill='both')
ransbox = CTkFrame(master=rframe, width=400)
ransbox.pack(fill='x')
ranstextbox = CTkEntry(master=ransbox, width=225, fg_color="#EEEEEE",
                       border_color="#1f61a5",
                       border_width=1, text_color="#000000", corner_radius=25)
ranstextbox.pack(side=LEFT, expand=True, fill='x', pady=5, padx=5)
ransbutton = CTkButton(master=ransbox, text='Answer', corner_radius=25, command=lambda: answer_qn())
ransbutton.pack(side=LEFT, pady=5, padx=5)
scrolling_frame_1 = CTkScrollableFrame(master=qna_display_frame, width=400,
                                       fg_color='#fafafa', scrollbar_button_color='#d2d3db')  # fg_color='#b2ccf2')
scrolling_frame_1.pack(side='left', fill='both', expand=True)
getqns()  # call to get/update qns

for i in dict_ids:
    q = dict_qns[dict_ids[i]]
    frame = CTkFrame(master=scrolling_frame_1, fg_color='#e4e5f1')
    frame.pack(fill='x', pady=5, padx=5)
    CTkLabel(master=frame, text=q, anchor='w', text_color="#1f61a5", justify="left",
             font=("Arial Bold", 14)).pack(side='left', padx=10, pady=10)

    b = CTkButton(master=frame, text='View', hover=True, corner_radius=25,
                  command=lambda text=q, id=i: fetch_data(text, id))
    ##b.bind("<Button-1>", lambda event, text=q: fetch_data(text))
    b.pack(side=RIGHT, padx=20, pady=5)
    b = CTkButton(master=scrolling_frame_1)
    r = r + 1


# user signup
def create_user_tab_check():
    global admin_logged
    if current_user_type == 'Admin' and not admin_logged:
        admin_logged = True
        signup_tab = menu_tabs.add('Create User')
        signup_page = CTkFrame(master=signup_tab, fg_color='#e7e7f4')
        signup_page.pack(expand=True, fill='both')

        signup_right_frame = CTkFrame(master=signup_page, height=500, width=300, fg_color="#ffffff")
        signup_right_frame.pack(expand=True, side='right', fill='y', pady=10, padx=10)

        signup_login_frame = CTkFrame(master=signup_right_frame, height=500, width=300, fg_color="#ffffff")
        signup_login_frame.propagate(False)
        signup_login_frame.pack(expand=True)

        signup_title_label = CTkLabel(master=signup_login_frame, text='Create User', text_color='#1f61a5', anchor='w',
                                      justify='left',
                                      font=("Arial Bold", 24))
        signup_title_label.pack(anchor="w", pady=(20, 5), padx=(25, 0))

        signup_id_label = CTkLabel(master=signup_login_frame, text='  User ID', text_color="#1f61a5", anchor="w",
                                   justify="left",
                                   font=("Arial Bold", 14), image=user_img, compound="left")
        signup_id_label.pack(anchor="w", pady=(15, 0), padx=(25, 0))
        signup_id_entry = CTkEntry(master=signup_login_frame, width=225, fg_color="#EEEEEE", border_color="#1f61a5",
                                   border_width=1, corner_radius=20,
                                   text_color="#000000")
        signup_id_entry.pack(anchor="w", padx=(25, 0))

        signup_password_label = CTkLabel(master=signup_login_frame, text='  Password', text_color="#1f61a5", anchor="w",
                                         justify="left",
                                         font=("Arial Bold", 14), image=password_img, compound="left")
        signup_password_label.pack(anchor="w", pady=(15, 0), padx=(25, 0))
        signup_password_entry = CTkEntry(master=signup_login_frame, show='*', width=225, fg_color="#EEEEEE",
                                         border_color="#1f61a5", corner_radius=20,
                                         border_width=1, text_color="#000000")
        signup_password_entry.pack(anchor="w", padx=(25, 0))
        signup_show_password_box = CTkCheckBox(master=signup_login_frame, text="Show Password", border_width=1,
                                               checkbox_width=20,
                                               checkbox_height=20,
                                               command=lambda: signup_toggle_password(signup_password_entry,
                                                                                      signup_show_password_box))
        signup_show_password_box.pack(anchor="w", padx=(25, 0), pady=10)

        signup_user_type_label = CTkLabel(master=signup_login_frame, text='  User Type', text_color="#1f61a5",
                                          anchor="w", justify="left",
                                          font=("Arial Bold", 14), image=user_img, compound="left")
        signup_user_type_label.pack(anchor="w", padx=(25, 0))

        user_types = ['Student', 'Teacher', 'Admin']

        signup_user_type_box = CTkComboBox(master=signup_login_frame, width=225, fg_color="#EEEEEE",
                                           border_color="#1f61a5", corner_radius=20,
                                           border_width=1, text_color="#000000", values=user_types, state='readonly')
        signup_user_type_box.pack(anchor="w", padx=(25, 0))

        signup_error_label = CTkLabel(master=signup_login_frame, text="", text_color="#FF0000")
        signup_error_label.pack(anchor="w", padx=(25, 0))

        signup_button = CTkButton(master=signup_login_frame, text="Create User", fg_color="#1f61a5",
                                  hover_color="#19429d",
                                  font=("Arial Bold", 12), text_color="#ffffff", width=225, corner_radius=20,
                                  command=lambda: user_details_add(signup_id_entry, signup_password_entry,
                                                                   signup_user_type_box, signup_error_label))
        signup_button.pack(anchor="w", pady=(20, 0), padx=(25, 0))
    else:
        if admin_logged:
            menu_tabs.delete("Create User")
            admin_logged = False


# run
window.mainloop()
