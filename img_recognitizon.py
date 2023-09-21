import cv2
import numpy as np
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

def get_coords(image):
    # image= cv2.imread(image)
    dimensions=image.shape
    print('Image Dimension    : ',dimensions)
    original_image= image
    image = cv2.blur(image, (30,30), cv2.BORDER_CONSTANT)
    lowerValues_rect = np.array([60, 120, 120])
    upperValues_rect = np.array([117, 255, 255])

    #myColors_sphero = [[0,0,255,179,83,255]]    
    lowerValues = np.array([0,0,168])
    upperValues = np.array([172,111,255])
    #mask for sphero
    hsv= cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lowerValues, upperValues)
    mask_rect = cv2.inRange(hsv, lowerValues_rect, upperValues_rect)
    contours_rect, hierarchy= cv2.findContours(mask_rect.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # find countours
    contours, hierarchy= cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    approx_shapes = [cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True) for 
                    contour in contours]
    #for sphero
    mu = [None]*len(contours)
    mc = [None]*len(contours)
    for i in range(len(contours)):
    # Get the mass centers
        mu[i] = cv2.moments(contours[i])
    # add 1e-5 to avoid division by zero
        mc[i] = (mu[i]['m10'] / (mu[i]['m00'] + 1e-5), mu[i]['m01'] / (mu[i]['m00'] + 1e-5))
    
    #for obstacle
    mu_rect = [None]*len(contours_rect)
    mc_rect = [None]*len(contours_rect)
    for i in range(len(contours_rect)):
    # Get the mass centers
        mu_rect[i] = cv2.moments(contours_rect[i])
    # add 1e-5 to avoid division by zero
        mc_rect[i] = (mu_rect[i]['m10'] / (mu_rect[i]['m00'] + 1e-5), mu_rect[i]['m01'] / (mu_rect[i]['m00'] + 1e-5)) 
    # Draw contours
    drawing = np.zeros((mask.shape[0], mask.shape[1], 3), dtype=np.uint8)
    drawing_rect = np.zeros((mask_rect.shape[0], mask_rect.shape[1], 3), dtype=np.uint8)

    coords_sphero = []
    for i,approx_shape in enumerate(approx_shapes):
        if len(approx_shape) > 10:

            coords_sphero.append([int(mc[i][0]), int(mc[i][1])])
            color = (255, 0, 0)
            cv2.drawContours(drawing, contours, i, color, 2)
            cv2.putText(drawing,str([int(mc[i][0]), int(mc[i][1])]),[int(mc[i][0]), int(mc[i][1])],cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255))
            cv2.circle(drawing, (int(mc[i][0]), int(mc[i][1])), 4, (0,0,255), -1)

    image_bytes_sphero = cv2.imencode(".jpg", drawing)[1].tobytes()
    # print(f"""
    #     ******Coords Spheros******  
          
    #       coords sphero:
    #         sphero 1X : {coords_sphero[0][0]}
    #         sphero 1Y : {coords_sphero[0][1]}
    #         sphero 2X : {coords_sphero[1][0]}
    #         sphero 2Y : {coords_sphero[1][1]}
            
    #     ******Coords Rectangles******
    #         """) 

    coords_rect = []
    for i in range(len(contours_rect)):
        color_rect = (0, 255, 0)
        cv2.drawContours(drawing_rect, contours_rect, i, color_rect, 2)
        cv2.putText(drawing_rect,
                    str([int(mc_rect[i][0]),
                    int(mc_rect[i][1])]),
                    [int(mc_rect[i][0]), int(mc_rect[i][1])],
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255,255,255))
        cv2.circle(drawing_rect, (int(mc_rect[i][0]), int(mc_rect[i][1])), 4, color_rect, -1)
        coords_rect.append([int(mc_rect[i][0]), int(mc_rect[i][1])])

    # for i, coord in enumerate(coords_rect):
    #     print(f"""
    #         coords Rectangle {i}:
    #             rect {i}X : {coord[0]}
    #             rect {i}Y : {coord[1]}""") 

    # cv2.imshow('Original', original_image)
    # cv2.imshow('Blurred', image)
    # cv2.imshow('Contours', drawing)
    # cv2.imshow('Contours_rect', drawing_rect)
    # cv2.waitKey()
    # Convert the CV2 image to bytes
    image_bytes_rect = cv2.imencode(".jpg", drawing_rect)[1].tobytes()

    # Display the CV2 image in Streamlit
    

    return coords_sphero, coords_rect, dimensions, image_bytes_rect, image_bytes_sphero

def sphero_init():
    toy = scanner.find_toy(toy_name="SM-8CEB")
    with SpheroEduAPI(toy) as droid:
        droid.set_main_led(Color(r=0, g=0, b=255))

if __name__ == "__main__":
    get_coords("img/many_sphero.jpg")