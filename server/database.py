from  firebase_admin import db
import google as g
import firebase_admin
from firebase_admin import credentials
import numpy as np

cred = credentials.Certificate("disaster.json")
firebase_admin.initialize_app(cred,{'databaseURL':"https://disaster101-231.firebaseio.com"})
people = db.reference("people/")
items = db.reference("items")
needs = db.reference("needs")
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

def create_person(name, skills, hyper_trackId):
    return people.push({"needs":[], "name":name, "skills":skills, "hyper_track_id":hyper_trackId})
def create_item(name, lat, long):
        items.push({"name":name, "lat":lat, "long":long})
def create_need(name, lat, long, personID):
    people.child(personID).child("needs").push({"name":name, "lat":lat, "long":long})
# id = create_person("test1", [{"category":"medical", "name":"doctor"}], "tesd")
# create_item("test1", 37.773526, -122.415906)
# create_need("test1", 37.773526, -122.415906, id.key)

