import streamlit as st
from img_recognitizon import get_coords
from parameters_estimator import get_parameters
import cv2
import numpy as np

st.title("Welcome to Spheros World Cup")

st.sidebar.header("Spheros World Cup")
img_file_buffer = st.camera_input("Take a picture")

def get_image():
    if img_file_buffer is not None:
        # To read image file buffer with OpenCV:
        bytes_data = img_file_buffer.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        return cv2_img

# If the user selects "View teams", show a list of all the teams in the tournament.
# if st.sidebar.checkbox("View teams"):
# st.table(data=[[team.name, team.country] for team in teams])

# If the user selects "View matches", show a list of all the matches in the tournament.
# if st.sidebar.checkbox("View matches"):
# st.table(data=[[match.home_team, match.away_team, match.date, match.time] for match in matches])

photo = get_image()
if photo is not None:
    # Show map
    header_coords = st.header("Get initial positions of spheros")
    coords_sphero, coords_obstacles, dimensions, image_bytes_rect, image_bytes_sphero= get_coords(photo)

    st.text("Sphero 1 coor x: " +str(coords_sphero[0][0]))
    st.text("Sphero 1 coor y: " +str(coords_sphero[0][1]))
    st.text("Sphero 2 coor x: " +str(coords_sphero[1][0]))
    st.text("Sphero 2 coor y: " +str(coords_sphero[1][1]))

    sphero_params_cont = st.container()
    image_cont = st.container()
        

    with sphero_params_cont:
        header_params = st.header("Get Parameters for Sphero", divider="orange")
        st.markdown("""Insert the coordinates of the point you want your sphero to go.
            This tool will transform your input to the needed parameters for your sphero's movements""")
        st.image(image_bytes_sphero, caption="Rectangles")
        st.image(image_bytes_rect, caption="Rectangles")
        col1, col2 = st.columns(2)
        with col1:
            x_coord_init = st.number_input("Insert the initial x coordinate", key="x_init", step=1)
            x_coord_final = st.number_input("Insert the objective x coordinate", key="x_final", step=1)
        with col2:
            y_coord_init = st.number_input("Insert the initial y coordinate", key="y_init", step=1)
            y_coord_final = st.number_input("Insert the objective y coordinate", key="y_final", step=1)
        
        distance, angle, time = get_parameters(x_coord_final, y_coord_final, x_coord_init, y_coord_init,pix=506,cm=20,dimensions=dimensions)

    col1_result, col2_result, col3_result = st.columns(3)

    with col1_result:
        distance_metric = st.metric(label="Distance", value=str(distance) + " cm", help= "Minimum distance between your sphero and the coordinate")
    with col2_result:
        angle_metric = st.metric(label="Angle", value=str(angle) + " °", help= "Angle the sphero needs to head to")
    with col3_result:
        time_metric = st.metric(label="Time", value=str(time) + " s", 
        help= "The time your sphero should take to go to the destination at a constant speed")