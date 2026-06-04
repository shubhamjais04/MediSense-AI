"""
MediSense AI — Shared Constants
Symptoms, diseases, disease-symptom mapping, risk levels, disease info
"""

import numpy as np

# ── 132 Symptoms ───────────────────────────────────────────────────────────────
SYMPTOMS = [
    'itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills',
    'joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting',
    'burning_micturition','spotting_urination','fatigue','weight_gain','anxiety',
    'cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy',
    'patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes',
    'breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin',
    'dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain',
    'constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm',
    'throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion',
    'chest_pain','weakness_in_limbs','fast_heart_rate','pain_during_bowel_motions',
    'pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness',
    'cramps','bruising','obesity','swollen_legs','swollen_blood_vessels',
    'puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties',
    'excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck',
    'swelling_joints','movement_stiffness','spinning_movements','loss_of_balance',
    'unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort',
    'foul_smell_of_urine','continuous_feel_of_urine','passage_of_gases','internal_itching',
    'toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium',
    'red_spots_over_body','belly_pain','abnormal_menstruation','dischromic_patches',
    'watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption','fluid_overload.1','blood_in_sputum',
    'prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples',
    'blackheads','scurring','skin_peeling','silver_like_dusting','small_dents_in_nails',
    'inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze'
]

# ── 41 Diseases ────────────────────────────────────────────────────────────────
DISEASES = [
    'Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
    'Peptic ulcer disease','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma',
    'Hypertension','Migraine','Cervical spondylosis','Paralysis (brain hemorrhage)',
    'Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
    'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis',
    'Tuberculosis','Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
    'Heart attack','Varicose veins','Hypothyroidism','Hyperthyroidism',
    'Hypoglycemia','Osteoarthritis','Arthritis','(vertigo) Paroymsal Positional Vertigo',
    'Acne','Urinary tract infection','Psoriasis','Impetigo'
]

