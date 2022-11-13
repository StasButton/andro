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
        return Image.open(io.BytesIO(image_data))  
    else:
        return None

st.title('Загрузка, скачивание изображений')

s = load_image()
if s is not None:
    st.download_button(label='скачать',data=s,file_name = 'O.jpg')
    
'''
img = load_image()
result = st.button('Распознать изображение')
if result:
    #x = preprocess_image(img)
    #preds = model.predict(x)
    st.write('**Результаты распознавания:**')
    #print_predictions(preds)
'''
