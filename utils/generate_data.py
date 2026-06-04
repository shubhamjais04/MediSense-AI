"""
MediSense AI — Dataset Generation
Generates 6 CSV files inside the data/ folder:
  1. symptoms_dataset.csv       — main ML training dataset
  2. disease_description.csv    — disease descriptions
  3. symptom_severity.csv       — severity weights per symptom
  4. precautions.csv            — precautions per disease
  5. diets.csv                  — diet recommendations
  6. medications.csv            — medication info (informational)
"""

import pandas as pd
import numpy as np
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.constants import SYMPTOMS, DISEASES, DISEASE_SYMPTOMS, DISEASE_INFO, SYMPTOM_WEIGHTS, RISK_LEVELS

np.random.seed(42)
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
os.makedirs(DATA_DIR, exist_ok=True)

# ── 1. Main Symptoms Dataset ───────────────────────────────────────────────────
def generate_symptoms_dataset(n_per_disease=120):
    rows = []
    for disease in DISEASES:
        core = DISEASE_SYMPTOMS.get(disease, SYMPTOMS[:4])
        for _ in range(n_per_disease):
            row = {'Disease': disease}
            # Pick 4-10 symptoms per sample (core + some noise)
            n_core = max(2, int(len(core) * np.random.uniform(0.6, 1.0)))
            chosen = list(np.random.choice(core, size=min(n_core, len(core)), replace=False))
            # 0-2 noise symptoms
            noise_pool = [s for s in SYMPTOMS if s not in core]
            noise = list(np.random.choice(noise_pool, size=np.random.randint(0, 3), replace=False))
            all_syms = chosen + noise
            # Store as Symptom_1 ... Symptom_17
            for i in range(17):
                row[f'Symptom_{i+1}'] = all_syms[i] if i < len(all_syms) else ''
            rows.append(row)
    df = pd.DataFrame(rows)
    # Also generate binary version
    bin_rows = []
    for _, r in df.iterrows():
        brow = {'Disease': r['Disease']}
        syms_in_row = [r[f'Symptom_{i+1}'] for i in range(17) if r[f'Symptom_{i+1}']]
        for s in SYMPTOMS:
            brow[s] = 1 if s in syms_in_row else 0
        bin_rows.append(brow)
    df_bin = pd.DataFrame(bin_rows)
    df.to_csv(os.path.join(DATA_DIR, 'symptoms_dataset.csv'), index=False)
    df_bin.to_csv(os.path.join(DATA_DIR, 'symptoms_binary.csv'), index=False)
    print(f"  symptoms_dataset.csv      → {len(df):,} rows, {len(df.columns)} columns")
    print(f"  symptoms_binary.csv       → {len(df_bin):,} rows, {len(df_bin.columns)} columns")
    return df, df_bin

# ── 2. Disease Description ─────────────────────────────────────────────────────
def generate_disease_description():
    rows = []
    for disease in DISEASES:
        info = DISEASE_INFO[disease]
        rows.append({
            'Disease': disease,
            'Description': info['description'],
            'Causes': info['causes'],
            'Prevention': info['prevention'],
            'Recovery_Time': info['recovery_time'],
            'When_To_See_Doctor': info['when_to_see_doctor'],
            'Risk_Level': RISK_LEVELS.get(disease, 'Medium'),
        })
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(DATA_DIR, 'disease_description.csv'), index=False)
    print(f"  disease_description.csv   → {len(df)} rows")
    return df

# ── 3. Symptom Severity ────────────────────────────────────────────────────────
def generate_symptom_severity():
    rows = [{'Symptom': s, 'weight': SYMPTOM_WEIGHTS[s]} for s in SYMPTOMS]
    df = pd.DataFrame(rows).sort_values('weight', ascending=False).reset_index(drop=True)
    df.to_csv(os.path.join(DATA_DIR, 'symptom_severity.csv'), index=False)
    print(f"  symptom_severity.csv      → {len(df)} rows")
    return df

