import streamlit as st
from src.help import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain

def user_input(user_question):
    # Call the conversational chain with the user's question
    if st.session_state.conversation:
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chatHistory = response['chat_history']
        
        for i, message in enumerate(st.session_state.chatHistory):
            if i % 2 == 0:
                st.write("User: ", message.content)
            else:
                st.write("Reply: ", message.content)

def main():
    st.set_page_config(page_title="ANSWER ME", page_icon="💁")  # Corrected for page title and icon
    st.header("PDF Q&A System 💁")

    user_question = st.text_input("Ask a Question from the PDF Files")

    # Initialize conversation and chat history if they don't exist
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = []

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)
        
        if st.button("Submit & Process"):
            if pdf_docs:  # Ensure files were uploaded
                with st.spinner("Processing..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    vector_store = get_vector_store(text_chunks)
                    st.session_state.conversation = get_conversational_chain(vector_store)
                    st.success("PDFs processed successfully!")
            else:
                st.warning("Please upload PDF files before processing.")

if __name__ == "__main__":
    main()
