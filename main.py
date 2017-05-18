import time

# initialise Firebase data stream
import stream

# while loop with delay
while 1:

    # check rain sensor
    import rainsensor

    # check temp/humidity sensor
    import humTempSensor

    # update values to server
    import upload

    # 5 minutes delay
    time.sleep(300)