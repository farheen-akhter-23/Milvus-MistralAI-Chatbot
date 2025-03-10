# 🎓 Academic Advisor Chatbot - CSUSB CSE  

🚀 **An AI-powered chatbot designed to assist students with academic advising at CSUSB's Computer Science and Engineering (CSE) department.**  

This chatbot leverages **Milvus (vector database), Large Language Models (LLMs), high-performance computing (HPC), and deep learning** to retrieve the most relevant responses to academic queries based on official university data.

---

## 🌟 Features  

✅ **Retrieves Academic Information**: The chatbot provides guidance on **courses, schedules, faculty, research opportunities, and resources** from official CSUSB CSE sources.  
✅ **Milvus Vector Search**: Uses **Milvus** as a high-speed vector database for storing and retrieving knowledge.  
✅ **Hybrid Search with RAG**: Implements **Retrieval-Augmented Generation (RAG)** to retrieve and summarize relevant information.  
✅ **LLM-Powered Responses**: Utilizes **Mistral-7B** to generate responses based strictly on academic content.  
✅ **Keyword Matching & Relevance Filtering**: Ensures high-quality, context-aware responses.  
✅ **Conversational Handling**: Recognizes basic greetings and common prompts.  
✅ **Interactive UI with Streamlit**: Runs on a **streamlit-based frontend**, making it user-friendly.  
✅ **HPC-Optimized**: Runs on **High-Performance Computing (HPC)** for fast processing and **99%+ accuracy** in bed posture recognition research.  
✅ **Jupyter Notebook (pynb) Representation**: A notebook version is available for better understanding of the chatbot's logic and architecture.  

---

## 📌 Data Sources  

This chatbot is built using **verified academic sources** from CSUSB:  

📖 **CSUSB CSE Department Website**: [https://www.csusb.edu/cse](https://www.csusb.edu/cse)  
📑 **CSUSB Academic Catalog**: [https://catalog.csusb.edu/colleges-schools-departments/natural-sciences/computer-science-engineering/](https://catalog.csusb.edu/colleges-schools-departments/natural-sciences/computer-science-engineering/)  

The system **scrapes** these websites, stores structured content in **Milvus**, and retrieves information when queried.

---

## 🏗️ Architecture  

The chatbot follows a **hybrid search + LLM** architecture:  

1️⃣ **Web Scraping & Data Storage**:  
   - Web pages are scraped and converted into a structured dataset.  
   - Data is **embedded using `SentenceTransformers (MiniLM-L6-v2)`** and stored in **Milvus**.  

2️⃣ **Query Processing & Context Matching**:  
   - User queries are transformed into **vector embeddings**.  
   - The chatbot **searches Milvus** for the most relevant documents.  
   - **TF-IDF keyword matching** helps refine results.  

3️⃣ **LLM Response Generation**:  
   - Uses **Mistral-7B** for generating responses based on retrieved context.  
   - Implements **prompt engineering techniques** to ensure factual correctness.  

4️⃣ **Interactive Streamlit UI**:  
   - Users interact with the chatbot in a web-based interface.  
   - Backend processes requests, generates responses, and returns them in real time.  

---

## 🚀 Installation & Setup  

### 🔹 **Prerequisites**  
Ensure you have the following installed:  
- **Python 3.10+**  
- **Docker** (for Milvus)  
- **Streamlit**  
- **Milvus Standalone**  
- **Hugging Face Transformers**  
- **MistralAI API Key**  

### 🔹 **Clone the Repository**  
```bash
git clone https://github.com/farheen-akhter-23/academic-chatbot
cd academic-chatbot
```

### 🔹 **Install Dependencies**  
```bash
pip install -r requirements.txt
```

### 🔹 **Set Environment Variables**  
```bash
export API_KEY="your_mistralai_api_key"
export MILVUS_URI="your_milvus_db_uri"
```

### 🔹 **Start Milvus**  
Ensure **Milvus** is running:  
```bash
docker-compose up -d
```

### 🔹 **Run the Chatbot**  
```bash
streamlit run app.py
```

---

## 📊 Jupyter Notebook (pynb) Representation  

A **Jupyter Notebook version** of the chatbot's processing pipeline is available for:  
- **Understanding data flow**  
- **Testing retrieval & embeddings**  
- **Evaluating response accuracy**  

📌 **Notebook Location**: `notebooks/chatbot_demo.ipynb`  

To run:  
```bash
jupyter notebook
```
Then, open `chatbot_demo.ipynb`.

---

## 🏆 Recent Research & Development  

### 📢 **IEEE CAI 2025 Paper Acceptance**  
🚀 **Our research paper has been accepted at the prestigious IEEE Conference on Artificial Intelligence (CAI 2025)!** 🎉  
🔗 [CAI 2025 Conference](https://cai.ieee.org/2025/)  

### 🏗️ **High-Performance Computing (HPC) & AI**  
We are currently working on:  
- **Deep Learning for Bed Posture Recognition** (99%+ accuracy)  
- **Optimizing AI Agents on HPC**  
- **Computer Vision for real-world applications**  

### 📝 **ATS Resume Checker**  
I recently tested **Gemini 1.5 Pro** for evaluating ATS-compliant resumes.  
🔗 **Check it out on GitHub:** [ATS Resume Profile Checker](https://github.com/farheen-akhter-23/LLM-RAG)  

---

## 📬 Get in Touch  

Interested in **AI, Machine Learning, LLMs, or Computer Vision**?  
Let's connect! 🔗 **[LinkedIn](https://www.linkedin.com/in/farheen-akhter-153a0b156/)**  

🚀 Looking forward to exciting AI collaborations!  

---

## 🏆 Contributors  
👨‍💻 **Farheen Akhter** - **AI Researcher & ML Engineer**  
💻 **CSUSB CSE Research Team**  

---

## 📜 License  
This project is **open-source** under the **MIT License**.

---

This **README** is designed to be **engaging, professional, and informative** while showcasing your **AI expertise** and making it **visible to recruiters**. Let me know if you'd like any tweaks! 🚀