# ── 4. Precautions ────────────────────────────────────────────────────────────
PRECAUTIONS = {
    'Fungal infection':['Keep skin clean and dry','Use antifungal powder','Avoid sharing personal items','Wear breathable clothing'],
    'Allergy':['Avoid allergens','Take antihistamines as prescribed','Use air purifiers at home','Keep windows closed during high pollen days'],
    'GERD':['Avoid spicy and fatty foods','Eat smaller meals','Do not lie down after eating','Elevate head while sleeping'],
    'Chronic cholestasis':['Avoid alcohol','Follow a low-fat diet','Take prescribed medications','Regular liver function tests'],
    'Drug Reaction':['Stop the suspected drug immediately','Consult doctor immediately','Carry medication allergy card','Inform all doctors of allergies'],
    'Peptic ulcer disease':['Avoid NSAIDs','Limit alcohol and caffeine','Eat regularly','Take antacids as prescribed'],
    'AIDS':['Use protection during sexual activity','Do not share needles','Take antiretroviral therapy','Regular CD4 count monitoring'],
    'Diabetes':['Monitor blood sugar daily','Follow diabetic diet','Exercise regularly','Take insulin/medications as prescribed'],
    'Gastroenteritis':['Stay hydrated with ORS','Wash hands frequently','Avoid solid food initially','Rest adequately'],
    'Bronchial Asthma':['Avoid triggers like dust and smoke','Carry inhaler always','Follow action plan','Get flu vaccine annually'],
    'Hypertension':['Monitor BP at home','Reduce salt intake','Exercise regularly','Avoid smoking and alcohol'],
    'Migraine':['Identify and avoid triggers','Maintain sleep schedule','Stay hydrated','Practice stress management'],
    'Cervical spondylosis':['Use ergonomic chair','Take breaks from screen','Do neck exercises','Use supportive pillow'],
    'Paralysis (brain hemorrhage)':['Call emergency services immediately','Do not move the patient','Monitor breathing','Begin rehabilitation early'],
    'Jaundice':['Avoid alcohol completely','Rest adequately','Stay hydrated','Follow doctors dietary advice'],
    'Malaria':['Take antimalarial drugs as prescribed','Use mosquito nets','Apply repellent','Avoid outdoor activity at dusk/dawn'],
    'Chicken pox':['Isolate from others','Avoid scratching','Take antivirals if prescribed','Keep skin clean'],
    'Dengue':['Rest completely','Drink plenty of fluids','Monitor platelet count','Avoid aspirin and NSAIDs'],
    'Typhoid':['Drink boiled water only','Eat freshly cooked food','Complete antibiotic course','Maintain hygiene'],
    'hepatitis A':['Avoid alcohol','Get vaccinated','Wash hands before eating','Rest and stay hydrated'],
    'Hepatitis B':['Get vaccinated','Use protection during sex','Do not share needles','Regular liver monitoring'],
    'Hepatitis C':['Do not share needles','Regular blood tests','Antiviral treatment as prescribed','Avoid alcohol'],
    'Hepatitis D':['Hepatitis B vaccination prevents D','Avoid sharing needles','Use protection','Regular monitoring'],
    'Hepatitis E':['Drink safe water','Avoid raw/undercooked food','Maintain hygiene','Rest and hydration'],
    'Alcoholic hepatitis':['Stop alcohol immediately','Follow prescribed diet','Regular liver function tests','Join support group'],
    'Tuberculosis':['Complete full course of antibiotics','Cover mouth while coughing','Ensure good ventilation','Regular sputum tests'],
    'Common Cold':['Rest adequately','Drink warm fluids','Use steam inhalation','Avoid cold exposure'],
    'Pneumonia':['Complete antibiotic course','Rest completely','Stay hydrated','Breathing exercises'],
    'Dimorphic hemmorhoids(piles)':['Eat high-fiber diet','Stay hydrated','Avoid straining','Sitz baths'],
    'Heart attack':['Call emergency immediately','Chew aspirin if available','Do not drive yourself','Begin CPR if needed'],
    'Varicose veins':['Elevate legs when resting','Wear compression stockings','Exercise regularly','Avoid long periods of standing'],
    'Hypothyroidism':['Take thyroid medication daily','Regular TSH tests','Eat iodine-rich foods','Exercise regularly'],
    'Hyperthyroidism':['Take antithyroid medications','Avoid excess iodine','Regular thyroid function tests','Wear sunglasses outdoors'],
    'Hypoglycemia':['Eat small frequent meals','Carry glucose tablets','Monitor blood sugar','Avoid skipping meals'],
    'Osteoarthritis':['Do low-impact exercise','Maintain healthy weight','Use hot/cold therapy','Physical therapy'],
    'Arthritis':['Physical therapy','Anti-inflammatory diet','Protect joints during activity','Adequate rest'],
    '(vertigo) Paroymsal Positional Vertigo':['Do Epley maneuver','Avoid sudden head movements','Move slowly when rising','Physical therapy'],
    'Acne':['Wash face twice daily','Avoid touching face','Use non-comedogenic products','Consult dermatologist'],
    'Urinary tract infection':['Drink plenty of water','Complete antibiotic course','Urinate after intercourse','Maintain hygiene'],
    'Psoriasis':['Moisturize skin regularly','Avoid triggers','Use prescribed topical treatments','Manage stress'],
    'Impetigo':['Keep affected area clean','Apply prescribed antibiotics','Avoid touching sores','Do not share towels'],
}
def generate_precautions():
    rows = []
    for disease in DISEASES:
        precs = PRECAUTIONS.get(disease, ['Consult a doctor','Follow prescribed treatment','Maintain hygiene','Get adequate rest'])
        rows.append({'Disease': disease, 'Precaution_1': precs[0], 'Precaution_2': precs[1] if len(precs)>1 else '','Precaution_3': precs[2] if len(precs)>2 else '','Precaution_4': precs[3] if len(precs)>3 else ''})
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(DATA_DIR, 'precautions.csv'), index=False)
    print(f"  precautions.csv           → {len(df)} rows")
    return df

