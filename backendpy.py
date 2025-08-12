import os
import asyncio
import nest_asyncio

nest_asyncio.apply()

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

# Set API key for Gemini. This should be a valid key.
os.environ["GOOGLE_API_KEY"] = "AIzaSyCtswwkSsnxrJIM3Eo9JhOeFB9Y4_-wTHE"

# Global variable to store the conversational chain and memory
# This prevents the chain from being re-created on every interaction
qa_chain = None
memory = None

def process_document(file_path):
    """
    Loads a PDF, splits it, creates a vector store, and initializes the conversational chain.
    """
    global qa_chain, memory
    
    # Check if a file was actually loaded
    if not os.path.exists(file_path):
        return None

    # Load PDF
    try:
        loader = PyPDFLoader(file_path)
        documents = loader.load()
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return None

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)

    # Create embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # Create a vector store
    vectorstore = FAISS.from_documents(docs, embeddings)

    # Initialize memory and the conversational chain
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
        return_source_documents=True
    )
    return qa_chain

def ask_question(query):
    """
    Uses the existing conversational chain to answer a question.
    """
    global qa_chain
    if qa_chain is None:
        return "Please upload a document first."
    
    # Run the query against the chain
    result = qa_chain({"question": query})
    return result["answer"]

def process_document(file_path):
    """
    Loads a PDF, splits it, creates a vector store, and initializes the conversational chain.
    """
    global qa_chain, memory
    
    if not os.path.exists(file_path):
        return None

    # Load PDF
    try:
        loader = PyPDFLoader(file_path)
        documents = loader.load()
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return None

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)

    # Create embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # Create a vector store
    vectorstore = FAISS.from_documents(docs, embeddings)

    # Memory for conversation
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"  # ✅ explicitly tell it which output to keep
    )

    # Use gemini-1.5-flash to avoid quota exhaustion
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)

    # Create chain with explicit output key
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
        return_source_documents=True,
        output_key="answer"  # ✅ fix ValueError
    )
    return qa_chain

