import os
import requests
from io import BytesIO
import firebase_admin
import pyrebase
from google.cloud.firestore_v1.base_query import FieldFilter
from firebase_admin import credentials,firestore,storage
from PIL import Image
from customtkinter import filedialog
cred = credentials.Certificate(r"D:\Athul\Miniproject\Main_prgm\Firebase_PvtKey.json")
config={
    "apiKey": "AIzaSyCtubeFcnQtDDC0Algoy09TvtvgjJyRojA",
    "authDomain": "study-material-repo.firebaseapp.com",
    "projectId": "study-material-repo",
    'storageBucket': "study-material-repo.appspot.com",
    "messagingSenderId": "291006521607",
    "appId": "1:291006521607:web:7196317a36dcf6f0e365a2",
    "measurementId": "G-6EGQ548K06",
    "databaseURL": ""
}

firebase_admin.initialize_app(cred,config)
firebase=pyrebase.initialize_app(config)
db=firestore.client()
storage=firebase.storage()
collection_ref = db.collection('userCollection')
#bucket=storage.bucket()
class UserProfile():#ctk.Ctk):
    username=[]     #Name
    user_type={}    #Name and Type
    data=[]
    videodata=[]
    notedata=[]
    def setData(self):
        field_filter=FieldFilter('Username','==',self.name)  #Filter to user j1
        query1=db.collection('userCollection').where(filter=field_filter)
        doc=query1.get()
        data=doc[0].to_dict()
        document_ids = [i.id for i in doc]
        self.id = document_ids[0]
        self.type=data['UserType']      #Set user type
        
    def changePassword(self):
        field_filter = FieldFilter('Username', '==', self.name)  # Filter to user j1
        query1 = db.collection('userCollection').where(filter=field_filter)
        doc = query1.get()
        data = doc[0].to_dict()
        document_ids = [i.id for i in doc]
        query1 = db.collection('userCollection').document(document_ids[0])
        doc=query1.get()
        data=doc.to_dict()
        print(data)
        newPassword=input("\nEnter new password:")
        query1.update({'Password':newPassword})
        print("Password Updated")
        
    def video(self):
        field_filter = FieldFilter('uploadedBy', '==', self.name)    #Filter
        query1 = db.collection('videoData').where(filter=field_filter)  #Video data
        doc=query1.get()
        for i in doc:
            i=i.to_dict()
            self.videodata.append(i['filename'])
        print(self.videodata)

    def PDFs(self):
        path = []
        field_filter = FieldFilter('uploadedBy', '==', self.name)  # Filter
        query1 = db.collection('pdfData').where(filter=field_filter)  # PDF data
        doc = query1.get()
        for i in doc:
            i = i.to_dict()
            self.notedata.append(i['filename'])
            path.append(i['link'])
        # print(self.notedata)
        print(path)  # Directories in path

    def setProfileImage(self):
            field_filter = FieldFilter('Username', '==', self.name)  # Filter to user j1
            query1 = db.collection('userCollection').where(filter=field_filter)
            doc=query1.get()
            document_ids = [i.id for i in doc]
            id=document_ids[0]
            #print('Document IDs:', document_ids)
            doc = query1.get()
            #data = doc[0].to_dict()
            #print(doc)
            path = filedialog.askopenfilename(filetypes=[(".PNG Files", "*.png")])
            if path:
                self.file_name = os.path.basename(path)
                self.img = Image.open(path)
                # Now, img is your uploaded image
                # You can perform operations on the image here
                print("Image shown successfully!")
                print(type(self.img))
                print(path)
                print(self.file_name)
            imgbytes=BytesIO()
            self.img.save(imgbytes,format='PNG')
            imgbytes.seek(0)
            storage.child(f'Profile_Pics/'+self.id).put(imgbytes,content_type='image/png')
            self.img_url=storage.child(f'Profile_Pics/'+self.id).get_url(None)    #DO CHANGE THE NAME TO THE ONE CHOSEN
            query1 = db.collection('userCollection').document(id)
            query1.update({"image_url":self.img_url})
        
    def getImage(self):

        field_filter = FieldFilter('Username', '==', self.name)  # Filter to user j1
        query1 = db.collection('userCollection').document(self.id)
        doc=query1.get()
        self.img_url=doc.to_dict()['image_url']
        response = requests.get(self.img_url, stream=True)

        if response.status_code == 200:
            image_data = response.content
            image = Image.open(BytesIO(image_data))
        #image to be used is in image


    def __init__(self,name,password):
        self.name=name
        self.password=password
        print(self.name,self.password)
        self.setData()
        print(self.type)
        self.video()
        self.PDFs()
        self.setProfileImage()
        self.getImage()
UserProfile('cse19','Password@234')
