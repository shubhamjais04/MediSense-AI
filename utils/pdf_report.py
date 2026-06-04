"""
MediSense AI — Complete PDF Report Generator
Full report: symptoms, predictions, disease info, causes, prevention,
recovery, medicines, diet, workout — nothing truncated.
"""

import datetime, os


def _s(text):
    """Strip non-latin-1 chars for FPDF compatibility."""
    return str(text).encode('latin-1', errors='replace').decode('latin-1')


def generate_pdf(selected_symptoms, top3, severity, duration_days, frequency):
    from fpdf import FPDF

    top1 = top3[0]
    info = top1.get('info', {})
    sev_label = 'Severe' if severity >= 7 else 'Moderate' if severity >= 4 else 'Mild'

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_page()

    # ── Header ─────────────────────────────────────────────────────────────────
    pdf.set_fill_color(15, 32, 87)
    pdf.rect(0, 0, 210, 40, 'F')

    # Accent strip
    pdf.set_fill_color(14, 165, 233)
    pdf.rect(0, 37, 210, 3, 'F')

    pdf.set_font('Helvetica', 'B', 20)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(12, 9)
    pdf.cell(0, 10, 'MediSense AI  -  Medical Report', ln=True)

    pdf.set_font('Helvetica', '', 10)
    pdf.set_xy(12, 23)
    pdf.cell(90, 7, _s(f'Generated: {datetime.datetime.now().strftime("%d %B %Y, %I:%M %p")}'))
    pdf.set_xy(110, 23)
    pdf.cell(0, 7, _s(f'Model v2.0  |  For Educational Purposes Only'))

    pdf.set_text_color(30, 30, 30)
    pdf.set_xy(12, 48)

    # ── Disclaimer ─────────────────────────────────────────────────────────────
    pdf.set_fill_color(255, 240, 240)
    pdf.set_draw_color(220, 100, 100)
    pdf.rect(10, 46, 190, 14, 'FD')
    pdf.set_font('Helvetica', 'BI', 8.5)
    pdf.set_text_color(160, 30, 30)
    pdf.set_xy(14, 49)
    pdf.multi_cell(182, 5, _s(
        'DISCLAIMER: This AI-generated report is for INFORMATIONAL PURPOSES ONLY. '
        'It does NOT constitute medical advice, diagnosis, or treatment. '
        'Always consult a licensed healthcare professional.'
    ))
    pdf.set_text_color(30, 30, 30)
    pdf.ln(4)

    # ── Helper functions ────────────────────────────────────────────────────────
    def section_header(title, r=30, g=64, b=175):
        pdf.set_font('Helvetica', 'B', 11)
        pdf.set_fill_color(r, g, b)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(190, 8, _s(f'   {title}'), ln=True, fill=True)
        pdf.set_text_color(30, 30, 30)
        pdf.ln(2)

    def kv_row(label, value, label_w=52):
        pdf.set_font('Helvetica', 'B', 10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(label_w, 7, _s(label + ':'))
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(20, 20, 20)
        # Use multi_cell for long values so they wrap
        x_after = pdf.get_x()
        y_before = pdf.get_y()
        pdf.multi_cell(190 - label_w, 7, _s(str(value)))
        # ensure we're on next line after multi_cell
        pdf.set_x(12)

    def bullet_list(items, bullet='->'):
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(20, 20, 20)
        for item in items:
            pdf.set_x(14)
            pdf.cell(6, 6, bullet)
            pdf.multi_cell(180, 6, _s(str(item)))
        pdf.ln(1)

    def divider():
        pdf.set_draw_color(220, 225, 240)
        pdf.line(12, pdf.get_y(), 198, pdf.get_y())
        pdf.ln(3)

    # ── Section 1: Patient Symptoms ────────────────────────────────────────────
    section_header('1.  Reported Symptoms & Clinical Parameters')
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(50, 50, 50)
    pdf.set_x(12)
    pdf.cell(0, 7, 'Symptoms Selected:', ln=True)
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(20, 20, 20)
    pdf.set_x(14)
    symp_str = _s(', '.join(s.replace('_', ' ').title() for s in selected_symptoms))
    pdf.multi_cell(182, 6, symp_str)
    pdf.ln(2)

    kv_row('Duration',       f'{duration_days} day(s)')
    kv_row('Frequency',      frequency)
    kv_row('Severity Score', f'{severity} / 10  [{sev_label}]')
    kv_row('Symptoms Count', f'{len(selected_symptoms)} symptom(s) reported')
    pdf.ln(3)

    # ── Section 2: Disease Predictions ────────────────────────────────────────
    section_header('2.  AI Disease Predictions  (Top 3)')
    rank_labels = ['#1  Most Likely', '#2  Possible', '#3  Consider']
    for i, res in enumerate(top3):
        pdf.set_font('Helvetica', 'B', 10)
        pdf.set_text_color(29, 78, 216)
        pdf.set_x(12)
        pdf.cell(70, 7, _s(f'  {rank_labels[i]}:  {res["disease"]}'))
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(50, 50, 50)
        pdf.cell(55, 7, _s(f'Probability: {res["probability"]}%'))
        pdf.set_font('Helvetica', 'B', 10)
        risk = res["risk"]
        color_map = {'High': (220,38,38), 'Medium': (217,119,6), 'Low': (5,150,105)}
        r2,g2,b2 = color_map.get(risk, (100,100,100))
        pdf.set_text_color(r2, g2, b2)
        pdf.cell(0, 7, _s(f'Risk Level: {risk}'), ln=True)
    pdf.set_text_color(30, 30, 30)
    pdf.ln(3)

    # ── Section 3: Disease Info (Top Prediction) ───────────────────────────────
    section_header(f'3.  Disease Information:  {top1["disease"]}')
    fields = [
        ('Description',      info.get('description',  'N/A')),
        ('Causes',           info.get('causes',        'N/A')),
        ('Prevention',       info.get('prevention',    'N/A')),
        ('Recovery Time',    info.get('recovery_time', 'N/A')),
        ('When to See Doctor', info.get('when_to_see_doctor', 'N/A')),
    ]
    for label, val in fields:
        pdf.set_x(12)
        pdf.set_font('Helvetica', 'B', 10)
        pdf.set_text_color(60, 60, 80)
        pdf.cell(0, 7, _s(label + ':'), ln=True)
        pdf.set_x(16)
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(20, 20, 20)
        pdf.multi_cell(182, 6, _s(val))
        pdf.ln(2)
    divider()

    # ── Section 4: Medicines ───────────────────────────────────────────────────
    section_header('4.  Medicines  (Informational Only - Always Consult Doctor)', r=5, g=80, b=130)
    medicines = info.get('medicines', ['Consult a licensed medical professional for appropriate medication'])
    bullet_list(medicines)
    pdf.set_font('Helvetica', 'I', 8.5)
    pdf.set_text_color(130, 50, 50)
    pdf.set_x(12)
    pdf.multi_cell(186, 5, _s('* The above medicines are listed for informational reference only. '
        'Do not self-medicate. Dosage, suitability, and contraindications must be assessed by a doctor.'))
    pdf.set_text_color(30, 30, 30)
    pdf.ln(3)

    # ── Section 5: Diet Recommendations ───────────────────────────────────────
    section_header('5.  Diet Recommendations', r=5, g=100, b=50)
    diet = info.get('diet', ['Follow a balanced, nutritious diet', 'Stay well hydrated', 'Avoid junk food during recovery'])
    bullet_list(diet)

    # ── Section 6: Workout / Activity Plan ────────────────────────────────────
    section_header('6.  Workout & Activity Plan', r=80, g=30, b=140)
    workout = info.get('workout', ['Rest during the acute phase', 'Consult your doctor before resuming exercise'])
    bullet_list(workout)

    # ── Section 7: Symptom Contribution ───────────────────────────────────────
    section_header('7.  Symptom Analysis  (Why This Diagnosis?)', r=40, g=40, b=40)
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(20, 20, 20)
    pdf.set_x(12)
    pdf.multi_cell(186, 6, _s(
        f'The AI identified {top1["disease"]} as the most likely condition based on the '
        f'pattern matching between your reported symptoms and disease profiles in the training data.'
    ))
    pdf.ln(2)
    from utils.constants import DISEASE_SYMPTOMS
    known = set(DISEASE_SYMPTOMS.get(top1['disease'], []))
    matched   = [s for s in selected_symptoms if s in known]
    unmatched = [s for s in selected_symptoms if s not in known]
    if matched:
        pdf.set_font('Helvetica', 'B', 10)
        pdf.set_text_color(29, 78, 216)
        pdf.set_x(12)
        pdf.cell(0, 7, _s(f'Directly linked symptoms ({len(matched)}):'), ln=True)
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(20, 20, 20)
        pdf.set_x(16)
        pdf.multi_cell(182, 6, _s(', '.join(s.replace('_',' ').title() for s in matched)))
        pdf.ln(2)
    if unmatched:
        pdf.set_font('Helvetica', 'B', 10)
        pdf.set_text_color(100, 100, 100)
        pdf.set_x(12)
        pdf.cell(0, 7, _s(f'Indirect / supporting symptoms ({len(unmatched)}):'), ln=True)
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(100, 100, 100)
        pdf.set_x(16)
        pdf.multi_cell(182, 6, _s(', '.join(s.replace('_',' ').title() for s in unmatched)))
        pdf.ln(2)

    # ── Section 8: Severity Explanation ───────────────────────────────────────
    divider()
    section_header('8.  Severity Score Explanation', r=40, g=40, b=40)
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(20, 20, 20)
    pdf.set_x(12)
    pdf.multi_cell(186, 6, _s(
        f'Severity Score: {severity}/10  [{sev_label}]\n'
        f'Formula: Symptom Weights x Duration Factor x Frequency Factor\n'
        f'Duration: {duration_days} day(s)  |  Frequency: {frequency}\n\n'
        f'Score Interpretation:\n'
        f'  0.0 - 3.9  ->  Mild      (Monitor at home, rest and hydrate)\n'
        f'  4.0 - 6.9  ->  Moderate  (Consult a doctor within 24-48 hours)\n'
        f'  7.0 - 10.0 ->  Severe    (Seek immediate medical attention)'
    ))
    pdf.ln(3)

    # ── Footer ──────────────────────────────────────────────────────────────────
    pdf.set_y(-22)
    pdf.set_draw_color(29, 78, 216)
    pdf.line(12, pdf.get_y(), 198, pdf.get_y())
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 8)
    pdf.set_text_color(120, 120, 140)
    pdf.cell(95, 5, _s('MediSense AI  |  Shubham Jaiswal'))
    pdf.cell(0, 5, _s('For Educational Purposes Only  |  Not a Medical Document'), align='R')

    return bytes(pdf.output())
