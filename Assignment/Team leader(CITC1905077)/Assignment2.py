import random
import time
import winsound
while(1):
    temp=random.randint(0,100)
    humidity=random.randint(0,100)
    if temp>50:
        print("Alert!..temperature is detected as "+str(temp)+"degree celcius")
        duration=5000
        freq=500
        winsound.Beep(freq,duration)
    else:
        print("temperature is "+str(temp)+"degree celcius")
        time.sleep(1)