# ── Disease → Key Symptoms ─────────────────────────────────────────────────────
DISEASE_SYMPTOMS = {
    'Fungal infection':['itching','skin_rash','nodal_skin_eruptions','dischromic_patches'],
    'Allergy':['continuous_sneezing','shivering','chills','watering_from_eyes'],
    'GERD':['stomach_pain','acidity','ulcers_on_tongue','vomiting','cough','chest_pain'],
    'Chronic cholestasis':['itching','vomiting','yellowish_skin','nausea','loss_of_appetite','abdominal_pain'],
    'Drug Reaction':['itching','skin_rash','stomach_pain','burning_micturition','spotting_urination'],
    'Peptic ulcer disease':['vomiting','loss_of_appetite','abdominal_pain','passage_of_gases','internal_itching'],
    'AIDS':['muscle_wasting','patches_in_throat','high_fever','extra_marital_contacts','fatigue'],
    'Diabetes':['fatigue','weight_loss','restlessness','lethargy','irregular_sugar_level','polyuria','increased_appetite','family_history'],
    'Gastroenteritis':['vomiting','sunken_eyes','dehydration','diarrhoea'],
    'Bronchial Asthma':['fatigue','cough','high_fever','breathlessness','family_history','mucoid_sputum'],
    'Hypertension':['headache','chest_pain','dizziness','loss_of_balance','lack_of_concentration'],
    'Migraine':['acidity','indigestion','headache','blurred_and_distorted_vision','excessive_hunger','stiff_neck','depression','irritability','visual_disturbances'],
    'Cervical spondylosis':['back_pain','weakness_in_limbs','neck_pain','dizziness','loss_of_balance'],
    'Paralysis (brain hemorrhage)':['vomiting','headache','weakness_of_one_body_side','altered_sensorium','slurred_speech'],
    'Jaundice':['itching','vomiting','fatigue','weight_loss','high_fever','yellowish_skin','dark_urine','abdominal_pain'],
    'Malaria':['chills','vomiting','high_fever','sweating','headache','nausea','diarrhoea','muscle_pain'],
    'Chicken pox':['itching','skin_rash','fatigue','lethargy','high_fever','headache','loss_of_appetite','mild_fever','swelled_lymph_nodes','malaise','red_spots_over_body','phlegm'],
    'Dengue':['skin_rash','chills','joint_pain','vomiting','fatigue','high_fever','headache','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','malaise','muscle_pain','red_spots_over_body'],
    'Typhoid':['chills','vomiting','fatigue','high_fever','headache','nausea','constipation','abdominal_pain','diarrhoea','toxic_look_(typhos)','belly_pain'],
    'hepatitis A':['joint_pain','vomiting','yellowish_skin','dark_urine','nausea','loss_of_appetite','abdominal_pain','diarrhoea','mild_fever','yellowing_of_eyes','muscle_pain'],
    'Hepatitis B':['itching','fatigue','lethargy','yellowish_skin','dark_urine','loss_of_appetite','abdominal_pain','yellow_urine','yellowing_of_eyes','malaise','receiving_blood_transfusion','receiving_unsterile_injections'],
    'Hepatitis C':['fatigue','yellowish_skin','nausea','loss_of_appetite','yellowing_of_eyes','family_history'],
    'Hepatitis D':['joint_pain','vomiting','fatigue','yellowish_skin','dark_urine','nausea','loss_of_appetite','yellowing_of_eyes','muscle_pain'],
    'Hepatitis E':['joint_pain','vomiting','fatigue','high_fever','yellowish_skin','dark_urine','nausea','loss_of_appetite','abdominal_pain','yellowing_of_eyes','acute_liver_failure','coma','stomach_bleeding'],
    'Alcoholic hepatitis':['vomiting','yellowish_skin','abdominal_pain','swelling_of_stomach','history_of_alcohol_consumption','fluid_overload'],
    'Tuberculosis':['chills','vomiting','fatigue','weight_loss','cough','high_fever','breathlessness','sweating','loss_of_appetite','mild_fever','yellowing_of_eyes','swelled_lymph_nodes','malaise','phlegm','blood_in_sputum','rusty_sputum'],
    'Common Cold':['continuous_sneezing','chills','fatigue','cough','high_fever','headache','swelled_lymph_nodes','malaise','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','loss_of_smell','muscle_pain'],
    'Pneumonia':['chills','fatigue','cough','high_fever','breathlessness','sweating','malaise','phlegm','blood_in_sputum','rusty_sputum'],
    'Dimorphic hemmorhoids(piles)':['constipation','pain_during_bowel_motions','pain_in_anal_region','bloody_stool','irritation_in_anus'],
    'Heart attack':['vomiting','breathlessness','sweating','chest_pain','weakness_in_limbs','fast_heart_rate'],
    'Varicose veins':['fatigue','cramps','bruising','obesity','swollen_legs','swollen_blood_vessels','prominent_veins_on_calf'],
    'Hypothyroidism':['fatigue','weight_gain','cold_hands_and_feets','mood_swings','lethargy','dizziness','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','depression','irritability','abnormal_menstruation'],
    'Hyperthyroidism':['fatigue','mood_swings','weight_loss','restlessness','sweating','diarrhoea','fast_heart_rate','excessive_hunger','muscle_weakness','irritability','abnormal_menstruation'],
    'Hypoglycemia':['fatigue','vomiting','anxiety','sweating','headache','nausea','blurred_and_distorted_vision','excessive_hunger','slurred_speech','irritability','drying_and_tingling_lips','palpitations'],
    'Osteoarthritis':['joint_pain','neck_pain','knee_pain','hip_joint_pain','swelling_joints','painful_walking'],
    'Arthritis':['muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','loss_of_balance'],
    '(vertigo) Paroymsal Positional Vertigo':['vomiting','headache','nausea','spinning_movements','loss_of_balance','unsteadiness'],
    'Acne':['skin_rash','pus_filled_pimples','blackheads','scurring'],
    'Urinary tract infection':['burning_micturition','bladder_discomfort','foul_smell_of_urine','continuous_feel_of_urine'],
    'Psoriasis':['skin_rash','joint_pain','skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails'],
    'Impetigo':['skin_rash','high_fever','blister','red_sore_around_nose','yellow_crust_ooze'],
}

