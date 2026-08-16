# 🔍 AI Research Agent

An Agentic AI-powered research assistant built using **Agno**, **Groq LLMs**, **DuckDuckGo Search**, and **FastAPI**.

The agent performs web research, retrieves relevant information from the internet, and generates concise summaries with source references.

---

## 🚀 Features

- AI-powered research assistant
- Real-time web search using DuckDuckGo
- Groq LLM integration for fast inference
- Tool-calling Agent architecture
- FastAPI REST API endpoint
- Modular and extensible design
- Suitable for Agentic AI learning and experimentation

---

## 🏗️ Project Structure

```text
AI-Research-Agent/
│
├── research_agent/
│   ├── chat_agent.py
│   ├── server.py
│   └── __init__.py
│
├── study-Planner/
│   ├── study_goals.py
│   └── __init__.py
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Tech Stack

- Python 3.10+
- Agno Framework
- Groq API
- DuckDuckGo Search (DDGS)
- FastAPI
- Uvicorn
- Pydantic

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/Asif13579/AI-Research-Agent.git
cd AI-Research-Agent
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from:

https://console.groq.com

---

## 🧠 Running Research Agent

```bash
python -m research_agent.chat_agent
```

Example Query:

```python
agent.print_response(
    "Research the latest trends in Agentic AI"
)
```

---

## 🌐 Running FastAPI Server

Start the API:

```bash
uvicorn research_agent.server:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## 📡 API Example

### Request

```http
POST /research
```

```json
{
  "query": "Latest Agentic AI trends"
}
```

### Response

```json
{
  "response": "Agentic AI systems are increasingly being used..."
}
```

---

## 🧪 Example Output

- Searches the web
- Retrieves relevant articles
- Summarizes findings
- Provides source links

Example:

```text
Title: Agentic AI Explained
Source: MIT Sloan

Summary:
- Agentic AI enables autonomous decision making.
- AI agents can perform multi-step tasks.
- Increasing adoption across enterprises.
```

---

## 🎯 Learning Objectives

This project demonstrates:

- Agentic AI concepts
- Tool Calling
- LLM Integration
- Web Search Tools
- FastAPI API Development
- Production-ready AI application patterns

---

## 🔮 Future Enhancements

- Multi-Agent Architecture
- RAG (Retrieval-Augmented Generation)
- Memory Support
- LangGraph Integration
- Streaming Responses
- Vector Database Integration (ChromaDB/FAISS)

---

## 👨‍💻 Author

**Asif Ahmad**

- Data Engineer | GenAI Engineer
- Python | FastAPI | LangChain | LangGraph | Agentic AI

GitHub:
https://github.com/Asif13579

---

## 📄 License

MIT License