# ── 5. Diets ──────────────────────────────────────────────────────────────────
def generate_diets():
    rows = []
    for disease in DISEASES:
        info = DISEASE_INFO[disease]
        diet = info.get('diet', ['Balanced diet','Stay hydrated'])
        rows.append({'Disease': disease, 'Diet_1': diet[0] if len(diet)>0 else '', 'Diet_2': diet[1] if len(diet)>1 else '', 'Diet_3': diet[2] if len(diet)>2 else '', 'Diet_4': diet[3] if len(diet)>3 else ''})
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(DATA_DIR, 'diets.csv'), index=False)
    print(f"  diets.csv                 → {len(df)} rows")
    return df

# ── 6. Medications (informational) ────────────────────────────────────────────
def generate_medications():
    rows = []
    for disease in DISEASES:
        info = DISEASE_INFO[disease]
        meds = info.get('medicines', ['Consult doctor'])
        rows.append({'Disease': disease, 'Medication_1': meds[0] if len(meds)>0 else '', 'Medication_2': meds[1] if len(meds)>1 else '', 'Disclaimer': 'Informational only - consult a licensed doctor before use'})
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(DATA_DIR, 'medications.csv'), index=False)
    print(f"  medications.csv           → {len(df)} rows")
    return df

if __name__ == '__main__':
    print("\nGenerating MediSense datasets...\n")
    df_sym, df_bin = generate_symptoms_dataset(120)
    generate_disease_description()
    generate_symptom_severity()
    generate_precautions()
    generate_diets()
    generate_medications()
    print(f"\nAll 6 datasets saved to: {DATA_DIR}\n")
