import io
import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.preprocessing import image

def load_image():
    uploaded_file = st.file_uploader(label='Выберите изображение')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        s = Image.open(io.BytesIO(image_data))
        return image_data 
    else:
        return None

st.title('Классификации изображений в облаке Streamlit')
s = load_image()
if s is not None:
    st.download_button(label='скачать',data=s,file_name = 'O.jpg')



