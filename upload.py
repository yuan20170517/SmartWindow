import pyrebase

config = {
  "apiKey": "AIzaSyDsZmfthgZvJbFLSWNOwCJGOMZnBhKMnDI",
  "authDomain": "smartwindow-91b1c.firebaseapp.com",
  "databaseURL": "https://smartwindow-91b1c.firebaseio.com/",
  "storageBucket": "smartwindow-91b1c.appspot.com",
  "serviceAccount": "/home/pi/Desktop/SmartWindow/key.json"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()


# update data
data = {"opened": "1", "rain":"0"}
db.update(data)