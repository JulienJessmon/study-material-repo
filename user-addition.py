import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(
    r"D:\Desktop\Python\study-mat-repo\study-material-repo-firebase-adminsdk-bj0om-72965ed62f.json")  # your path will be different based on where you store your private key
firebase_admin.initialize_app(cred)


def userDetails_add():
    flag = 0
    username = input("Enter Username: ")
    password = input("Enter Password: ")
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
            print(
                "make sure your password is more than 8 characters and has a capital letter, a number, a special character and no spaces in them")
            userDetails_add()
    if flag == 1:
        db = firestore.client()
        data = {
            'Username': username,
            'Password': password
        }

        doc_ref = db.collection('userCollection').document()
        doc_ref.set(data)

        print('DocumentID: ', doc_ref.id)  # purely for knowing it works, don't need it in the code
    if flag == 0:
        print(
            "make sure your password is more than 8 characters and has a capital letter, a number, a special character and no spaces in them")
        userDetails_add()


userDetails_add()
