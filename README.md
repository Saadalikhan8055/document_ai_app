
---

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
- 🌐 **User-Friendly Web App**  

---

## 🛠️ Tech Stack
- **Backend:** Python (Flask / FastAPI)  
- **LLM Framework:** LangChain  
- **Vector DB:** FAISS  
- **LLM API:** Google Gemini API  
- **Frontend:** Streamlit / Flask templates  

---

## 📂 Project Structure

document_ai_app/ │── app/                # Flask/FastAPI application │   ├── static/         # CSS, JS │   ├── templates/      # HTML templates │   ├── routes.py       # App routes │   └── ... │── modules/            # LangChain, FAISS, PDF loader │── uploads/            # Uploaded PDFs │── requirements.txt    # Dependencies │── run.py              # Main entry point │── README.md           # Documentation

---

## ⚙️ Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/Saadalikhan8055/document_ai_app.git
   cd document_ai_app

2. Create a virtual environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


3. Install dependencies

pip install -r requirements.txt


4. Set environment variables (create a .env file)

GEMINI_API_KEY=your_google_gemini_api_key


5. Run the application

python run.py

Then open your browser at:
👉 http://127.0.0.1:5000/




---

📊 Future Enhancements

📱 Mobile app integration

🔐 Authentication & user accounts

📂 Multi-PDF support

🎙️ Voice-based Q&A

☁️ Cloud deployment (Heroku/Render/AWS)



---

🤝 Contributing

Contributions are welcome! Fork this repo, make improvements, and submit a PR.


---

📜 License

This project is licensed under the MIT License.


---

👨‍💻 Author

Saad Ali Khan
AI & ML Engineer | Passionate about building LLM-powered apps 🚀