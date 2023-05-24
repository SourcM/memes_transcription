import streamlit as st
import easyocr
import numpy as np
# import cv2
# import matplotlib.pyplot as plt
# %matplotlib inline
from PIL import Image, ImageOps

 
@st.cache(allow_output_mutation=True)

# with st.spinner('Model is being loaded..'):
reader = easyocr.Reader(['en'])
 
st.write("""
         # Memes Understanding
         """
         )
 
file = st.file_uploader("Upload the meme image", type=["jpg", "png"])
st.set_option('deprecation.showfileUploaderEncoding', False)
 

if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    image = np.asarray(image)
    image = image[:,:,::-1]
    result = reader.readtext(img)
    for detection in result: 
        text = detection[1]
        st.write(text)
