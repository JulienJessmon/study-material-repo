import customtkinter as ct
import tkinter as tk
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"D:\Athul\Miniproject\Main_prgm\Firebase_PvtKey.json")
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
    dialog = ct.CTkInputDialog(text="Enter data:", title="Test")
    data = dialog.get_input()
    if data:
        ct.CTkLabel(master=rframe)


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


def fetch_data(rframe, qn):  # fetches data to put in rframe..qns and answers
    # print(rframe)
    # print(qn)
    print(dict_qns)
    empty_frame(rframe)
    for id, q in dict_qns.items():
        if q == qn:
            break

    ct.CTkLabel(master=rframe, width=600, text=qn, anchor='w').pack(pady=10, padx=(30, 0))
    ans = get_ans(id)
    if ans is None:
        ct.CTkLabel(master=rframe,width=600,text='No Answer Yet',text_color='#ff0000',anchor='e').pack(pady=10,padx=(0,30))
    else:
        for i in ans:
            print(i)
            ct.CTkLabel(master=rframe, width=600, text=i, anchor='e').pack(pady=10, padx=10)


def main():
    global r
    # Main GUI
    root = ct.CTk()
    root.title('Hello')
    root.geometry('500x600')
    root.minsize(500, 600)

    def button_click_event():
        # buttons in scrolling frame and their event handling
        global r
        print(r)
        dialog = ct.CTkInputDialog(text="Enter Question:", title="Test")
        data = dialog.get_input()
        if data:
            ct.CTkLabel(master=scrolling_frame_1, text=data, anchor='w').grid(row=r, column=0, padx=(100, 100), pady=5)
            b = ct.CTkButton(master=scrolling_frame_1, text='View', fg_color='#aab7f2', hover_color='#99a4d9',
                             hover=True)
            b.bind("<Button-1>", lambda event, text=data: fetch_data(rframe, text))
            b.grid(row=r, column=1, padx=20, pady=5)
            doc_ref = db.collection('qna').document()
            doc_ref.set({'qn': data, 'ans': ''})
            getqns()
            r += 1
    post_button = ct.CTkButton(master=root, text='Post Question', corner_radius=50, hover_color='#ff0000', hover=True,command=button_click_event)
    post_button.pack(pady=10)
    rframe = ct.CTkFrame(master=root, height=500, width=600)
    rframe.pack(side='right', fill='both')

    scrolling_frame_1 = ct.CTkScrollableFrame(master=root, height=500, width=600,
                                              scrollbar_button_hover_color='#aab7f2')  # fg_color='#b2ccf2')
    scrolling_frame_1.pack(side='left', fill='y')
    getqns()  # call to get/update qns

    for i in dict_ids:
        q = dict_qns[dict_ids[i]]
        ct.CTkLabel(master=scrolling_frame_1, text=q, anchor='w').grid(row=r, column=0, padx=(100, 100), pady=10)
        b = ct.CTkButton(master=scrolling_frame_1, text='View', fg_color='#aab7f2', hover_color='#99a4d9', hover=True)
        b.bind("<Button-1>", lambda event, text=q: fetch_data(rframe, text))
        b.grid(row=r, column=1, padx=20, pady=5)
        r = r + 1
    root.mainloop()


if __name__ == '__main__':
    main()
