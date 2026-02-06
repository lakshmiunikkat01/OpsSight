# OpsSight – AI-Powered Operational Intelligence Dashboard

OpsSight is an AI-powered operational intelligence system that ingests heterogeneous Excel files, performs schema-adaptive preprocessing, detects operational anomalies using machine learning, and presents insights through an interactive dashboard.

The project is designed to handle **real-world operational data**, where Excel schemas may vary across teams, and ensures graceful degradation instead of system failures.

---

##  Key Features

-  **Excel Ingestion**
  - Supports multiple Excel templates
  - Automatic column normalization

-  **Schema-Adaptive Preprocessing**
  - Handles missing or inconsistent columns
  - Numeric coercion and safe filtering
  - No crashes on unexpected input

-  **Anomaly Detection**
  - Uses Isolation Forest for anomaly detection
  - Automatically skips ML when insufficient signals exist

-  **Insight Generation**
  - Converts anomalies into human-readable business insights
  - Explains results clearly for non-technical stakeholders

-  **Interactive Dashboard**
  - Built with Streamlit
  - Displays processed data, anomalies, and insights
  - Graceful messaging when no anomalies are found

---

##  Tech Stack

- **Language:** Python  
- **Libraries:** Pandas, Scikit-learn  
- **ML Model:** Isolation Forest  
- **Dashboard:** Streamlit  
- **Data Source:** Excel (.xlsx)

---

##  Project Structure
OpsSight/
├── anomaly_detection/
│ └── detect.py
├── preprocessing/
│ └── clean.py
├── ingestion/
│ └── ingest.py
├── insights/
│ └── narrator.py
├── dashboard/
│ └── app.py
├── main.py
└── .gitignore

---

##  How to Run Locally

 1. Install dependencies
pip install -r requirements.txt
2. Run the Streamlit dashboard
streamlit run dashboard/app.py
3. Upload an Excel file
Files with operational metrics → anomaly detection + insights
Files without metrics → safe processing with clear messaging