# ── Risk Levels ────────────────────────────────────────────────────────────────
RISK_LEVELS = {
    'Fungal infection':'Low','Allergy':'Low','GERD':'Low',
    'Chronic cholestasis':'Medium','Drug Reaction':'Medium',
    'Peptic ulcer disease':'Medium','AIDS':'High','Diabetes':'Medium',
    'Gastroenteritis':'Low','Bronchial Asthma':'Medium',
    'Hypertension':'Medium','Migraine':'Low','Cervical spondylosis':'Low',
    'Paralysis (brain hemorrhage)':'High','Jaundice':'Medium',
    'Malaria':'High','Chicken pox':'Low','Dengue':'High',
    'Typhoid':'High','hepatitis A':'Medium','Hepatitis B':'High',
    'Hepatitis C':'High','Hepatitis D':'High','Hepatitis E':'High',
    'Alcoholic hepatitis':'High','Tuberculosis':'High',
    'Common Cold':'Low','Pneumonia':'High',
    'Dimorphic hemmorhoids(piles)':'Low','Heart attack':'High',
    'Varicose veins':'Low','Hypothyroidism':'Medium',
    'Hyperthyroidism':'Medium','Hypoglycemia':'Medium',
    'Osteoarthritis':'Low','Arthritis':'Low',
    '(vertigo) Paroymsal Positional Vertigo':'Low','Acne':'Low',
    'Urinary tract infection':'Low','Psoriasis':'Low','Impetigo':'Low',
}

# ── Symptom Weights ────────────────────────────────────────────────────────────
np.random.seed(42)
SYMPTOM_WEIGHTS = {s: round(np.random.uniform(0.3, 1.0), 3) for s in SYMPTOMS}
for s in ['high_fever','chest_pain','breathlessness','altered_sensorium','coma',
          'stomach_bleeding','blood_in_sputum','weakness_of_one_body_side','fast_heart_rate']:
    if s in SYMPTOM_WEIGHTS:
        SYMPTOM_WEIGHTS[s] = 1.0


