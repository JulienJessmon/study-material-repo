from customtkinter import *
import tkinter as tk
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"C:\Users\Admin\PycharmProjects\MiniProject\study-material-repo-firebase-adminsdk-bj0om-7cddb30570.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
collection_ref = db.collection('qna')
dict_ids = {}
dict_qns = {}
list_qns = []
a = {}
r = 0
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
                for answer in data:
                    print(answer)
                return (data)
        except KeyError:
            print("Error")      #Show error in frame
    else:
        print('failed')
        return []


def answer_qn():  # Answer a qn
    c = int(input())
    for i in dict_ids:
        if i == c:
            # print(dict_qns[dict_ids[i]])
            break
    a = get_ans(dict_ids[c])
    answer = input("\nEnter answer:")
    a.append(answer)
    doc_ref = db.collection('qna').document(dict_ids[c])
    doc_ref.update({'ans': a})

    # print(ans)


def fetch_data(qn):  # fetches data to put in rframe..qns and answers
    # print(rframe)
    # print(qn)
    empty_frame(raframe)
    for id, q in dict_qns.items():
        if q == qn:
            break

    rqframe.configure(text=qn)
    ans = get_ans(id)
    if ans is None:
        CTkLabel(master=raframe, text='No Answer Yet',text_color='#ff0000',anchor='e').pack(padx=10,pady=10)
    else:
        for i in ans:
            message_frame = CTkFrame(master=raframe,fg_color='#e4e5f1')
            message_frame.pack(padx=5,pady=5,side=TOP, anchor=NW)
            CTkLabel(master=message_frame, text=i, anchor='e').pack(padx=10,pady=5)


def test():
    frame = CTkFrame(master=root)
    frame.pack()

# Main GUI
root = CTk(fg_color='#fafafa')
root.title('Hello')
root.geometry('800x500')
root.minsize(800, 500)
set_appearance_mode('light')

def button_click_event():
    # buttons in scrolling frame and their event handling
    global r
    dialog = CTkInputDialog(text="Enter Question:", title="Test")
    data = dialog.get_input()
    if data:
        frame = CTkFrame(master=scrolling_frame_1, fg_color='#e4e5f1')
        frame.pack(fill='x', pady=5, padx=5)
        CTkLabel(master=frame, text=data, anchor='w',text_color="#1f61a5", justify="left",
                          font=("Arial Bold", 14)).pack(side='left', padx=10, pady=10)
        b = CTkButton(master=frame, text='View', hover=True)
        b.bind("<Button-1>", lambda event, text=data: fetch_data(text))
        b.pack(side=RIGHT, padx=20, pady=5)
        doc_ref = db.collection('qna').document()
        doc_ref.set({'qn': data, 'ans': ''})
        getqns()
        r += 1
post_button = CTkButton(master=root, text='Post Question', corner_radius=50, hover_color='#ff0000', hover=True,command=button_click_event)
post_button.pack(pady=10)
rframe = CTkFrame(master=root, width=400)
rframe.pack(side='right', fill='both', expand=True)
rqframe = CTkLabel(master=rframe, text="",fg_color='#fafafa',text_color="#1f61a5", justify="left",
                          font=("Arial Bold", 14), width=400)
rqframe.pack(fill='x')
raframe = CTkScrollableFrame(master=rframe,fg_color='#fafafa')
raframe.pack(expand=True,fill='both')
ransbox = CTkFrame(master=rframe, width=400)
ransbox.pack(fill='x')
ranstextbox = CTkEntry(master=ransbox)
ranstextbox.pack(side=LEFT, expand=True,fill='x',pady=5,padx=5)
ransbutton = CTkButton(master=ransbox, text='Answer', command=lambda: answer_qn())
ransbutton.pack(side=LEFT,pady=5,padx=5)
scrolling_frame_1 = CTkScrollableFrame(master=root,width=400,
                                              fg_color='#fafafa', scrollbar_button_color='#d2d3db')  # fg_color='#b2ccf2')
scrolling_frame_1.pack(side='left', fill='both', expand=True)
getqns()  # call to get/update qns
for i in dict_ids:
    q = dict_qns[dict_ids[i]]
    frame = CTkFrame(master=scrolling_frame_1, fg_color='#e4e5f1')
    frame.pack(fill='x', pady=5,padx=5)
    CTkLabel(master=frame, text=q, anchor='w', text_color="#1f61a5", justify="left",
                          font=("Arial Bold", 14)).pack(side='left', padx=10, pady=10)

    b = CTkButton(master=frame, text='View', hover=True)
    b.bind("<Button-1>", lambda event, text=q: fetch_data(text))
    b.pack(side=RIGHT, padx=20, pady=5)
    b = CTkButton(master=scrolling_frame_1)
    r = r + 1
root.mainloop()


