#

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from ultralytics import YOLO
import cv2
from collections import Counter
from streamlit_player import st_player
from PIL import Image
import cv2
import numpy as np
from collections import Counter
from ultralytics import YOLO
import time
from IPython.display import display, clear_output
from PIL import Image
from matplotlib import pyplot as plt


st.title("WELCOME TO DEEP BEAUTY")

st.write("This is Bel Lüscher talking, a former makeup artist turned into data analyst. Here you can find a way to do the makeup yourself, through the power of machine learning. Be the machine yourself and learn to do the best makeup for your own eyeshape!")

st.write("---")

# Load the model
model_path = "/Users/belluscher/Library/CloudStorage/OneDrive-Pessoal/A_IRONHACK/Week_8/Face_Recognition/train9Xobject150/weights/best.pt"
model = YOLO(model_path)
class_names = {0: 'almond', 1: 'deep-set', 2: 'downturned', 3: 'hooded', 4: 'monolid', 5: 'protuding', 6: 'round', 7: 'upturned'}

# Define a function to run the model and get the prediction
def get_prediction(image):
    results = model(image)
    class_labels = results[0].boxes.cls
    if class_labels is not None:
        mode_result = Counter(class_labels.tolist()).most_common(1)[0][0]
        return class_names.get(mode_result)
    return None

# Initialize session state for prediction result
if 'prediction' not in st.session_state:
    st.session_state.prediction = None

option = st.selectbox("DISCOVER YOUR EYE SHAPE", ("Upload a photo", "Use the camera"))

if option == "Upload a photo":
    uploaded_file = st.file_uploader("Upload to discover your EYE SHAPE", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image = np.array(image)

        # Run the model on the image
        results = model(image)

        # Render the results on the image
        result_img = results[0].plot()
        st.image(result_img, caption='Uploaded Image', use_column_width=True)
        if st.session_state.prediction is None:
            st.session_state.prediction = get_prediction(image)
else:
    if st.session_state.prediction is None:
        cap = cv2.VideoCapture(1)
        class_labels_accumulated = []
        start_time = time.time()
        try:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                results = model(frame)
                class_labels = results[0].boxes.cls
                if class_labels is not None:
                    class_labels_accumulated.extend(class_labels.tolist())
                if time.time() - start_time > 7:
                    break
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()
            if class_labels_accumulated:
                mode_result = Counter(class_labels_accumulated).most_common(1)[0][0]
                st.session_state.prediction = class_names.get(mode_result)

if st.session_state.prediction:
    st.write(f"Predicted Eye Shape: {st.session_state.prediction}")
    if st.button("See the suggested Makeup Tutorials"):
        if st.session_state.prediction == 'protuding':
            st.write("Makeup for PROTRUDING eyes")
            st.write("Makeup by Saz")
            st_player("https://www.youtube.com/watch?v=UPnGfCs6IgE")
            st.write("Sam Young")
            st_player("https://www.youtube.com/watch?v=XkEq9TqpOXA&t=2s")
            st.write("Advise My Style p")
            st_player("https://www.youtube.com/watch?v=UPnGfCs6IgE")
        elif st.session_state.prediction == 'hooded':
            st.write("Makeup for HOODED eyes")
            st.write("Michaella")
            st_player("https://www.youtube.com/watch?v=AWOlM4qkoDg")
            st.write("Risa Does Makeup")
            st_player("https://www.youtube.com/watch?v=u4XZi7IGfB4")
            st.write("Brittany Nichole")
            st_player("https://www.youtube.com/watch?v=kHnAS4NJuWU&list=PL0ajLoeF4OjrulRIyQXhQMJidgK2xbiYX")
        elif st.session_state.prediction == 'almond':
            st.write("Makeup for ALMOND eyes")
            st.write("Melissa Van Dijk")
            st_player("https://www.youtube.com/watch?v=E5sn6LNBSoM")
            st.write("Jean Watts")
            st_player("https://www.youtube.com/watch?v=JPUbSvsxjsY&list=PLkjw3goLraSrg1CFmwgFf2le4kU6xMrPN")
            st.write("Leah Halton")
            st_player("https://www.youtube.com/watch?v=02xfgtxL9RA")
        elif st.session_state.prediction == 'deep-set':
            st.write("Makeup for DEEP_SET eyes")
            st.write("Hung Vanngo")
            st_player("https://www.youtube.com/watch?v=ntJwR5VInxw")
            st.write("Bobbi Brown Cosmetics")
            st_player("https://www.youtube.com/watch?v=Rysc1Iw2V3k")
            st.write("Danielle Donnelly")
            st_player("https://www.youtube.com/watch?v=mpZo-0JuBTA")
            st.write("Ali Andreea")
            st_player("https://www.youtube.com/watch?v=E1JsJEObDM4")
        elif st.session_state.prediction == 'downturned':
            st.write("Makeup for DOWNTURNED eyes")
            st.write("Risa Does Makeup")
            st_player("https://www.youtube.com/watch?v=K6uUE9md19g")
            st.write("Jen Phelps")
            st_player("https://www.youtube.com/shorts/JP7p_ud-ZRc")
            st.write("Makeup and Art Freak")
            st_player("https://www.youtube.com/watch?v=5CjhSxVBA2U")
        elif st.session_state.prediction == 'monolid':
            st.write("Makeup for MONOLID eyes")
            st.write("Jenny Moon")
            st_player("https://www.youtube.com/shorts/YwNjlXHoiyE")
            st.write("Fenty Beauty")
            st_player("https://www.youtube.com/watch?v=QWZl5ujH8uE")
            st.write("Elaine Park")
            st_player("https://www.youtube.com/watch?v=wWTnS89NutM")
        elif st.session_state.prediction == 'round':
            st.write("Makeup for ROUND eyes")
            st.write("Mallory Osses")
            st_player("https://www.youtube.com/watch?v=8XCpevgyStc")
            st.write("Raluca Makeup")
            st_player("https://www.youtube.com/watch?v=Bqv7b-J9iIo")
            st.write("Raluca Makeup 2")
            st_player("https://www.youtube.com/watch?v=umyd2cjXWPI")
        elif st.session_state.prediction == 'upturned':
            st.write("Makeup for UPTURNED eyes")
            st.write("Ariana Grande")
            st_player("https://www.youtube.com/watch?v=MdLcP8dJls4")
            st.write("Rachel OCool")
            st_player("https://www.youtube.com/watch?v=Fjnew2Maq20")
            st.write("Advise My Style")
            st_player("https://www.youtube.com/watch?v=d6exsQPLK_U")
        else:
            st.write("We're still building the makeup Library. Hang on!")





