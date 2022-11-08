#import os
#import uvicorn
#from fastapi import FastAPI, File, UploadFile
#from fastapi.responses import FileResponse

import io
import streamlit as st
from PIL import Image
import numpy as np


@st.cache(allow_output_mutation=True)
def load_model():
    return 'OK'

st.title('Классификации изображений в облаке')


