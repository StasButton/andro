#import os
#import uvicorn
#from fastapi import FastAPI, File, UploadFile
#from fastapi.responses import FileResponse

import io
import streamlit as st
from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions
import numpy as np


@st.cache(allow_output_mutation=True)

def load_image():
    uploaded_file = st.file_uploader(label='Выберите изображение для распознавания')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        return Image.open(io.BytesIO(image_data))
    else:
        return None

st.title('Классификации изображений в облаке')
img = load_image()


