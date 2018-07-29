from  firebase_admin import db
import google as g
import firebase_admin
from firebase_admin import credentials
import numpy as np

cred = credentials.Certificate("disaster.json")
firebase_admin.initialize_app(cred,{'databaseURL':"https://disaster101-231.firebaseio.com"})

def createNeed():
    people = db.reference('people').get()
    items = db.reference('items').get()
    needs = {}
    # for person in people:
    #     for need in
    print(people)
    er = 6731 #km
    def hav(t1,t2,l1,l2):
        a = np.sin((np.rad2deg(t1-t2))/2)**2+np.cos(np.radians(t1))*np.cos(np.radians(t2))*np.sin((np.radians(l1-l2))/2)**2
        c = 2*np.arctan2(np.sqrt(a),np.sqrt(1-a))
        return er*c
    close = 5 #km distance

createNeed()