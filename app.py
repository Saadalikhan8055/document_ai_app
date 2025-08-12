import streamlit as st
import os
from backendpy import process_document, ask_question

st.set_page_config(page_title="AI PDF Chatbot with Memory", layout="wide")
st.title("📄 AI PDF Chatbot with Memory")

# Initialize chat history and retriever in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "retriever" not in st.session_state:
    st.session_state.retriever = None

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User upload section
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    # Check if a file has been uploaded and processed
    if st.session_state.retriever is None:
        st.success("File uploaded!")

        # Save the uploaded file temporarily and process it
        file_path = os.path.join("data", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
            
        with st.spinner("Processing PDF..."):
            st.session_state.retriever = process_document(file_path)
            st.success("PDF processed. Start chatting!")
            
    # Chat input section
    prompt = st.chat_input("Ask a question about the document:")
    if prompt:
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = ask_question(prompt)
            st.write(response)
        
        # Add AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
