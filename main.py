import io
import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.preprocessing import image

from tensorflow.keras import utils
#ar = np.random.randint(0, 255, (28,28,3))


def load_image():
    uploaded_file = st.file_uploader(label='Выберите изображение')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        img = Image.open(io.BytesIO(image_data))
        #
        ar = np.array(img)
        img = utils.array_to_img(ar)
        
        img_byte_arr = io.BytesIO(ar)
        img.save(img_byte_arr, format='PNG')
        image_data_arr = img.getvalue()
        
        #st.text(type(ar))
        return  image_data 
    else:
        return None

st.title('Загрузка, скачивание изображений')

s = load_image()
if s is not None:
    st.download_button(label='скачать',data=s,file_name = 'O.jpg')
