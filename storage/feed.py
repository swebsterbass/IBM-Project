# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:21:43 2020

@author: webst
"""
from datetime import datetime
from firebase import firebase


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


import os
dirname = os.path.dirname(__file__)
# filename = os.path.join(dirname, 'relative/path/to/file/you/want')



# link to the database
project_id = "project-1095559261267193051"
connectionURL = "https://project-1095559261267193051.firebaseio.com/"
# need to convert the below string from a normal string to a raw string
# this conversion can occur by putting an r in front of the string
# credPath = r"C:\Users\webst\OneDrive\Academic FIles\2020-21 SEN\0th semester\ibm\group project\IBM-Project\storage\project-1095559261267193051-firebase-adminsdk-fltiq-a3ddfe6a1f.json"
credPath = os.path.join(dirname, 'project-1095559261267193051-firebase-adminsdk-fltiq-a3ddfe6a1f.json')
print(credPath)
feedChunkSize = 5

class post():
    
    def __init__(self, title, author, des, stars, ofn, oln, dt, st, city):
        """
        input: title, description, stars, officer first name, officer last name,
            datetime, state, city
            
        """
        self.title = title
        self.author = author
        self.description = des
        self.stars = stars
        self.officerFirstName = ofn
        self.officerLastName = oln
        self.dateTime = datetime.datetime.now()
        self.state = st
        self.city = city.casefold()
        



def clear():
    """
    empties the database
    
    """
    # the final argument is None because at the most the firebase project
    # is in test mode so it does not require any kind of authentication
    fb = firebase.FirebaseApplication(connectionURL, None)
    
    
    # the string format is "\databsename\tablename"
    result = fb.get("/Customers", '')
    print(result)
    

def search(keyword, field):
    return
    # the final argument is None because at the most the firebase project
    # is in test mode so it does not require any kind of authentication
    fb = firebase.FirebaseApplication(connectionURL, None)
    
    
    # the string format is "/databasename/tablename"
    result = fb.get("/Customers", '-MCZFBAthRAFEgANf_vS')
    print(result)
    


# firestore database code
def submitPost(db):
    
    # apparently when you do from datetime import datetime
    # you just write datetime.now()
    # i think that if you write import datetime, then you 
    # have to write datetime.datetime.now()
    data = {
        u'title': u'Hello, World!',
        u'author': u'Harry',
        u'description': u'interesting experience',
        u'stars': 3,
        u'officerFirstName': "Soldier",
        u'officerLastName': "Man",
        u'dateTime': datetime.now(),
        u'state': "FL",
        u'city': "Jacksonville",
        }
    
    db.collection(u'posts').document(u'one').set(data)
    
    return None
    

def populateDatabase(db):
    
    # apparently when you do from datetime import datetime
    # you just write datetime.now()
    # i think that if you write import datetime, then you 
    # have to write datetime.datetime.now()
    data = {
        u'title': u'Hello, World!',
        u'author': u'Harry',
        u'description': u'interesting experience',
        u'stars': 3,
        u'officerFirstName': "Soldier",
        u'officerLastName': "Man",
        u'dateTime': datetime.now(),
        u'state': "FL",
        u'city': "Jacksonville",
        }
    
    db.collection(u'posts').document(u'1').set(data)
    
    data = {
        u'title': u'Hello, World!',
        u'author': u'Billy',
        u'description': u'horrible experience',
        u'stars': 1,
        u'officerFirstName': "Tan",
        u'officerLastName': "Dilly",
        u'dateTime': datetime.now(),
        u'state': "GA",
        u'city': "Jacksonville",
        }
    
    db.collection(u'posts').document(u'2').set(data)
    
    data = {
        u'title': u'Hello, World!',
        u'author': u'Casear',
        u'description': u'horrible experience',
        u'stars': 5,
        u'officerFirstName': "Tan",
        u'officerLastName': "Dilly Dad",
        u'dateTime': datetime.now(),
        u'state': "FL",
        u'city': "Jacksonville",
        }
    
    db.collection(u'posts').document(u'3').set(data)
    
    data = {
        u'title': u'Hated Every Moment!',
        u'author': u'Daniel',
        u'description': u'an experience',
        u'stars': 0,
        u'officerFirstName': "Tan",
        u'officerLastName': "Dilly Dad",
        u'dateTime': datetime.now(),
        u'state': "FL",
        u'city': "Jacksonville",
        }
    
    db.collection(u'posts').document(u'4').set(data)
    
    data = {
        u'title': u'Livid',
        u'author': u'Emma',
        u'description': u'i nearly died',
        u'stars': 0,
        u'officerFirstName': "Racist",
        u'officerLastName': "Police Officer",
        u'dateTime': datetime.now(),
        u'state': "FL",
        u'city': "Jacksonville",
        }
    
    db.collection(u'posts').document(u'5').set(data)
    
    data = {
        u'title': u'No Way!!!!',
        u'author': u'Fabio Leo',
        u'description': u'i nearly died',
        u'stars': 0,
        u'officerFirstName': "Very Racist",
        u'officerLastName': "Police Officer",
        u'dateTime': datetime.now(),
        u'state': "FL",
        u'city': "Jacksonville",
        }
    
    db.collection(u'posts').document(u'6').set(data)
    
    data = {
        u'title': u'Ok',
        u'author': u'Insignificant User',
        u'description': u'nothing happened',
        u'stars': 5,
        u'officerFirstName': "Goody",
        u'officerLastName': "Good",
        u'dateTime': datetime.now(),
        u'state': "TX",
        u'city': "Houston",
        }
    
    db.collection(u'posts').document(u'7').set(data)
    
    return None

    
def searchFirestore(db, city, state):
    posts_ref = db.collection(u'posts')
    docs = None
    
    #query_ref = posts_ref.where(u'state', u'==', state).where(u'city', u'==',city)
    query_ref = posts_ref.where(u'state', u'==', state).where(u'city', u'==',city).order_by(u'dateTime', u'DESCENDING').limit(feedChunkSize)
    docs = query_ref.stream()
    
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
    
    
    

# def searchFirestoreByDesc(db, keywords):
#     posts_ref = db.collection(u'posts')
#     docs = None
    
#     #query_ref = posts_ref.where(u'state', u'==', state).where(u'city', u'==',city)
#     query_ref = posts_ref.where(u'state', u'==', state).where(u'city', u'==',city).order_by(u'dateTime', u'DESCENDING').limit(feedChunkSize)
#     docs = query_ref.stream()
    
#     for doc in docs:
#         print(f'{doc.id} => {doc.to_dict()}')

    
if __name__ == "__main__":
    # search("hello", "title")
    
    # Use the application default credentials
    # this method does not work
    # cred = credentials.ApplicationDefault()
    # firebase_admin.initialize_app(cred, {
    #   'projectId': project_id,
    # })
    
    
    cred = credentials.Certificate(credPath)
    default_app = firebase_admin.initialize_app(cred)
    
    # either one of these commands work.
    # db = firestore.client()
    db = firebase_admin.firestore.client()
    # submitPost(db)
    populateDatabase(db)
    searchFirestore(db, u"Jacksonville", u"FL")