from  firebase_admin import db
import google as g
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred,{'databaseURL':"https://disaster101-231.firebaseio.com"})

def createNeed():
    people = db.reference('people').get()
    items = db.reference('items').get()
