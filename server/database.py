from  firebase_admin import db
import google as g
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("disaster.json")
firebase_admin.initialize_app(cred,{'databaseURL':"https://disaster101-231.firebaseio.com"})
people = db.reference("people/")
items = db.reference("items")
needs = db.reference("needs")
def createNeed():
    people = db.reference('people').get()
    items = db.reference('items').get()
def create_person(name, skills, hyper_trackId):
    return people.push({"needs":[], "name":name, "skills":skills, "hyper_track_id":hyper_trackId})
def create_item(name, lat, long):
        items.push({"name":name, "lat":lat, "long":long})
def create_need(name, lat, long, personID):
    people.child(personID).child("needs").push({"name":name, "lat":lat, "long":long})
id = create_person("test1", [{"category":"medical", "name":"doctor"}], "tesd")
create_item("test1", 37.773526, -122.415906)
create_need("test1", 37.773526, -122.415906, id.key)