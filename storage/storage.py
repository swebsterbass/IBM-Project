# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:03:21 2020

@author: webst
"""

from firebase import firebase

# link to the database
connectionURL = "https://project-1095559261267193051.firebaseio.com/"

# the final argument is None because at the most the firebase project
# is in test mode so it does not require any kind of authentication
fb = firebase.FirebaseApplication(connectionURL, None)

data = {
        "Name":"test_name2",
        "Email":"test_name2@gmail.com",
        "Phone":1234567899
        }

# the string format is "\databsename\tablename"
# you do not need to specify the database in the url below because it will
# think you are trying to make a 2nd chart
result = fb.post("/Customers", data)
print(result)