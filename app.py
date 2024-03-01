import streamlit as st
from PIL import Image
import numpy as np

def main():
    st.markdown("<h1 style='text-align: center; color: white;'>Welcome to True View!</h1>", unsafe_allow_html=True)
    
    image_file_buffer = st.camera_input("")
    
    if image_file_buffer is not None:
        image = Image.open(image_file_buffer)
        img_array = np.array(image)
        
        if "messages" not in st.session_state:
            st.session_state.messages = []
            
        for i  in range(len(st.session_state.messages)):
            agent = st.session_state.messages[i]["role"]
            agent_content = st.session_state.messages[i]["content"]
            
            with st.chat_message(agent):
                st.write(agent_content)
        
        user_input = st.chat_input("Please enter your question here...")
        if user_input:
            with st.chat_message("user"):
                st.markdown(user_input)
                
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            bot_response = "I am a bot, I am here to help you with your questions."
            with st.chat_message("assistant"):
                st.markdown(bot_response)
                
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
        
    
    
if __name__ == "__main__":
    main()