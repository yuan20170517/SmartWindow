import time

# input humidity sensor threshold level
humidity_threshold = float(input("Set humidity level: "))
# input temperature threshold level
temp_threshold = float(input("Set temperature level: "))

retest = 0

# logic to open or close window
while 1:
    time.sleep(5)  # check time after some time e.g. 30 min
    # check rain sensor output: Raining is 1 and Not Raining is 0
    rain = int(input("rain droplets? yes (press 1) or no (press 0): "))

    if rain == 1:
        # check humidity sensor output: Raining if more than 50
        humidity = float(input("Enter humidity level: "))
        if humidity > humidity_threshold:
            # check temperature sensor output: Raining if less than 24.0
            temp = float(input("Enter temperature: "))
            if temp < temp_threshold:
                print("very likely to be raining")
                print("power motor to close window")
            else:
                time.sleep(2)  # check time after some time e.g. 1 min
                retest += 1  # count the number of retests
                temp = float(input("Retest Enter temperature: "))
        else:
            time.sleep(2)  # check time after some time e.g. 1 min
            retest += 1  # count the number of retests
            humidity = float(input("Retest humidity level: "))
    else:
        print("not raining")
        print("power motor to open window")
    # ask for user input if retests more than 2 times
    if retest > 2:
        print("request user input")
        retest = 0
        break
