# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 19:16:07 2020

@author: webst
"""
from firebase import firebase

# link to the database
connectionURL = "https://project-1095559261267193051.firebaseio.com/"

# the final argument is None because at the most the firebase project
# is in test mode so it does not require any kind of authentication
fb = firebase.FirebaseApplication(connectionURL, None)

# the string format is "\databsename\tablename"
result = fb.get("/Customers", '')
print(result)