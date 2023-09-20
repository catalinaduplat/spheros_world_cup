from img_recognitizon import get_coords
import math
from math import sqrt
import numpy as np

# def pix_to_cm(pix:int,cm:int):

#     one_pix:float =pix/cm
#     coorx_on_cm:float=float(dimensions[0])/one_pix
#     coory_on_cm:float=float(dimensions[1])/one_pix

#     return one_pix, coorx_on_cm, coory_on_cm

def get_parameters(x_final:int ,y_final:int, x_init:int, y_init:int, dimensions, pix,cm):


    #Get all x an y distances
    cathetus_x:float=int(x_init)-x_final
    cathetus_y:float=int(y_init)-y_final

    # print(cathetus_x,cathetus_y)
    # print(coords_sphero[0][0],coords_sphero[0][1])

    #Get the value of 1cm
    #one_pix,coorx_on_cm,coory_on_cm=pix_to_cm(506,20) # 506 px is equal to 20 cm
    one_pix:float =pix/cm
    coorx_on_cm:float=float(dimensions[0])/one_pix
    coory_on_cm:float=float(dimensions[1])/one_pix
    #convert the cathetus to cm
    cathetus_x:float=cathetus_x/one_pix
    cathetus_y:float=cathetus_y/one_pix
    print(cathetus_x,cathetus_y)

    #Get the value of teta
    teta=math.atan2(cathetus_y,cathetus_x)
    teta=np.degrees(teta)

    hypotenuse:float=sqrt((cathetus_x**2)+(cathetus_y**2))

    #the speed is constant 5
    time=(hypotenuse/5)-5

    return hypotenuse, teta, time

if __name__ == "__main__":
    coords_sphero, coords_obstacles,dimensions= get_coords('img/Boxes.png')
    print(get_parameters(1108,287))