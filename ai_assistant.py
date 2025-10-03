import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("API_KEY"))

# Initialize the model
model = genai.GenerativeModel('gemini-2.5-flash-lite')

# Set up Streamlit UI
st.title("🤖 AI Assistant for Deepika")
st.markdown("""
This assistant uses Google's Gemini 2.5 flash-lite model to answer your questions.
Type your query below and press **Send** to get a response.
""")

# Initialize session state for chat history
if 'history' not in st.session_state:
    st.session_state.history = []
    
# Chat interface
user_input = st.chat_input("Type your message here...")

if user_input:
    with st.spinner('Generating response...'):
        try:
            response = model.generate_content(user_input)
            st.session_state.history.append({"role": "user", "content": user_input})
            st.session_state.history.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")

# Display chat history
for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Add clear chat button
if st.button("Clear Chat"):
    st.session_state.history = []
    st.experimental_rerun()
