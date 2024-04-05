import firebase_admin
from google.cloud.firestore_v1.base_query import FieldFilter
from firebase_admin import credentials,firestore
cred = credentials.Certificate(r"D:\Athul\Miniproject\Main_prgm\Firebase_PvtKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
collection_ref = db.collection('userCollection')

class UserProfile():#ctk.Ctk):
    username=[]     #Name
    user_type={}    #Name and Type
    data=[]
    #def data(self):
        #un=collection_ref.get()
        #query=
       # for i in un:
           # userdata=i.to_dict()
           # name=userdata.get("Username")
           # self.username.append(name)
          #  self.user_type[name]=userdata.get("UserType")
        #print(self.username,self.user_type)
    def setData(self):
        field_filter=FieldFilter('Username','==','j1')
        query1=db.collection('userCollection').where(filter=field_filter)
        doc=query1.get()
        data=doc[0].to_dict()
        self.type=data['UserType']
    def video(self):
        field_filter = FieldFilter('uploadedBy', '==', 'j1')
        query1 = db.collection('videoData').where(filter=field_filter)
        doc=query1.get()
        for i in doc:
            i=i.to_dict()
            self.data.append(i['filename'])
        print(self.data)

        #col_ref=db.collection('userCollection').document(doc)


    def __init__(self,name,password):
        #self.title('')
        #self.data()
        self.name=name
        self.password=password
        print(self.name,self.password)
        self.setData()
        print(self.type)
        self.video()
UserProfile('j1','Password@234')