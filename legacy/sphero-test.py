import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

toy = scanner.find_toy(toy_name="SM-8CEB")
with SpheroEduAPI(toy) as droid:
    droid.set_main_led(Color(r=0, g=0, b=255))
    #droid.set_speed(60)
    #i=0
    #while True:    
        # droid.set_speed(5)
        # time.sleep(1)
        # droid.set_heading(0)
        #droid.roll(i,speed=5,duration=2)
        #i=i+30
        # time.sleep(1)
        # droid.set_heading(90)
        # droid.roll(90,speed=10,duration=1)
        # time.sleep(1)
        # droid.set_heading(180)
        # droid.roll(180,speed=10,duration=1)
        # time.sleep(1)
        # droid.set_heading(270) 
        # time.sleep(1)
        # droid.set_speed(0)
        # droid.roll(270,speed=10,duration=1)
        #droid.set_heading(360)       
        # drodroid.roll(speed=10,duration=1)id.roll(90,30,5)
        # print("roll 1")
        # droid.stop_roll(180)
        # print("stoped")
        # droid.set_speed(35)
        # droid.set_speed(0)
        #print("stoped")