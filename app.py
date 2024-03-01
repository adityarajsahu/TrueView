import streamlit as st
from PIL import Image
import numpy as np
from transformers import ViltProcessor, ViltForQuestionAnswering

def main():
    st.markdown("<h1 style='text-align: center; color: white;'>Welcome to True View!</h1>", unsafe_allow_html=True)
    
    processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
    model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
    
    image_file_buffer = st.camera_input("")
    
    if image_file_buffer is not None:
        image = Image.open(image_file_buffer)
        # img_array = np.array(image)
        
        if "messages" not in st.session_state:
            st.session_state.messages = []
            
        for i  in range(len(st.session_state.messages)):
            agent = st.session_state.messages[i]["role"]
            agent_content = st.session_state.messages[i]["content"]
            
            with st.chat_message(agent):
                st.write(agent_content)
        
        user_input = st.chat_input("Please enter your question regarding the image here...")
        if user_input:
            with st.chat_message("user"):
                st.markdown(user_input)
                
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            encoding = processor(image, user_input, return_tensors="pt")
            outputs = model(**encoding)
            logits = outputs.logits
            idx = logits.argmax(-1).item()
            bot_response = model.config.id2label[idx]
            with st.chat_message("assistant"):
                st.markdown(bot_response)
                
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
        
    
    
if __name__ == "__main__":
    main()