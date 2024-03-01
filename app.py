import streamlit as st
from PIL import Image
import numpy as np

def main():
    st.markdown("<h1 style='text-align: center; color: white;'>Welcome to True View!</h1>", unsafe_allow_html=True)
    image_file_buffer = st.camera_input("Click a picture")
    
    if image_file_buffer is not None:
        image = Image.open(image_file_buffer)
        img_array = np.array(image)
        
        st.image(image, caption="Captured Image", use_column_width=True)
    
    
if __name__ == "__main__":
    main()