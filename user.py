from move_interface import AdiSphero

## Set your sphero name
sphero = AdiSphero("DEVICE-NAME")

## Test sphero connection: Run this if you want to test the connection to your sphero
# sphero.init_sphero()

## Orient sphero:
# TODO: Run orient_sphero() if you want to know where the sphero is pointing at.
# TODO: Change orientation_angle to get your 0° orientation relative to the sphero and field
orientation_angle = 0
def orient_sphero():
    sphero.orient_to_front(orientation_angle)

## Move sphero:
# TODO: Create your sphero path for soccer field 1
def move_sphero_field1():
    sphero.move_sphero(orientation_angle, heading=0, distance=0)

# TODO: Create your sphero path for soccer field 2
def move_sphero_field2():
    sphero.move_sphero(orientation_angle, heading=0, distance=0)

# TODO: Create your sphero path for soccer field 3
def move_sphero_field3():
    sphero.move_sphero(orientation_angle, heading=0, distance=0)
