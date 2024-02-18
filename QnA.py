from customtkinter import *
from PIL import Image
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
def main():
    cred = credentials.Certificate(r"D:\Athul\Miniproject\Main_prgm\Firebase_PvtKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    # GUI Code
    # window
    window = CTk()
    window.title('Study Material Repository')
    window.geometry('600x500')
    window.minsize(600, 500)
    set_appearance_mode('light')
    b = ''
    def button_click_event():
        dialog = CTkInputDialog(text="Enter Question:", title="Test")
        b = dialog.get_input()
        if b:
            CTkButton(scrollable_frame, text=b, command=command_button).pack(pady=10)
            doc_ref = db.collection('qna').document()
            doc_ref.set({'qn': b})
    button = CTkButton(window, text="Post Question", command=button_click_event, corner_radius=100)
    button.pack(padx=20, pady=20)
    scrollable_frame = CTkScrollableFrame(window, width=550, height=550)
    scrollable_frame.pack(pady=25)

    def command_button():
        new_window = CTkToplevel(window)
        new_window.geometry("600x500")
        new_window.title(txt)
        frame=CTkScrollableFrame(new_window,height=200,width=500).pack()
        lab=CTkLabel(frame,text='Hello')
        #lab.pack()
        #lab.configure(text=tbox2.get())


        #tbox=CTkTextbox(new_window,height=300,width=500,fg_color=("gray", "black"),state='disabled').pack(pady=10,padx=10)

        tbox2=CTkTextbox(new_window,height=300,width=500,fg_color=("gray", "black")).pack(pady=10,padx=10)
        #tbox.insert(txt)


    collection_ref = db.collection('qna')
    texts = collection_ref.stream()

    for text_doc in texts:
        text_data = text_doc.to_dict()
        txt = text_data.get('qn', '')
        CTkButton(scrollable_frame, text=txt, command=command_button).pack(pady=10)





    window.mainloop()
if __name__=="__main__":
    main()