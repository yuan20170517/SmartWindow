# Capture image
from picamera import PiCamera

camera = PiCamera()
camera.capture('/home/pi/Desktop/window.jpg')


# Upload image
from google.cloud import storage

client = storage.Client()

bucket = client.get_bucket('smartwindow-91b1c.appspot.com')

imageBlob = bucket.get_blob('window.jpg')
imageBlob.upload_from_filename(filename='/home/pi/Desktop/window.jpg')
