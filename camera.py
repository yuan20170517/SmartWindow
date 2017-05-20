from google.cloud import storage
from picamera import PiCamera

# Capture image
camera = PiCamera()
camera.capture('/home/pi/Desktop/window.jpg')


# Upload image
client = storage.Client()

bucket = client.get_bucket('smartwindow-91b1c.appspot.com')

imageBlob = bucket.get_blob('window.jpg')
imageBlob.upload_from_filename(filename='/home/pi/Desktop/window.jpg')