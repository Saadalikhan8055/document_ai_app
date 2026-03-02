# Document AI App

Document AI App is an **interactive PDF Q&A system** powered by **Python, LangChain, FAISS, and Google Gemini API**.  
You can upload PDFs, ask questions in **natural language**, and get **accurate answers with source references**.  
The app also supports **conversational memory**, so you can continue asking follow-up questions without losing context.

---

## 🚀 Features
- 📄 Upload **PDFs** and instantly query their content  
- 🤖 **Natural Language Q&A** powered by Gemini API + LangChain  
- 🔍 **Fast Search** using FAISS vector embeddings  
- 💬 **Conversational Memory** – keeps context across multiple queries  
- 📑 **Answers with Sources** – ensures reliability  
- 🌐 **User-Friendly Web App** built with Streamlit  

---

## 🛠️ Tech Stack
- **Frontend:** Streamlit  
- **Backend:** Python with LangChain  
- **LLM Framework:** LangChain  
- **Vector Database:** FAISS  
- **LLM API:** Google Gemini API (1.5-Flash)  
- **PDF Processing:** PyPDFLoader  
- **Text Processing:** RecursiveCharacterTextSplitter  

---

## 📂 Project Structure

```
document_ai_app/
├── app.py                    # Streamlit frontend application
├── backendpy.py              # Backend logic & LangChain integration
├── requirements.txt          # Python dependencies (to be filled)
├── README.md                 # Documentation
├── data/                     # Stored PDF files
├── uploads/                  # Uploaded PDF files (temporary)
└── utils/                    # Utility modules
    ├── __init__.py
    ├── pdf_loader.py         # PDF loading utility (PyPDF2)
    ├── text_splitter.py      # Text chunking utility (LangChain)
    └── vector_store.py       # FAISS vector store utility
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Saadalikhan8055/document_ai_app.git
cd document_ai_app
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up Google Gemini API Key
- Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- Update the API key in `backendpy.py`:
  ```python
  os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY_HERE"
  ```

### 5. Run the application
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 📋 Dependencies

Key packages used in this project:
- **streamlit** – Web UI framework
- **langchain** – LLM orchestration framework
- **langchain-google-genai** – Google Gemini API integration
- **langchain-community** – Community integrations
- **faiss-cpu** – Vector similarity search
- **pypdf** – PDF document loading
- **PyPDF2** – PDF reading utility
- **nest-asyncio** – Async event loop support

---

## 🎯 How It Works

1. **Upload PDF:** User uploads a PDF file through the Streamlit interface
2. **Process Document:** The PDF is loaded using PyPDFLoader and split into chunks
3. **Create Embeddings:** Text chunks are converted to embeddings using Google's embedding model
4. **Vector Store:** Embeddings are stored in FAISS for fast similarity search
5. **Conversational Chain:** ConversationalRetrievalChain is initialized with LLM, retriever, and memory
6. **Chat Interface:** User can ask questions about the document
7. **Retrieve Context:** Semantic search retrieves relevant document chunks
8. **Generate Answer:** Google Gemini generates contextual answers using conversation history
9. **Memory Management:** ConversationBufferMemory maintains chat history

---

## 🔧 Configuration

### Text Chunking Parameters (in `backendpy.py`)
```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,        # Size of each text chunk
    chunk_overlap=200       # Overlap between chunks
)
```

### LLM Settings (in `backendpy.py`)
```python
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2         # Controls randomness of responses
)
```

---

## 📝 Usage Example

1. Start the application:
   ```bash
   streamlit run app.py
   ```

2. Open your browser to `http://localhost:8501`

3. Upload a PDF file

4. Wait for the PDF to be processed (see "PDF processed. Start chatting!" message)

5. Type your question in the chat input field

6. Get answers with conversational memory support for follow-ups

---

## ⚠️ Important Notes

- **API Key Security:** Never commit your actual API key to version control. Use environment variables
- **File Storage:** Uploaded PDFs are temporarily stored in the `data/` directory
- **Session State:** Chat history and retriever are maintained in Streamlit session state
- **Vector Store:** FAISS vector stores are created in memory during each session

---

## 🚀 Future Enhancements

- 📱 Multiple document support
- 🔐 Authentication & user accounts  
- 📂 Persistent vector store storage
- 📄 Support for multiple file formats (DOCX, TXT, etc.)
- 🎙️ Voice-based Q&A
- ☁️ Cloud deployment (Heroku/Render/AWS)
- 📊 Export conversation history

---

## 🤝 Contributing

Contributions are welcome! Fork this repo, make improvements, and submit a PR.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Saad Ali Khan  
AI & ML Engineer | Passionate about building LLM-powered apps 🚀
