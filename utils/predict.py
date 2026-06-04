"""
MediSense AI — Prediction Engine
Handles top-3 predictions, severity scoring, symptom contributions
"""

import sys, pickle, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.constants import SYMPTOMS, DISEASE_SYMPTOMS, DISEASE_INFO, RISK_LEVELS, SYMPTOM_WEIGHTS

BASE   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MDIR   = os.path.join(BASE, 'models')

def _load(name):
    with open(os.path.join(MDIR, name), 'rb') as f:
        return pickle.load(f)

model      = _load('best_model.pkl')
le         = _load('label_encoder.pkl')
symptoms   = _load('symptom_list.pkl')
all_models = _load('all_models.pkl')
cv_results = _load('cv_results.pkl')
meta       = _load('model_meta.pkl')


def predict_top3(selected_symptoms, duration_days=1, frequency='Daily'):
    """Return top-3 disease predictions with probabilities."""
    vec = [0] * len(symptoms)
    for s in selected_symptoms:
        if s in symptoms:
            vec[symptoms.index(s)] = 1

    proba   = model.predict_proba([vec])[0]
    top3idx = proba.argsort()[::-1][:3]

    results = []
    for idx in top3idx:
        disease = le.inverse_transform([idx])[0]
        results.append({
            'disease':     disease,
            'probability': round(float(proba[idx]) * 100, 1),
            'risk':        RISK_LEVELS.get(disease, 'Medium'),
            'info':        DISEASE_INFO.get(disease, {}),
        })
    return results


def compute_severity(selected_symptoms, duration_days=1, frequency='Daily'):
    """Severity = sum(weights) × duration_factor × frequency_factor  → 0-10 scale."""
    freq_map = {'Once': 0.5, 'Occasionally': 0.75, 'Daily': 1.0, 'Multiple times/day': 1.5}
    freq_factor     = freq_map.get(frequency, 1.0)
    duration_factor = min(1 + (duration_days - 1) * 0.15, 3.0)

    raw         = sum(SYMPTOM_WEIGHTS.get(s, 0.5) for s in selected_symptoms)
    max_possible = max(len(selected_symptoms) * 1.0 * 3.0, 1)
    score       = min((raw * duration_factor * freq_factor / max_possible) * 10, 10)
    return round(score, 2)


def get_symptom_contributions(selected_symptoms, disease_name):
    """Which selected symptoms match the predicted disease's known symptom list."""
    known = set(DISEASE_SYMPTOMS.get(disease_name, []))
    contributions = []
    for s in selected_symptoms:
        contributions.append({
            'symptom': s.replace('_', ' ').title(),
            'weight':  SYMPTOM_WEIGHTS.get(s, 0.5),
            'match':   s in known,
        })
    contributions.sort(key=lambda x: (-x['match'], -x['weight']))
    return contributions
