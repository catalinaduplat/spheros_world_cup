import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

class AdiSphero: 
    def __init__(self, name: str) -> None:
        self.name = name

    def init_sphero(self):
        toy = scanner.find_toy(toy_name=self.name)
        with SpheroEduAPI(toy) as droid:
            droid.set_main_led(Color(r=0, g=0, b=255))
            return droid

    def _move(self, heading: int, duration: float):        
        toy = scanner.find_toy(toy_name=self.name)
        with SpheroEduAPI(toy) as droid:
            droid.set_main_led(Color(r=0, g=0, b=255))
            droid.roll(heading=heading, speed =5, duration=duration)
            print(droid.get_distance())
    
    def orient_to_front(self, desired_orientation: int):
        toy = scanner.find_toy(toy_name=self.name)
        with SpheroEduAPI(toy) as droid:
            droid.set_back_led(255)
            droid.set_heading(desired_orientation)
            time.sleep(10)

    def _move_step(self, heading: int, droid: SpheroEduAPI):
        droid.roll(heading=heading, speed=1, duration=0.8)
        droid.stop_roll()
        return droid.get_distance()


    def move_sphero(self, heading: int, distance: float):        
        toy = scanner.find_toy(toy_name=self.name)
        with SpheroEduAPI(toy) as droid:
            droid.set_main_led(Color(r=0, g=0, b=255))
            current_distance = 0
            delta = 4
            while True:
                print(current_distance)
                if current_distance >= (distance - delta):
                    break
                else:
                    current_distance = self._move_step(heading, droid)