# ── Medicines per disease (informational) ─────────────────────────────────────
DISEASE_MEDICINES = {
    'Fungal infection':   ['Clotrimazole cream (topical)','Fluconazole (oral, consult doctor)','Miconazole powder','Terbinafine (consult doctor)'],
    'Allergy':            ['Cetirizine (antihistamine)','Loratadine','Fexofenadine','Montelukast (consult doctor)','Nasal corticosteroid spray'],
    'GERD':               ['Omeprazole (PPI)','Pantoprazole','Ranitidine (consult doctor)','Antacids (Gelusil, Digene)','Domperidone'],
    'Chronic cholestasis':['Ursodeoxycholic acid (UDCA)','Cholestyramine (for itching)','Fat-soluble vitamins (A,D,E,K)','Rifampicin (consult doctor)'],
    'Drug Reaction':      ['Discontinue causative drug immediately','Antihistamines (Cetirizine)','Corticosteroids (consult doctor)','Calamine lotion (for rash)'],
    'Peptic ulcer disease':['Omeprazole or Pantoprazole','Amoxicillin + Clarithromycin (if H.pylori)','Antacids (Gelusil)','Sucralfate (consult doctor)'],
    'AIDS':               ['Antiretroviral Therapy (ART) as prescribed','Tenofovir + Emtricitabine + Efavirenz (first-line)','Cotrimoxazole (prophylaxis)','Regular CD4/viral load monitoring'],
    'Diabetes':           ['Metformin (Type 2, first-line)','Insulin (Type 1 or advanced Type 2)','Glipizide / Glimepiride (consult doctor)','Empagliflozin (consult doctor)'],
    'Gastroenteritis':    ['ORS (Oral Rehydration Solution)','Zinc supplements (children)','Ondansetron (for vomiting)','Loperamide (adults, consult doctor)'],
    'Bronchial Asthma':   ['Salbutamol inhaler (reliever)','Budesonide inhaler (controller)','Montelukast (consult doctor)','Prednisolone (acute attacks, doctor only)'],
    'Hypertension':       ['Amlodipine','Telmisartan / Losartan','Atenolol','Hydrochlorothiazide (consult doctor)'],
    'Migraine':           ['Sumatriptan (acute attack)','Ibuprofen or Naproxen','Paracetamol + Metoclopramide','Propranolol (prophylaxis, consult doctor)'],
    'Cervical spondylosis':['Ibuprofen / Diclofenac (pain relief)','Muscle relaxants (Methocarbamol, consult doctor)','Physiotherapy exercises','Nerve pain: Pregabalin (consult doctor)'],
    'Paralysis (brain hemorrhage)':['Emergency: Mannitol IV (hospital only)','Antiplatelet/anticoagulant as prescribed','Physiotherapy post-stabilization','Aspirin (ischemic stroke, doctor only)'],
    'Jaundice':           ['Treat underlying cause','Ursodeoxycholic acid (liver support)','Avoid alcohol and hepatotoxic drugs','IV fluids if dehydrated (hospital)'],
    'Malaria':            ['Artemether-Lumefantrine (Coartem)','Chloroquine (P.vivax, consult doctor)','Primaquine (radical cure, consult doctor)','Paracetamol (for fever)'],
    'Chicken pox':        ['Acyclovir (antiviral, consult doctor)','Calamine lotion (for itching)','Paracetamol (fever, avoid aspirin)','Antihistamines (Cetirizine for itch)'],
    'Dengue':             ['Paracetamol (fever — avoid Ibuprofen/Aspirin)','ORS for hydration','Platelet transfusion if severe (hospital)','No specific antiviral available'],
    'Typhoid':            ['Azithromycin (first-line)','Ciprofloxacin (consult doctor)','Ceftriaxone IV (severe cases, hospital)','Paracetamol (fever)'],
    'hepatitis A':        ['No specific antiviral — supportive care','Paracetamol for discomfort (low dose)','IV fluids if needed (hospital)','Avoid alcohol completely'],
    'Hepatitis B':        ['Tenofovir (antiviral, consult doctor)','Entecavir (consult doctor)','Pegylated Interferon (specialist only)','Regular liver function monitoring'],
    'Hepatitis C':        ['Sofosbuvir + Velpatasvir (consult doctor)','Ribavirin (combination, specialist)','Regular viral load monitoring','Avoid alcohol'],
    'Hepatitis D':        ['Pegylated Interferon-alpha (only option)','Tenofovir (for co-infection with HBV)','Specialist hepatologist required','Supportive care'],
    'Hepatitis E':        ['Supportive care (rest + hydration)','Ribavirin (severe/chronic cases, consult doctor)','Avoid alcohol and hepatotoxic drugs','IV fluids if dehydrated'],
    'Alcoholic hepatitis':['Complete alcohol cessation','Prednisolone (severe cases, consult doctor)','Nutritional support (thiamine, B vitamins)','Pentoxifylline (consult doctor)'],
    'Tuberculosis':       ['Isoniazid + Rifampicin + Pyrazinamide + Ethambutol (2 months)','Isoniazid + Rifampicin (4 months continuation)','Pyridoxine (B6, prevent neuropathy)','Strictly under DOTS program'],
    'Common Cold':        ['Paracetamol (fever/pain)','Cetirizine (runny nose)','Pseudoephedrine (congestion, consult doctor)','Zinc lozenges','Steam inhalation'],
    'Pneumonia':          ['Amoxicillin-Clavulanate (community-acquired)','Azithromycin (atypical pneumonia)','Ceftriaxone IV (severe, hospital)','Paracetamol (fever)'],
    'Dimorphic hemmorhoids(piles)':['Sitz baths (warm water)','Hydrocortisone cream (for inflammation)','Docusate sodium (stool softener)','Diosmin + Hesperidin (consult doctor)'],
    'Heart attack':       ['EMERGENCY: Aspirin 300mg (chew immediately)','Clopidogrel (consult doctor)','Nitroglycerin spray (if available)','Statin therapy (consult doctor)','Call ambulance — hospital treatment essential'],
    'Varicose veins':     ['Compression stockings (Grade 2)','Diosmin + Hesperidin (Daflon)','Aspirin (consult doctor)','Sclerotherapy or surgery (specialist)'],
    'Hypothyroidism':     ['Levothyroxine (T4 replacement, daily)','Dose adjusted by TSH levels','Regular thyroid function tests','Take on empty stomach in morning'],
    'Hyperthyroidism':    ['Methimazole (Carbimazole, consult doctor)','Propylthiouracil (PTU, consult doctor)','Beta-blockers: Propranolol (symptoms)','Radioiodine therapy (specialist)'],
    'Hypoglycemia':       ['Glucose tablets or 15g fast-acting sugar','Glucagon injection (severe, emergency)','Dextrose IV (hospital, severe)','Adjust diabetes medications (consult doctor)'],
    'Osteoarthritis':     ['Paracetamol (first-line pain relief)','Ibuprofen / Diclofenac (topical or oral)','Glucosamine + Chondroitin (supplement)','Duloxetine (neuropathic pain, consult doctor)'],
    'Arthritis':          ['Methotrexate (RA, consult doctor)','Hydroxychloroquine (consult doctor)','NSAIDs: Ibuprofen / Naproxen','Prednisolone (acute flares, consult doctor)'],
    '(vertigo) Paroymsal Positional Vertigo':['Betahistine (Vertin, consult doctor)','Meclizine (anti-vertigo)','Ondansetron (nausea)','Epley maneuver (physical therapy — very effective)'],
    'Acne':               ['Benzoyl peroxide (topical)','Clindamycin gel (topical, consult doctor)','Adapalene / Tretinoin (topical, consult doctor)','Doxycycline (oral, consult doctor)'],
    'Urinary tract infection':['Nitrofurantoin (first-line, consult doctor)','Trimethoprim-Sulfamethoxazole','Ciprofloxacin (consult doctor)','Phenazopyridine (pain relief, short-term)'],
    'Psoriasis':          ['Betamethasone cream (topical, consult doctor)','Calcipotriol ointment (vitamin D analog)','Methotrexate (severe, consult doctor)','Biologics: Adalimumab (specialist only)'],
    'Impetigo':           ['Mupirocin ointment (topical, first-line)','Fusidic acid cream (topical)','Flucloxacillin (oral, consult doctor)','Amoxicillin-Clavulanate (widespread cases)'],
}

