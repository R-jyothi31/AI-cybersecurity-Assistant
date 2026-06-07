
# 🚀 AI Cybersecurity Assistant

An Agentic AI-powered cybersecurity platform that helps security analysts identify threats, enrich indicators, map MITRE ATT&CK techniques, retrieve CISA advisories, and generate mitigation recommendations automatically.

---

## 📦 Step 1 — Install Required Packages

Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install flask flask-cors sentence-transformers faiss-cpu requests reportlab transformers
```

---

## 🔑 Step 2 — Configure API Keys

Open:

```text
backend/config.py
```

Add your API keys:

```python
VIRUSTOTAL_API_KEY = "your_virustotal_api_key"
ABUSEIPDB_API_KEY = "your_abuseipdb_api_key"
```

---

## ▶️ Step 3 — Start the Backend

Run:

```bash
python app.py
```

You should see:

```text
AI Cybersecurity Assistant running at http://localhost:5000
```

---

## 🌐 Step 4 — Open the Frontend

Open:

```text
frontend/index.html
```

in your browser.

Or visit:

```text
http://localhost:5000
```

if Flask serves the frontend.

---

## 🔍 Step 5 — Analyze Threats

Examples:

```text
Analyze IP: 8.8.8.8
```

```text
Analyze Hash: e99a18c428cb38d5f260853678922e03
```

```text
Recent ransomware techniques
```

```text
Latest CISA vulnerabilities
```

The assistant will:

✅ Search threat intelligence sources
✅ Query VirusTotal
✅ Query AbuseIPDB
✅ Map MITRE ATT&CK techniques
✅ Retrieve CISA advisories
✅ Generate mitigation recommendations
✅ Create downloadable security reports

---

# ⚙️ How It Works

### 1️⃣ User submits a security query

Examples:

```text
IP Address
File Hash
Domain
Threat Description
```

↓

### 2️⃣ Flask Backend Receives Request

```text
Frontend → Flask API
```

↓

### 3️⃣ Agentic AI Workflow Starts

Multiple AI agents work together:

```text
Threat Detection Agent
MITRE Mapping Agent
Threat Intelligence Agent
Recommendation Agent
Report Generation Agent
```

↓

### 4️⃣ External Intelligence Sources Queried

```text
VirusTotal API
AbuseIPDB API
MITRE ATT&CK Framework
CISA Advisories Feed
```

↓

### 5️⃣ FAISS Vector Search

Relevant cybersecurity knowledge is retrieved from the vector database.

↓

### 6️⃣ AI Generates Recommendations

The system provides:

```text
Threat Classification
Risk Level
MITRE ATT&CK Mapping
Indicators of Compromise (IOCs)
Mitigation Steps
```

↓

### 7️⃣ Results Displayed on Dashboard

Users receive:

```text
Threat Analysis
Security Recommendations
PDF Security Report
```

---

# 🛠️ Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Flask
* REST APIs

### AI & RAG

* FAISS Vector Database
* Sentence Transformers
* Agentic AI Architecture

### Threat Intelligence

* VirusTotal API
* AbuseIPDB API
* MITRE ATT&CK Framework
* CISA Advisories

### Reporting

* PDF Report Generation

