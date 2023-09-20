from move_interface import AdiSphero

# Set your sphero name
sphero = AdiSphero("SM-1D91")

# Test sphero connection
# sphero.init_sphero()

# Orient sphero
orientation_angle = 0
# sphero.orient_to_front(orientation_angle)

# Move sphero
calculator_angle = 0
calculator_distance = 40
sphero.move_sphero(orientation_angle, heading=calculator_angle, distance=calculator_distance)