# ── Disease Info ───────────────────────────────────────────────────────────────
DISEASE_INFO = {
    'Dengue':{'description':'A mosquito-borne viral infection causing severe flu-like illness.','causes':'Aedes mosquito bite carrying dengue virus (DENV 1-4)','prevention':'Use mosquito repellent, wear protective clothing, eliminate standing water','recovery_time':'1-2 weeks with proper care','when_to_see_doctor':'Immediately if bleeding, severe abdominal pain, or persistent vomiting','medicines':['Paracetamol (consult doctor)','ORS for hydration'],'diet':['Papaya leaf juice','Coconut water','High fluid intake','Light easily digestible food'],'workout':['Complete rest recommended','Light walking only after fever subsides']},
    'Malaria':{'description':'A parasitic infection transmitted by Anopheles mosquito bites.','causes':'Plasmodium parasite via Anopheles mosquito bite','prevention':'Mosquito nets, repellents, antimalarial prophylaxis when traveling','recovery_time':'2-4 weeks with treatment','when_to_see_doctor':'Immediately - malaria can be life-threatening if untreated','medicines':['Antimalarials prescribed by doctor only','Paracetamol for fever'],'diet':['Light meals','High fluid intake','Avoid oily/spicy food'],'workout':['Complete rest during fever episodes']},
    'Diabetes':{'description':'A chronic metabolic disorder where blood sugar levels remain elevated.','causes':'Insulin deficiency (Type 1) or insulin resistance (Type 2), genetics, obesity','prevention':'Healthy diet, regular exercise, weight management, blood sugar monitoring','recovery_time':'Lifelong management required','when_to_see_doctor':'If blood sugar is uncontrolled, or symptoms worsen significantly','medicines':['Metformin (consult doctor)','Insulin therapy as prescribed'],'diet':['Low glycemic index foods','High fiber','Avoid sugary beverages','Small frequent meals'],'workout':['30 min brisk walking daily','Swimming','Yoga for stress management']},
    'Common Cold':{'description':'A viral infection of the upper respiratory tract.','causes':'Rhinovirus, coronavirus, adenovirus - spread via droplets','prevention':'Handwashing, avoid close contact with infected people, vitamin C','recovery_time':'7-10 days','when_to_see_doctor':'If symptoms persist beyond 10 days or high fever develops','medicines':['Paracetamol for fever (consult doctor)','Antihistamines for runny nose'],'diet':['Warm soups','Ginger tea','Honey and lemon water','Stay hydrated'],'workout':['Rest recommended','Light stretching if feeling up to it']},
    'Hypertension':{'description':'Persistently elevated blood pressure that damages arteries over time.','causes':'Stress, unhealthy diet, obesity, genetics, sedentary lifestyle','prevention':'Low sodium diet, regular exercise, stress management, avoid smoking/alcohol','recovery_time':'Lifelong management - medication + lifestyle changes','when_to_see_doctor':'If BP consistently above 140/90 or severe headache/vision problems','medicines':['Antihypertensives as prescribed by doctor only'],'diet':['DASH diet','Low sodium','High potassium (bananas, leafy greens)','Avoid processed food'],'workout':['30 min moderate cardio 5 days/week','Yoga','Avoid heavy weightlifting']},
    'Typhoid':{'description':'A bacterial infection caused by Salmonella typhi via contaminated food/water.','causes':'Contaminated food or water, poor sanitation','prevention':'Typhoid vaccine, clean water, proper sanitation, handwashing','recovery_time':'3-4 weeks with antibiotics','when_to_see_doctor':'Immediately - typhoid needs confirmed diagnosis and antibiotics','medicines':['Antibiotics as prescribed by doctor','Paracetamol for fever'],'diet':['Soft easily digestible foods','High calorie liquid diet','Avoid raw vegetables'],'workout':['Complete rest until fully recovered']},
    'Migraine':{'description':'A neurological condition causing severe, recurring headaches.','causes':'Hormonal changes, stress, certain foods, sleep disruption, bright lights','prevention':'Identify and avoid triggers, regular sleep schedule, stress management','recovery_time':'4-72 hours per episode; chronic management needed','when_to_see_doctor':'If headache is sudden/severe, with fever or stiff neck','medicines':['Triptans, NSAIDs as prescribed','Avoid overuse of painkillers'],'diet':['Avoid caffeine, alcohol, aged cheese','Stay hydrated','Regular meal times'],'workout':['Regular low-intensity aerobic exercise','Yoga and relaxation techniques']},
    'Pneumonia':{'description':'An infection inflaming air sacs in the lungs, potentially filling them with fluid.','causes':'Bacteria (Streptococcus), viruses, fungi - spread via droplets','prevention':'Pneumococcal vaccine, flu vaccine, handwashing, no smoking','recovery_time':'1-3 weeks for mild; severe cases need hospitalization','when_to_see_doctor':'Immediately if breathing difficulty, bluish lips, or high fever','medicines':['Antibiotics as prescribed','Cough medicine (consult doctor)'],'diet':['High protein diet','Warm fluids','Vitamin C rich foods'],'workout':['Complete rest during acute phase','Breathing exercises during recovery']},
    'Heart attack':{'description':'Blockage of blood supply to part of the heart muscle causing tissue damage.','causes':'Coronary artery disease, blood clots, high cholesterol, hypertension','prevention':'Healthy diet, no smoking, regular exercise, cholesterol/BP management','recovery_time':'Varies; cardiac rehab typically 4-6 weeks','when_to_see_doctor':'EMERGENCY - Call ambulance immediately','medicines':['Emergency treatment only by medical professionals'],'diet':['Heart-healthy diet: low fat, high fiber','Omega-3 rich foods','Avoid salt and processed food'],'workout':['Supervised cardiac rehabilitation program only']},
    'Tuberculosis':{'description':'A serious bacterial infection primarily affecting the lungs.','causes':'Mycobacterium tuberculosis spread through air droplets','prevention':'BCG vaccine, avoid close contact with infected, good ventilation','recovery_time':'6-9 months of antibiotic treatment','when_to_see_doctor':'Immediately for diagnosis - TB requires confirmed testing and treatment','medicines':['4-drug regimen as strictly prescribed by doctor'],'diet':['High calorie, high protein diet','Vitamin D and zinc rich foods'],'workout':['Light activity as tolerated','Rest during acute phase']},
}
# Fill defaults for remaining diseases + wire DISEASE_MEDICINES into all
for d in DISEASES:
    meds = DISEASE_MEDICINES.get(d, ['Consult a licensed medical professional for appropriate medication'])
    if d not in DISEASE_INFO:
        DISEASE_INFO[d] = {
            'description':f'{d} is a medical condition requiring professional diagnosis.',
            'causes':'Multiple factors including infections, genetics, or lifestyle',
            'prevention':'Consult a healthcare provider for personalized prevention strategies',
            'recovery_time':'Varies by severity - consult a doctor',
            'when_to_see_doctor':'If symptoms persist or worsen, consult a doctor promptly',
            'medicines': meds,
            'diet':['Balanced nutrition supports recovery','Stay hydrated'],
            'workout':['Rest during acute phase; consult doctor before resuming exercise']
        }
    else:
        # overwrite medicines for detailed diseases too
        DISEASE_INFO[d]['medicines'] = meds
