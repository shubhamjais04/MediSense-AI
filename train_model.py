"""
MediSense AI — Model Training Script
Trains RandomForest, GradientBoosting, SVC with 5-fold cross-validation
Saves all model artifacts to models/
Run: python train_model.py
"""

import pandas as pd
import numpy as np
import pickle, os, datetime, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score, StratifiedKFold, train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
from utils.constants import SYMPTOMS, DISEASES, DISEASE_SYMPTOMS, SYMPTOM_WEIGHTS

MODELS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
DATA_DIR   = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
os.makedirs(MODELS_DIR, exist_ok=True)

def generate_training_data(n_per_disease=120):
    """Generate synthetic training data from disease-symptom mappings."""
    np.random.seed(42)
    X_rows, y = [], []
    for disease in DISEASES:
        core = DISEASE_SYMPTOMS.get(disease, SYMPTOMS[:4])
        for _ in range(n_per_disease):
            vec = [0] * len(SYMPTOMS)
            n_core = max(2, int(len(core) * np.random.uniform(0.6, 1.0)))
            chosen = np.random.choice(core, size=min(n_core, len(core)), replace=False)
            for s in chosen:
                if s in SYMPTOMS:
                    vec[SYMPTOMS.index(s)] = 1
            noise_count = np.random.randint(0, 3)
            noise_pool = [s for s in SYMPTOMS if s not in core]
            for s in np.random.choice(noise_pool, size=min(noise_count, len(noise_pool)), replace=False):
                vec[SYMPTOMS.index(s)] = 1
            X_rows.append(vec)
            y.append(disease)
    X = pd.DataFrame(X_rows, columns=SYMPTOMS)
    return X, pd.Series(y)

def train():
    print("=" * 60)
    print("  MediSense AI — Model Training")
    print("=" * 60)

    # ── Load / Generate Data ───────────────────────────────────────
    bin_csv = os.path.join(DATA_DIR, 'symptoms_binary.csv')
    if os.path.exists(bin_csv):
        print("\n[1/5] Loading binary dataset from data/...")
        df = pd.read_csv(bin_csv)
        X = df[SYMPTOMS]
        y = df['Disease']
    else:
        print("\n[1/5] Generating training data...")
        X, y = generate_training_data(120)

    print(f"      Dataset: {X.shape[0]:,} samples × {X.shape[1]} features")
    print(f"      Diseases: {y.nunique()} classes")

    # ── Label Encode ───────────────────────────────────────────────
    print("\n[2/5] Encoding labels...")
    le = LabelEncoder()
    y_enc = le.fit_transform(y)

    # ── Train/Test Split ───────────────────────────────────────────
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_enc, test_size=0.2, random_state=42, stratify=y_enc
    )
    print(f"      Train: {len(X_train):,}  |  Test: {len(X_test):,}")

    # ── Define Models ──────────────────────────────────────────────
    print("\n[3/5] Training models with 5-Fold Cross-Validation...\n")
    models = {
        'RandomForest':     RandomForestClassifier(n_estimators=200, max_depth=15, random_state=42, n_jobs=-1),
        'GradientBoosting': GradientBoostingClassifier(n_estimators=100, max_depth=6, random_state=42),
        'SVC':              SVC(probability=True, kernel='rbf', C=1.0, random_state=42),
    }

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_results = {}

    for name, model in models.items():
        scores = cross_val_score(model, X, y_enc, cv=cv, scoring='accuracy', n_jobs=-1)
        cv_results[name] = {
            'cv_mean': float(scores.mean()),
            'cv_std':  float(scores.std()),
            'scores':  scores.tolist()
        }
        model.fit(X_train, y_train)
        test_acc = model.score(X_test, y_test)
        print(f"  {name:20s}  CV={scores.mean()*100:.2f}% ±{scores.std()*100:.2f}%   Test={test_acc*100:.2f}%")

    # ── Best Model ─────────────────────────────────────────────────
    best_name  = max(cv_results, key=lambda k: cv_results[k]['cv_mean'])
    best_model = models[best_name]
    print(f"\n  Best Model: {best_name}  (CV={cv_results[best_name]['cv_mean']*100:.2f}%)")

    # ── Classification Report ──────────────────────────────────────
    print("\n[4/5] Classification Report (test set):")
    y_pred = best_model.predict(X_test)
    report = classification_report(y_test, y_pred, target_names=le.classes_, output_dict=True)
    report_df = pd.DataFrame(report).transpose()
    print(report_df[['precision','recall','f1-score','support']].round(3).to_string())

    # ── Save Artifacts ─────────────────────────────────────────────
    print("\n[5/5] Saving model artifacts to models/...")
    meta = {
        'best_model_name':    best_name,
        'training_date':      datetime.datetime.now().strftime('%Y-%m-%d'),
        'model_version':      'v2.0',
        'cv_accuracy':        cv_results[best_name]['cv_mean'],
        'cv_std':             cv_results[best_name]['cv_std'],
        'n_diseases':         len(DISEASES),
        'n_symptoms':         len(SYMPTOMS),
        'n_training_samples': len(X),
        'prediction_count':   0,
    }

    artifacts = {
        'best_model.pkl':    best_model,
        'label_encoder.pkl': le,
        'symptom_list.pkl':  SYMPTOMS,
        'all_models.pkl':    models,
        'cv_results.pkl':    cv_results,
        'model_meta.pkl':    meta,
    }
    for fname, obj in artifacts.items():
        with open(os.path.join(MODELS_DIR, fname), 'wb') as f:
            pickle.dump(obj, f)
        print(f"      Saved: models/{fname}")

    print("\n" + "=" * 60)
    print("  Training Complete!")
    print(f"  Best Model : {best_name}")
    print(f"  CV Accuracy: {cv_results[best_name]['cv_mean']*100:.2f}% ± {cv_results[best_name]['cv_std']*100:.2f}%")
    print("=" * 60 + "\n")
    return best_model, le, SYMPTOMS, cv_results

if __name__ == '__main__':
    train()
