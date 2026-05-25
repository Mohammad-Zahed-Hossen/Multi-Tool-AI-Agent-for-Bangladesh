# 🇧🇩 Multi-Tool AI Agent for Bangladesh

An AI-powered multi-tool agent built using LangChain, Gemini, SQLite, and Tavily Search.

This project can:

- Answer Bangladesh institutional data queries
- Answer hospital-related queries
- Answer restaurant-related queries
- Perform general web search for Bangladesh-related knowledge
- Automatically select the correct tool using an AI agent

---

# 🚀 Features

## 📚 Institutional Information Tool
Handles queries about:
- Schools
- Colleges
- Universities
- Madrasas
- EIIN
- MPO status
- Educational statistics

Example:
```text
How many colleges are in Dhaka?
```

---

## 🏥 Hospital Information Tool
Handles queries about:
- Hospitals
- Clinics
- Private hospitals
- Government hospitals
- Healthcare facilities

Example:
```text
How many private hospitals are in Chattogram?
```

---

## 🍽️ Restaurant Information Tool
Handles queries about:
- Restaurant ratings
- Restaurant locations
- Reviews
- Top-rated restaurants

Example:
```text
Show top rated restaurants.
```

---

## 🌐 Web Search Tool
Handles:
- General knowledge
- Bangladesh healthcare policy
- DGHS
- Cultural or government-related information

Example:
```text
What is DGHS in Bangladesh?
```

---

# 🧠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | AI agent framework |
| Gemini API | Large Language Model |
| SQLite | Database |
| Pandas | CSV processing |
| Tavily Search API | Web search |
| HuggingFace Datasets | Dataset source |

---

# 📁 Project Structure

```text
multi_tool_ai_agent/
│
├── data/
│   ├── institutions.csv
│   ├── hospitals.csv
│   └── restaurants.csv
│
├── databases/
│   ├── institutions.db
│   ├── hospitals.db
│   └── restaurants.db
│
├── tools/
│   ├── institutions_tool.py
│   ├── hospitals_tool.py
│   ├── restaurants_tool.py
│   └── web_search_tool.py
│
├── agent/
│   └── main_agent.py
│
├── setup_db.py
├── check_db.py
├── test_tools.py
├── test_web_search.py
├── requirements.txt
├── .env
└── README.md
```

---

# 📦 Dataset Sources

## Institutional Information of Bangladesh
- https://huggingface.co/datasets/Mahadih534/Institutional-Information-of-Bangladesh

## All Bangladeshi Hospitals
- https://huggingface.co/datasets/Mahadih534/all-bangladeshi-hospitals

## Bangladeshi Restaurant Data
- https://huggingface.co/datasets/Mahadih534/Bangladeshi-Restaurant-Data

---

# ⚙️ Installation Guide

## 1. Clone Repository

```bash
git clone https://github.com/Mohammad-Zahed-Hossen/Multi-Tool-AI-Agent-for-Bangladesh.git
```

```bash
cd Multi-Tool-AI-Agent-for-Bangladesh
```

---

# 🐍 Create Virtual Environment

## Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

---

## Mac/Linux

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

# 📥 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Setup Environment Variables

Create a `.env` file in the root directory.

Example:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

# 🔐 Get API Keys

## Gemini API Key
https://aistudio.google.com/app/apikey

## Tavily API Key
https://app.tavily.com/home

---

# 📂 Add Dataset CSV Files

Download datasets and place them inside:

```text
data/
```

Rename them as:

```text
institutions.csv
hospitals.csv
restaurants.csv
```

---

# 🗄️ Create SQLite Databases

Run:

```bash
python setup_db.py
```

This will create:

```text
databases/
├── institutions.db
├── hospitals.db
└── restaurants.db
```

---

# ✅ Verify Databases

Run:

```bash
python check_db.py
```

---

# 🧪 Test Database Tools

Run:

```bash
python test_tools.py
```

---

# 🌐 Test Web Search Tool

Run:

```bash
python test_web_search.py
```

---

# 🤖 Run Main AI Agent

Run:

```bash
python agent/main_agent.py
```

---

# 💬 Example Queries

## Educational Queries

```text
How many colleges are in Dhaka?
```

```text
Show institutions in Chattogram.
```

```text
How many MPO approved institutions exist?
```

---

## Hospital Queries

```text
How many private hospitals are in Chattogram?
```

```text
Show hospitals in Dhaka.
```

---

## Restaurant Queries

```text
Show top rated restaurants.
```

```text
Restaurants in Cox's Bazar.
```

---

## Web Search Queries

```text
What is DGHS in Bangladesh?
```

```text
What is the healthcare policy of Bangladesh?
```

---

# 🏗️ System Architecture

```text
                ┌────────────────┐
                │     USER       │
                └──────┬─────────┘
                       │
                       ▼
             ┌──────────────────┐
             │   MAIN AGENT     │
             └──────┬───────────┘
                    │
     ┌──────────────┼──────────────┐
     ▼              ▼              ▼
┌──────────┐  ┌──────────┐  ┌────────────┐
│HospitalDB│  │Institution│  │RestaurantDB│
└──────────┘  └──────────┘  └────────────┘
                    │
                    ▼
             ┌────────────┐
             │ Web Search │
             └────────────┘
```

---

# 🧠 AI Workflow

```text
User Query
    ↓
Main AI Agent
    ↓
Tool Selection
    ↓
Database/Web Search Tool
    ↓
SQL Query or Web Search
    ↓
Response Generation
    ↓
Final Answer
```

---

# 📌 Important Notes

- Gemini is used as the main LLM.
- SQLite stores structured Bangladesh datasets.
- Tavily is used for web search.
- LangChain ReAct Agent handles tool routing.
- Tool descriptions are optimized to improve routing accuracy.

---

# 🚧 Future Improvements

Possible future upgrades:

- Streamlit chatbot UI
- Memory support
- FastAPI deployment
- LangGraph integration
- RAG pipeline
- Better SQL safety
- Vector database support

---

# 👨‍💻 Author

Mohammad Zahed Hossen

CSE Final Year Student

---

# 📜 License

This project is developed for educational and academic purposes.
