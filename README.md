# Financial-data-extraction-app-using-ai
Strealmlit application that could do Financial Data Extraction

**Financial Data Extraction App (Streamlit + Ollama + Groq)**

<img width="1203" height="668" alt="image" src="https://github.com/user-attachments/assets/97fa8a77-197c-4265-8864-a740c32d735e" />

**Overview**

This app extracts structured financial information from arbitrary text (e.g., earnings reports, annual reports, investor presentations, bank statements).
Built with Streamlit for the user interface, and uses local and cloud LLM inference via Ollama and Groq to parse and extract financial fields quickly and accurately.
Users paste or upload text, click Extract, and receive structured outputs (JSON / CSV-ready) containing the requested financial fields (revenue, net income, EPS, assets, liabilities, dates, currencies, notes, etc.).
Key points

**Low friction:**
users only provide the text to analyze — no manual tagging or complex setup required.
Hybrid inference: run LLMs locally with Ollama and/or use Groq’s cloud inference for fast responses.
Designed to be usable with free/open-source tooling; verify licensing/pricing and API limits for your deployment.
Features

Extract common financial items: revenue, gross profit, net income, operating income, EPS, assets, liabilities, equity, cash flow line items, fiscal period, currency, and footnotes.
Output as structured JSON and downloadable CSV.
Confidence scoring and provenance pointers (where the extracted value came from in the source text).
Simple Streamlit UI: paste text, choose extraction profile (e.g., Income Statement, Balance Sheet, Cash Flow, Custom), get results.
Supports both local (Ollama) and cloud (Groq) LLM backends; can switch modes from the UI or config.
How it works (high level)



**Streamlit UI** -> Controller -> Backend Adapter (OllamaAdapter or GroqAdapter) -> LLM -> Normalizer/Validator -> Results UI / Export
                Environment & setup (example)

**Prerequisites**


  Python 3.9+
  pip
  For Ollama: install Ollama and pull a model (follow Ollama docs for installation and model setup).
  For Groq: obtain API credentials if using cloud inference (check Groq docs and your account details).
  Example environment variables (stored in .env)
  MODE=ollama # or groq
  OLLAMA_HOST=""
  GROQ_API_KEY=your_groq_api_key_here
  OUTPUT_FORMAT=json
  Install Python deps
  pip install -r requirements.txt
  (requirements.txt might include: streamlit, requests, python-dotenv, pandas, jsonschema)
  
  **Running the app**
  
  Start Ollama locally if using local mode (follow Ollama instructions).
  streamlit run app.py
  Open the displayed Streamlit URL, paste text, choose profile, and click Extract.


