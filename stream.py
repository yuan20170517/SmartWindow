import pyrebase

# initialise
config = {
  "apiKey": "AIzaSyDsZmfthgZvJbFLSWNOwCJGOMZnBhKMnDI",
  "authDomain": "smartwindow-91b1c.firebaseapp.com",
  "databaseURL": "https://smartwindow-91b1c.firebaseio.com/",
  "storageBucket": "smartwindow-91b1c.appspot.com",
  "serviceAccount": "/home/pi/Desktop/SmartWindow/key.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# create stream
def stream_handler(message):
  opened = db.child("opened").get().val()
  rain = db.child("rain").get().val()
  print opened
  print rain

my_stream = db.stream(stream_handler)