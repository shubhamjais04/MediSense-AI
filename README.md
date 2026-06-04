# 🩺 MediSense AI v2.0

> **AI-powered medical diagnosis and health intelligence platform**  
> Built with Python · Streamlit · Scikit-learn · Plotly · SQLite · FPDF2  

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.4+-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

🌐 Live Demo: https://medisense-app.streamlit.app

---

## 🌟 Features (11 Upgrades)

| # | Feature | Description |
|---|---------|-------------|
| 1 | **Cross-Validation Accuracy** | 5-fold stratified CV — no fake 100% accuracy |
| 2 | **Explainable AI** | Symptom contribution chart — *why* a disease was predicted |
| 3 | **Top-3 Disease Predictions** | Probability distribution across top 3 candidates |
| 4 | **Risk Level Classification** | Low / Medium / High urgency per disease |
| 5 | **Advanced Severity Score** | `weight × duration × frequency` formula |
| 6 | **Visual Analytics Dashboard** | Interactive Plotly charts for all predictions |
| 7 | **Safe Medicine Recommendations** | Informational only — always with doctor disclaimer |
| 8 | **PDF Medical Report** | Downloadable report: symptoms, predictions, diet, workout |
| 9 | **SQLite Prediction History** | Full-stack persistence + CSV export |
| 10 | **Disease Information Library** | Description, causes, prevention, recovery for all 41 diseases |
| 11 | **Model Monitoring Panel** | Version, training date, CV accuracy, fold scores |

---

## 🗂️ Project Structure

```
MediSense/
├── app.py                        # Main Streamlit app (5 pages)
├── train_model.py                # Model training with CV
├── requirements.txt
├── README.md
├── .gitignore
│
├── utils/
│   ├── __init__.py               # Clean unified imports
│   ├── constants.py              # Symptoms, diseases, info, risk levels
│   ├── predict.py                # Prediction engine (top-3, severity, SHAP)
│   ├── database.py               # SQLite history (save, load, analytics)
│   ├── pdf_report.py             # PDF report generator
│   └── generate_data.py          # Dataset generation script
│
├── data/
│   ├── symptoms_dataset.csv      # Main symptom dataset (4,920 rows)
│   ├── symptoms_binary.csv       # Binary encoded dataset (4,920 × 133)
│   ├── disease_description.csv   # Disease info (41 rows)
│   ├── symptom_severity.csv      # Symptom weight mapping (132 rows)
│   ├── precautions.csv           # Precautions per disease
│   ├── diets.csv                 # Diet recommendations
│   └── medications.csv           # Medication info (informational)
│
├── models/
│   ├── best_model.pkl            # Best trained classifier
│   ├── label_encoder.pkl         # Disease label encoder
│   ├── symptom_list.pkl          # 132 tracked symptoms
│   ├── all_models.pkl            # All trained models
│   ├── cv_results.pkl            # Cross-validation scores
│   └── model_meta.pkl            # Training metadata
│
├── notebooks/
│   └── medisense_analysis.ipynb  # Complete EDA + ML notebook (executed)
│
└── images/                       # Auto-generated EDA plots
    ├── disease_distribution.png
    ├── disease_symptom_heatmap.png
    ├── symptom_frequency.png
    ├── symptom_severity.png
    ├── model_comparison.png
    ├── feature_importance.png
    ├── severity_scoring.png
    └── per_class_accuracy.png
```

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/shubhamjais04/MediSense.git
cd MediSense

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) Retrain models
python train_model.py

# 5. Launch the app
streamlit run app.py
```

---

## 📊 Dataset Overview

| File | Rows | Columns | Description |
|------|------|---------|-------------|
| symptoms_dataset.csv | 4,920 | 18 | Raw symptom data (Symptom_1 … Symptom_17) |
| symptoms_binary.csv | 4,920 | 133 | Binary encoded (0/1 per symptom) |
| disease_description.csv | 41 | 7 | Disease info + risk levels |
| symptom_severity.csv | 132 | 2 | Symptom weight mappings |
| precautions.csv | 41 | 5 | 4 precautions per disease |
| diets.csv | 41 | 5 | 4 diet tips per disease |
| medications.csv | 41 | 4 | Informational medication info |

---

## 🤖 Model Performance

| Model | CV Accuracy | Std Dev |
|-------|------------|---------|
| SVC (RBF) | ~99.7% | ±0.2% |
| RandomForest | ~98.6% | ±0.3% |

> ⚠️ High accuracy is on a synthetic dataset.  
> Real-world performance will vary — transparently disclosed in the app.

---

## 🏥 Disease Coverage

**41 diseases** across 8 categories:
- **Infectious:** Dengue, Malaria, Typhoid, Tuberculosis, Chicken pox
- **Metabolic:** Diabetes, Hypothyroidism, Hyperthyroidism, Hypoglycemia
- **Cardiac:** Heart Attack, Hypertension, Varicose Veins
- **Hepatic:** Hepatitis A/B/C/D/E, Alcoholic Hepatitis, Jaundice
- **Respiratory:** Pneumonia, Bronchial Asthma, Common Cold, GERD
- **Neurological:** Migraine, Paralysis, Vertigo, Cervical Spondylosis
- **Dermatological:** Acne, Psoriasis, Impetigo, Fungal Infection
- **Other:** Arthritis, Osteoarthritis, AIDS, UTI, Piles

---

## ⚠️ Medical Disclaimer

This application is for **educational and demonstration purposes only**.  
It does **NOT** constitute medical advice.  
Always consult a licensed healthcare professional for diagnosis and treatment.

---

## 👨‍💻 Author

**Shubham Jaiswal**   
[LinkedIn](https://linkedin.com/in/shubhjais04) · [GitHub](https://github.com/shubhamjais04)
