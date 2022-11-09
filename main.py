import io
import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.preprocessing import image

def load_image():
    uploaded_file = st.file_uploader(label='Выберите изображение для распознавания')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        ib = Image.open(io.BytesIO(image_data))
        return ib 
    else:
        return None


st.title('Классификации изображений в облаке Streamlit')
io = load_image()
st.download_button(label='скачать', data=io)
