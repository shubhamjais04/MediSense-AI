"""
MediSense AI v2.0 — Fixed Streamlit Application
All 5 pages fully working, light mode, proper sidebar, complete PDF
"""

import streamlit as st
import plotly.graph_objects as go
import datetime, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import utils as u

# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MediSense AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── CSS: Force light mode everywhere, fix sidebar, fix inputs ──────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500;600;700&display=swap');

/* ── Global light mode ── */
*, *::before, *::after { box-sizing: border-box; }
html, body { background: #F0F4FF !important; }
.stApp { background: #F0F4FF !important; }
[data-testid="stAppViewContainer"] { background: #F0F4FF !important; }
[data-testid="stMain"] { background: #F0F4FF !important; }
[data-testid="block-container"] { background: #F0F4FF !important; }
[data-testid="stHeader"] { background: rgba(240,244,255,0.95) !important; backdrop-filter: blur(8px); }

/* ── Sidebar background ── */
[data-testid="stSidebar"] { background: linear-gradient(175deg, #0f2057 0%, #1a3aa8 50%, #2152cc 100%) !important; }
[data-testid="stSidebar"] > div:first-child { background: transparent !important; }
[data-testid="stSidebar"] .stMarkdown { color: #fff !important; }
[data-testid="stSidebar"] p, [data-testid="stSidebar"] span,
[data-testid="stSidebar"] label, [data-testid="stSidebar"] div { color: #fff !important; }

/* ── Sidebar radio buttons ── */
[data-testid="stSidebar"] .stRadio label { color: rgba(255,255,255,0.85) !important; font-size: 0.9rem !important; padding: 6px 0 !important; }
[data-testid="stSidebar"] .stRadio [data-testid="stMarkdownContainer"] p { color: rgba(255,255,255,0.85) !important; }

/* ── Sidebar multiselect ── */
[data-testid="stSidebar"] [data-baseweb="select"] { background: rgba(255,255,255,0.12) !important; border-radius: 10px !important; }
[data-testid="stSidebar"] [data-baseweb="select"] > div { background: rgba(255,255,255,0.12) !important; border: 1px solid rgba(255,255,255,0.3) !important; border-radius: 10px !important; }
[data-testid="stSidebar"] [data-baseweb="select"] input { background: transparent !important; color: #fff !important; }
[data-testid="stSidebar"] [data-baseweb="select"] input::placeholder { color: rgba(255,255,255,0.6) !important; }
[data-testid="stSidebar"] [data-baseweb="select"] [data-baseweb="tag"] { background: rgba(255,255,255,0.25) !important; border: none !important; }
[data-testid="stSidebar"] [data-baseweb="select"] [data-baseweb="tag"] span { color: #fff !important; }
[data-testid="stSidebar"] [data-baseweb="select"] svg { fill: rgba(255,255,255,0.7) !important; }

/* ── Sidebar selectbox ── */
[data-testid="stSidebar"] [data-baseweb="select"] [data-testid="stWidgetLabel"] { color: #fff !important; }
[data-testid="stSidebar"] .stSelectbox label { color: #fff !important; }
[data-testid="stSidebar"] .stSelectbox [data-testid="stWidgetLabel"] p { color: #fff !important; }

/* ── Sidebar slider ── */
[data-testid="stSidebar"] .stSlider [data-testid="stWidgetLabel"] p { color: #fff !important; }
[data-testid="stSidebar"] .stSlider > div { color: #fff !important; }
[data-testid="stSidebar"] .stSlider [data-testid="stTickBar"] { color: #fff !important; }
[data-testid="stSidebar"] .stSlider span { color: #fff !important; }
[data-testid="stSidebar"] .stSlider p { color: #fff !important; }
[data-testid="stSidebar"] .stButton > button { color: #fff !important; background: rgba(255,255,255,0.2) !important; border: 1.5px solid rgba(255,255,255,0.5) !important; }
[data-testid="stSidebar"] .stButton > button p { color: #fff !important; }
[data-testid="stSidebar"] .stButton > button span { color: #fff !important; }
[data-testid="stSidebar"] .stButton > button * { color: #fff !important; }
            
/* ── Dropdown menu popup (fix black dropdown) ── */
[data-baseweb="popover"] { background: #fff !important; }
[data-baseweb="menu"] { background: #fff !important; }
[data-baseweb="menu"] ul { background: #fff !important; }
[data-baseweb="menu"] li { background: #fff !important; color: #1a1a2e !important; }
[data-baseweb="menu"] li:hover { background: #eff6ff !important; color: #1d4ed8 !important; }
[data-baseweb="option"] { background: #fff !important; color: #1a1a2e !important; }
ul[role="listbox"] { background: #fff !important; }
ul[role="listbox"] li { color: #1a1a2e !important; background: #fff !important; }
li[role="option"] { background: #fff !important; color: #1a1a2e !important; }
li[role="option"]:hover { background: #eff6ff !important; color: #1d4ed8 !important; }

/* ── Main content text — all dark, no grey ── */
h1, h2, h3, h4, h5, h6 { color: #1e3a8a !important; font-family: 'DM Serif Display', serif !important; }
p, span, div, label { color: #1a1a2e !important; font-family: 'DM Sans', sans-serif; }
.stCaption, [data-testid="stCaptionContainer"] p { color: #374151 !important; }
[data-testid="stMarkdownContainer"] p { color: #1a1a2e !important; }

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #1a3aa8, #2563eb) !important;
    color: #fff !important; border: none !important;
    border-radius: 12px !important; padding: 10px 28px !important;
    font-family: 'DM Sans', sans-serif !important; font-weight: 600 !important;
    font-size: 0.95rem !important;
    box-shadow: 0 4px 15px rgba(37,99,235,0.35) !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover { transform: translateY(-2px) !important; box-shadow: 0 8px 25px rgba(37,99,235,0.45) !important; }

/* ── Download button ── */
[data-testid="stDownloadButton"] > button {
    background: linear-gradient(135deg, #047857, #10b981) !important;
    color: #fff !important; border: none !important; border-radius: 12px !important;
    font-weight: 600 !important; box-shadow: 0 4px 15px rgba(16,185,129,0.35) !important;
}

/* ── Input fields in main area ── */
.stTextInput input { background: #fff !important; border: 1.5px solid #c7d2fe !important; border-radius: 10px !important; color: #1a1a2e !important; padding: 10px 14px !important; }
.stTextInput input:focus { border-color: #2563eb !important; box-shadow: 0 0 0 3px rgba(37,99,235,0.15) !important; }
.stTextInput input::placeholder { color: #9ca3af !important; }

/* ── Tabs ── */
[data-testid="stTabs"] [role="tab"] { font-family: 'DM Sans', sans-serif !important; font-weight: 600 !important; color: #6b7280 !important; }
[data-testid="stTabs"] [role="tab"][aria-selected="true"] { color: #1d4ed8 !important; border-bottom: 3px solid #1d4ed8 !important; }

/* ── Expander ── */
details summary { color: #1e3a8a !important; font-weight: 600 !important; font-family: 'DM Sans', sans-serif !important; }
details { background: #fff !important; border: 1px solid #e0e7ff !important; border-radius: 12px !important; margin-bottom: 8px !important; padding: 4px 0 !important; }

/* ── Component classes ── */
.hero { background: linear-gradient(135deg, #0f2057, #1d4ed8 55%, #0ea5e9); border-radius: 20px; padding: 32px 40px; margin-bottom: 24px; color: #fff !important; position: relative; overflow: hidden; box-shadow: 0 16px 48px rgba(29,78,216,0.3); }
.hero * { color: #fff !important; }
.hero-title { font-family: 'DM Serif Display', serif; font-size: 2.6rem; font-weight: 400; margin: 0 0 6px; line-height: 1.1; }
.hero-sub { font-size: 0.97rem; opacity: 0.82; margin: 0; font-weight: 300; }

.mcard { background: #fff; border-radius: 16px; padding: 22px 24px; box-shadow: 0 2px 14px rgba(29,78,216,0.08); border: 1px solid #e0e7ff; text-align: center; transition: transform 0.2s, box-shadow 0.2s; }
.mcard:hover { transform: translateY(-3px); box-shadow: 0 8px 28px rgba(29,78,216,0.16); }
.mcard-val { font-family: 'DM Serif Display', serif; font-size: 2.2rem; color: #1d4ed8 !important; margin: 0; line-height: 1; }
.mcard-lbl { font-size: 0.75rem; color: #6b7280 !important; margin: 6px 0 0; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; }

.pcard { background: #fff; border-radius: 14px; padding: 18px 22px; margin-bottom: 12px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); border-left: 5px solid #2563eb; transition: transform 0.18s; }
.pcard:hover { transform: translateX(4px); }
.pcard.r1 { border-left-color: #1d4ed8; background: linear-gradient(135deg, #eff6ff 0%, #fff 60%); }
.pcard.r2 { border-left-color: #06b6d4; }
.pcard.r3 { border-left-color: #8b5cf6; }
.pcard-rank { font-size: 0.72rem; color: #9ca3af !important; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 4px; }
.pcard-disease { font-family: 'DM Serif Display', serif; font-size: 1.35rem; color: #1a1a2e !important; margin: 0 0 8px; }
.pcard-prob { font-size: 1.05rem; font-weight: 700; color: #1d4ed8 !important; }

.risk-high { background: #fee2e2; color: #dc2626 !important; padding: 3px 12px; border-radius: 20px; font-size: 0.78rem; font-weight: 700; display: inline-block; }
.risk-medium { background: #fef3c7; color: #d97706 !important; padding: 3px 12px; border-radius: 20px; font-size: 0.78rem; font-weight: 700; display: inline-block; }
.risk-low { background: #d1fae5; color: #059669 !important; padding: 3px 12px; border-radius: 20px; font-size: 0.78rem; font-weight: 700; display: inline-block; }

.sh { font-family: 'DM Serif Display', serif; font-size: 1.4rem; color: #1e3a8a !important; margin: 28px 0 14px; padding-bottom: 8px; border-bottom: 2px solid #e0e7ff; }

.iblock { background: #fff; border-radius: 12px; padding: 14px 18px; margin-bottom: 10px; box-shadow: 0 1px 6px rgba(0,0,0,0.05); border: 1px solid #e0e7ff; }
.iblock-lbl { font-size: 0.7rem; color: #6b7280 !important; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 4px; }
.iblock-val { font-size: 0.93rem; color: #1a1a2e !important; line-height: 1.55; }

.pill { display: inline-block; padding: 4px 12px; margin: 3px; border-radius: 20px; font-size: 0.78rem; font-weight: 600; }
.pm { background: #dbeafe; color: #1d4ed8 !important; border: 1px solid #bfdbfe; }
.pw { background: #f3f4f6; color: #6b7280 !important; border: 1px solid #e5e7eb; }
.pd { background: #f0fdf4; color: #166534 !important; border: 1px solid #bbf7d0; }
.pmed { background: #eff6ff; color: #1d4ed8 !important; border: 1px solid #bfdbfe; }
.pwk { background: #fdf4ff; color: #7e22ce !important; border: 1px solid #e9d5ff; }

.hrow { background: #fff; border-radius: 10px; padding: 12px 16px; margin-bottom: 7px; box-shadow: 0 1px 5px rgba(0,0,0,0.05); border: 1px solid #e0e7ff; }

.aw { background: linear-gradient(135deg, #fef2f2, #fff5f5); border: 1.5px solid #fca5a5; border-radius: 12px; padding: 12px 18px; margin: 12px 0; }
.ai { background: linear-gradient(135deg, #eff6ff, #f8faff); border: 1.5px solid #bfdbfe; border-radius: 12px; padding: 12px 18px; margin: 12px 0; }

.landing-box { background: #fff; border-radius: 18px; padding: 40px 32px; margin-top: 20px; box-shadow: 0 2px 16px rgba(29,78,216,0.07); border: 1px solid #e0e7ff; text-align: center; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding:16px 0 24px'>
        <div style='font-size:3rem; margin-bottom:6px'>🩺</div>
        <div style='font-family:"DM Serif Display",serif; font-size:1.5rem; color:#fff; font-weight:400'>MediSense AI</div>
        <div style='font-size:0.72rem; color:rgba(255,255,255,0.55); margin-top:3px'>v2.0 · Health Intelligence Platform</div>
    </div>
    <hr style='border:none; border-top:1px solid rgba(255,255,255,0.2); margin:0 0 20px'>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        ["🔬 Diagnose", "📊 Analytics Dashboard", "📋 Prediction History", "📚 Disease Library", "⚙️ Model Monitoring"],
        label_visibility="collapsed"
    )

    st.markdown("<hr style='border:none; border-top:1px solid rgba(255,255,255,0.2); margin:20px 0'>", unsafe_allow_html=True)

    # Symptom inputs only on Diagnose page
    if page == "🔬 Diagnose":
        st.markdown("<div style='font-size:0.8rem; font-weight:700; color:rgba(255,255,255,0.9); letter-spacing:0.05em; margin-bottom:8px'>🔍 SELECT YOUR SYMPTOMS</div>", unsafe_allow_html=True)

        display_map = {s.replace('_', ' ').title(): s for s in u.SYMPTOMS}
        selected_display = st.multiselect(
            "Symptoms",
            options=list(display_map.keys()),
            placeholder="Type to search symptoms...",
            label_visibility="collapsed"
        )
        selected_symptoms = [display_map[d] for d in selected_display]

        st.markdown("<div style='font-size:0.8rem; font-weight:700; color:rgba(255,255,255,0.9); letter-spacing:0.05em; margin-top:18px; margin-bottom:8px'>⏱️ DURATION & FREQUENCY</div>", unsafe_allow_html=True)

        duration_days = st.slider("Duration (days)", 1, 30, 1, label_visibility="visible")
        frequency = st.selectbox("Frequency", ["Once", "Occasionally", "Daily", "Multiple times/day"], label_visibility="visible")

        st.markdown("<div style='margin-top:16px'>", unsafe_allow_html=True)
        analyze_btn = st.button("🔬 Analyze Symptoms", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        selected_symptoms, duration_days, frequency, analyze_btn = [], 1, "Daily", False

    st.markdown("""
    <div style='position:fixed; bottom:16px; left:0; right:0; text-align:center;
         font-size:0.65rem; color:rgba(255,255,255,0.35); line-height:1.6; pointer-events:none'>
        Shubham Jaiswal · Amdox Technologies · 2025
    </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — DIAGNOSE
# ══════════════════════════════════════════════════════════════════════════════
if page == "🔬 Diagnose":
    st.markdown("""
    <div class='hero'>
        <div class='hero-title'>🩺 MediSense AI</div>
        <div class='hero-sub'>AI-powered symptom analysis · Top-3 disease predictions · Explainable diagnosis · PDF medical reports</div>
    </div>""", unsafe_allow_html=True)

    if not analyze_btn:
        c1, c2, c3 = st.columns(3)
        for col, (val, lbl) in zip([c1,c2,c3], [
            (u.meta.get('n_diseases', 41), "Diseases Covered"),
            (u.meta.get('n_symptoms', 132), "Symptoms Tracked"),
            (f"{u.meta.get('cv_accuracy', 0.99)*100:.1f}%", "CV Accuracy"),
        ]):
            with col:
                st.markdown(f"<div class='mcard'><div class='mcard-val'>{val}</div><div class='mcard-lbl'>{lbl}</div></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class='landing-box'>
            <div style='font-size:3.5rem; margin-bottom:14px'>👈</div>
            <div style='font-family:"DM Serif Display",serif; font-size:1.5rem; color:#1e3a8a; margin-bottom:10px'>
                Select your symptoms from the sidebar
            </div>
            <div style='color:#6b7280; font-size:0.95rem; line-height:1.7; max-width:520px; margin:0 auto'>
                Search and pick your symptoms, set how long you've had them and how often,<br>
                then click <strong style="color:#1d4ed8">Analyze Symptoms</strong> for your AI-powered diagnosis.
            </div>
        </div>""", unsafe_allow_html=True)

    elif not selected_symptoms:
        st.warning("⚠️ Please select at least one symptom from the sidebar before analyzing.")

    else:
        with st.spinner("Analyzing your symptoms..."):
            top3 = u.predict_top3(selected_symptoms, duration_days, frequency)
            severity = u.compute_severity(selected_symptoms, duration_days, frequency)
            contributions = u.get_symptom_contributions(selected_symptoms, top3[0]['disease'])
            u.save_prediction(selected_symptoms, top3, severity, top3[0]['risk'], duration_days, frequency)

        # ── Feature 3: Top-3 Predictions ──────────────────────────────────
        st.markdown("<div class='sh'>🎯 Disease Predictions</div>", unsafe_allow_html=True)
        col_cards, col_donut = st.columns([3, 2])

        with col_cards:
            for i, res in enumerate(top3):
                rclass = ['r1','r2','r3'][i]
                medal  = ['🥇','🥈','🥉'][i]
                rc     = f"risk-{res['risk'].lower()}"
                st.markdown(f"""
                <div class='pcard {rclass}'>
                    <div class='pcard-rank'>{medal} Prediction #{i+1}</div>
                    <div class='pcard-disease'>{res['disease']}</div>
                    <div style='display:flex; align-items:center; gap:10px'>
                        <span class='pcard-prob'>{res['probability']}%</span>
                        <span class='{rc}'>{res['risk']} Risk</span>
                    </div>
                </div>""", unsafe_allow_html=True)

        with col_donut:
            others = max(0, 100 - sum(r['probability'] for r in top3))
            fig = go.Figure(go.Pie(
                labels=[r['disease'].split('(')[0].strip() for r in top3] + ['Other'],
                values=[r['probability'] for r in top3] + [others],
                hole=0.55,
                marker=dict(colors=['#1d4ed8','#06b6d4','#8b5cf6','#e5e7eb']),
                textinfo='label+percent',
                textfont=dict(size=10, family='DM Sans'),
                showlegend=False,
            ))
            fig.update_layout(
                height=260, margin=dict(t=8,b=8,l=8,r=8),
                annotations=[dict(text='Top 3', x=0.5, y=0.5,
                    font=dict(size=14, family='DM Serif Display', color='#1e3a8a'), showarrow=False)],
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font=dict(family='DM Sans'),
            )
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar':False})

        # ── Feature 5 & 6: Severity Score ─────────────────────────────────
        st.markdown("<div class='sh'>📊 Severity Analysis</div>", unsafe_allow_html=True)
        sev_color = '#dc2626' if severity >= 7 else '#d97706' if severity >= 4 else '#059669'
        sev_label = 'Severe' if severity >= 7 else 'Moderate' if severity >= 4 else 'Mild'

        cg, ct = st.columns([1, 2])
        with cg:
            fig_g = go.Figure(go.Indicator(
                mode="gauge+number",
                value=severity,
                number={'suffix':'/10','font':{'size':24,'family':'DM Serif Display','color':sev_color}},
                gauge={
                    'axis':{'range':[0,10],'tickwidth':1,'tickcolor':'#94a3b8'},
                    'bar':{'color':sev_color,'thickness':0.28},
                    'bgcolor':'white',
                    'steps':[
                        {'range':[0,3.9],'color':'#dcfce7'},
                        {'range':[4,6.9],'color':'#fef9c3'},
                        {'range':[7,10],'color':'#fee2e2'},
                    ],
                    'threshold':{'line':{'color':sev_color,'width':3},'thickness':0.75,'value':severity},
                },
            ))
            fig_g.update_layout(height=220, margin=dict(t=30,b=10,l=18,r=18),
                paper_bgcolor='rgba(0,0,0,0)', font=dict(family='DM Sans'))
            st.plotly_chart(fig_g, use_container_width=True, config={'displayModeBar':False})

        with ct:
            advice = {
                'Severe':   "🚨 <strong>Seek medical attention immediately.</strong> Your symptoms suggest a potentially serious condition. Do not delay consulting a doctor.",
                'Moderate': "⚠️ <strong>Consult a doctor soon.</strong> Your symptoms are moderate in severity and should not be ignored.",
                'Mild':     "✅ <strong>Monitor your symptoms.</strong> Your condition appears mild. Rest, stay hydrated, and see a doctor if symptoms worsen.",
            }[sev_label]
            st.markdown(f"""
            <div style='background:#fff; border-radius:16px; padding:24px 28px; height:100%;
                 box-shadow:0 2px 12px rgba(0,0,0,0.06); border:1px solid #e0e7ff; min-height:180px;'>
                <div style='font-family:"DM Serif Display",serif; font-size:1.7rem; color:{sev_color}; margin-bottom:8px'>
                    {sev_label} Condition
                </div>
                <div style='color:#6b7280; font-size:0.85rem; margin-bottom:14px'>
                    Score: <strong style="color:{sev_color}">{severity}/10</strong>
                    &nbsp;·&nbsp; Duration: <strong>{duration_days} day(s)</strong>
                    &nbsp;·&nbsp; Frequency: <strong>{frequency}</strong>
                </div>
                <div style='color:#374151; font-size:0.93rem; line-height:1.65'>{advice}</div>
            </div>""", unsafe_allow_html=True)

        # ── Feature 2: Explainable AI ──────────────────────────────────────
        st.markdown("<div class='sh'>🔍 Why This Diagnosis?</div>", unsafe_allow_html=True)
        cp, cb_ = st.columns([2, 3])

        with cp:
            pills = "".join(
                f"<span class='pill {'pm' if c['match'] else 'pw'}'>{'✓' if c['match'] else '·'} {c['symptom']}</span>"
                for c in contributions
            )
            st.markdown(f"""
            <div style='background:#fff; border-radius:14px; padding:18px 20px;
                 box-shadow:0 2px 10px rgba(0,0,0,0.06); border:1px solid #e0e7ff;'>
                <div style='font-size:0.7rem; color:#6b7280; font-weight:700; text-transform:uppercase;
                     letter-spacing:0.06em; margin-bottom:10px'>
                    Symptom match for: {top3[0]['disease']}
                </div>
                {pills}
                <div style='margin-top:12px; font-size:0.73rem; color:#9ca3af'>
                    ✓ Blue = directly linked · Grey = indirect
                </div>
            </div>""", unsafe_allow_html=True)

        with cb_:
            top10 = contributions[:10]
            if top10:
                fig_b = go.Figure(go.Bar(
                    y=[c['symptom'] for c in top10][::-1],
                    x=[c['weight']  for c in top10][::-1],
                    orientation='h',
                    marker=dict(
                        color=['#1d4ed8' if c['match'] else '#94a3b8' for c in top10][::-1],
                        line=dict(width=0)
                    ),
                    text=[f"{c['weight']:.2f}" for c in top10][::-1],
                    textposition='outside',
                    textfont=dict(size=10),
                ))
                fig_b.update_layout(
                    height=max(200, len(top10)*34),
                    margin=dict(t=6,b=6,l=8,r=60),
                    xaxis=dict(showgrid=True, gridcolor='#f1f5f9', title='Weight', color='#6b7280'),
                    yaxis=dict(showgrid=False, color='#374151'),
                    paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(family='DM Sans', size=11, color='#374151'),
                )
                st.plotly_chart(fig_b, use_container_width=True, config={'displayModeBar':False})

        # ── Feature 11: Disease Information ───────────────────────────────
        st.markdown(f"<div class='sh'>📋 About: {top3[0]['disease']}</div>", unsafe_allow_html=True)
        info = top3[0]['info']
        ci1, ci2 = st.columns(2)
        with ci1:
            for lbl, key in [('Description','description'),('Causes','causes'),('Prevention','prevention')]:
                st.markdown(f"""<div class='iblock'>
                    <div class='iblock-lbl'>{lbl}</div>
                    <div class='iblock-val'>{info.get(key,'N/A')}</div>
                </div>""", unsafe_allow_html=True)
        with ci2:
            for lbl, key in [('Recovery Time','recovery_time'),('When to See Doctor','when_to_see_doctor')]:
                st.markdown(f"""<div class='iblock'>
                    <div class='iblock-lbl'>{lbl}</div>
                    <div class='iblock-val'>{info.get(key,'N/A')}</div>
                </div>""", unsafe_allow_html=True)

        # ── Feature 7: Medicines / Diet / Workout ─────────────────────────
        cm_, cd_, cw_ = st.columns(3)
        with cm_:
            st.markdown("**💊 Medicines** *(informational only)*")
            st.markdown("".join(f"<span class='pill pmed'>{m}</span>" for m in info.get('medicines',[])), unsafe_allow_html=True)
        with cd_:
            st.markdown("**🥗 Diet Plan**")
            st.markdown("".join(f"<span class='pill pd'>{d}</span>" for d in info.get('diet',[])), unsafe_allow_html=True)
        with cw_:
            st.markdown("**🏃 Workout Plan**")
            st.markdown("".join(f"<span class='pill pwk'>{w}</span>" for w in info.get('workout',[])), unsafe_allow_html=True)

        st.markdown("""
        <div class='aw'>
            <strong style='color:#dc2626'>⚕️ Medical Disclaimer:</strong>
            <span style='color:#7f1d1d; font-size:0.9rem'> This AI prediction is for informational purposes only.
            Always consult a qualified healthcare professional for accurate diagnosis and treatment.</span>
        </div>""", unsafe_allow_html=True)

        # ── Feature 9: PDF Report ──────────────────────────────────────────
        st.markdown("<div class='sh'>📥 Download Medical Report</div>", unsafe_allow_html=True)
        pdf_bytes = u.generate_pdf(selected_symptoms, top3, severity, duration_days, frequency)
        col_dl, col_info = st.columns([1, 3])
        with col_dl:
            st.download_button(
                label="📄 Download PDF Report",
                data=pdf_bytes,
                file_name=f"MediSense_Report_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
                mime="application/pdf",
            )
        with col_info:
            st.caption("Includes: symptoms · top-3 predictions · confidence scores · disease info · causes · prevention · diet plan · workout plan · medicines (informational)")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — ANALYTICS DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📊 Analytics Dashboard":
    st.markdown("""
    <div class='hero'>
        <div class='hero-title'>📊 Analytics Dashboard</div>
        <div class='hero-sub'>Prediction trends · Disease distribution · Risk breakdown · Severity analytics</div>
    </div>""", unsafe_allow_html=True)

    analytics = u.get_analytics()
    if analytics is None:
        st.info("💡 No predictions yet. Go to **🔬 Diagnose** to make your first prediction!")
    else:
        c1, c2, c3, c4 = st.columns(4)
        for col, (val, lbl) in zip([c1,c2,c3,c4], [
            (analytics['total'],             "Total Predictions"),
            (f"{analytics['avg_severity']:.1f}/10", "Avg Severity"),
            (analytics['risk_dist'].get('High', 0), "High Risk Cases"),
            (len(analytics['top_diseases']), "Unique Diseases"),
        ]):
            with col:
                st.markdown(f"<div class='mcard'><div class='mcard-val'>{val}</div><div class='mcard-lbl'>{lbl}</div></div>", unsafe_allow_html=True)

        st.markdown("<div class='sh'>🏥 Most Predicted Diseases</div>", unsafe_allow_html=True)
        ca, cb = st.columns(2)
        with ca:
            diseases = list(analytics['top_diseases'].keys())
            counts   = list(analytics['top_diseases'].values())
            # Shorten disease names for display
            short_names = [d[:28]+'…' if len(d)>28 else d for d in diseases]
            fig = go.Figure(go.Bar(
                x=counts[::-1],
                y=short_names[::-1],
                orientation='h',
                marker=dict(
                    color=['#1d4ed8','#2563eb','#3b82f6','#60a5fa','#93c5fd',
                           '#06b6d4','#0e7490','#0891b2','#0ea5e9','#38bdf8'][:len(counts)][::-1],
                    line=dict(width=0)
                ),
                text=counts[::-1],
                textposition='outside',
                textfont=dict(size=11, color='#374151'),
            ))
            fig.update_layout(
                height=max(280, len(diseases)*40),
                margin=dict(t=10,b=10,l=10,r=50),
                paper_bgcolor='#fff', plot_bgcolor='#fff',
                xaxis=dict(showgrid=True, gridcolor='#e5e7eb', color='#000000', title='Count', tickfont=dict(color='#000000', size=12)),
                yaxis=dict(showgrid=False, color='#000000', automargin=True, tickfont=dict(color='#000000', size=12)),
                font=dict(family='DM Sans', size=12, color='#000000'),
            )
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar':False})

        with cb:
            rd = analytics['risk_dist']
            rcolors = {'High':'#ef4444','Medium':'#f59e0b','Low':'#10b981'}
            fig2 = go.Figure(go.Pie(
                labels=list(rd.keys()),
                values=list(rd.values()),
                hole=0.52,
                marker=dict(colors=[rcolors.get(k,'#6b7280') for k in rd.keys()],
                            line=dict(color='#fff', width=2)),
                textinfo='label+percent',
                textfont=dict(size=13, family='DM Sans'),
            ))
            fig2.update_layout(
                height=320,
                margin=dict(t=10,b=10,l=10,r=10),
                paper_bgcolor='#fff',
                annotations=[dict(text='Risk', x=0.5, y=0.5,
                    font=dict(size=16, family='DM Serif Display', color='#1e3a8a'), showarrow=False)],
                font=dict(family='DM Sans', color='#374151'),
            )
            st.plotly_chart(fig2, use_container_width=True, config={'displayModeBar':False})


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — PREDICTION HISTORY
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📋 Prediction History":
    st.markdown("""
    <div class='hero'>
        <div class='hero-title'>📋 Prediction History</div>
        <div class='hero-sub'>All past diagnoses stored in SQLite · Full-stack skill demonstration · Export to CSV</div>
    </div>""", unsafe_allow_html=True)

    df = u.get_history()
    if df.empty:
        st.info("💡 No predictions yet. Go to **🔬 Diagnose** to get started!")
    else:
        st.markdown(f"**{len(df)} prediction(s) on record**")
        st.markdown("<div style='margin-top:12px'>", unsafe_allow_html=True)
        for _, row in df.iterrows():
            rc = f"risk-{row['risk_level'].lower()}"
            sym_preview = str(row['symptoms'])[:65] + ('…' if len(str(row['symptoms'])) > 65 else '')
            st.markdown(f"""
            <div class='hrow'>
                <div style='display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px'>
                    <div>
                        <div style='font-family:"DM Serif Display",serif; font-size:1.08rem; color:#1e3a8a; margin-bottom:3px'>
                            {row['top1_disease']}
                        </div>
                        <div style='font-size:0.8rem; color:#6b7280'>
                            {row['timestamp']} &nbsp;·&nbsp; {sym_preview}
                        </div>
                    </div>
                    <div style='text-align:right; flex-shrink:0'>
                        <div style='font-weight:700; color:#1d4ed8; font-size:1rem; margin-bottom:3px'>
                            {row['top1_prob']:.1f}%
                        </div>
                        <span class='{rc}'>{row['risk_level']} Risk</span>
                    </div>
                </div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<div style='margin-top:16px'>", unsafe_allow_html=True)
        st.download_button(
            "📥 Export History (CSV)",
            df.to_csv(index=False),
            "medisense_history.csv",
            "text/csv"
        )
        st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 4 — DISEASE LIBRARY
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📚 Disease Library":
    st.markdown("""
    <div class='hero'>
        <div class='hero-title'>📚 Disease Library</div>
        <div class='hero-sub'>Comprehensive reference for all 41 diseases · Causes · Prevention · Diet · Workout · Medicines</div>
    </div>""", unsafe_allow_html=True)

    search = st.text_input(
        "Search diseases",
        placeholder="e.g. Dengue, Diabetes, Malaria, Heart attack...",
        label_visibility="collapsed"
    )
    filtered = [d for d in u.DISEASES if search.lower() in d.lower()] if search else u.DISEASES
    st.caption(f"Showing {len(filtered)} of {len(u.DISEASES)} diseases  ·  Click any disease to expand")

    for disease in filtered:
        info = u.DISEASE_INFO.get(disease, {})
        risk = u.RISK_LEVELS.get(disease, 'Medium')
        rc   = f"risk-{risk.lower()}"
        icon = '🔴' if risk=='High' else '🟡' if risk=='Medium' else '🟢'

        with st.expander(f"{icon}  {disease}", expanded=False):
            c1, c2 = st.columns([3, 1])
            with c1:
                st.markdown(f"""<div class='iblock'>
                    <div class='iblock-lbl'>Description</div>
                    <div class='iblock-val'>{info.get('description','N/A')}</div>
                </div>""", unsafe_allow_html=True)
            with c2:
                st.markdown(f"<span class='{rc}'>{risk} Risk</span><br><br>", unsafe_allow_html=True)
                st.caption(f"Recovery: {info.get('recovery_time','Varies')}")

            ca, cb = st.columns(2)
            with ca:
                for lbl, key in [('Causes','causes'),('Prevention','prevention')]:
                    st.markdown(f"""<div class='iblock'>
                        <div class='iblock-lbl'>{lbl}</div>
                        <div class='iblock-val'>{info.get(key,'N/A')}</div>
                    </div>""", unsafe_allow_html=True)
            with cb:
                st.markdown(f"""<div class='iblock'>
                    <div class='iblock-lbl'>When to See Doctor</div>
                    <div class='iblock-val'>{info.get('when_to_see_doctor','N/A')}</div>
                </div>""", unsafe_allow_html=True)
                syms = u.DISEASE_SYMPTOMS.get(disease, [])
                pills_html = "".join(f"<span class='pill pm'>{s.replace('_',' ').title()}</span>" for s in syms[:8])
                st.markdown(f"""<div class='iblock'>
                    <div class='iblock-lbl'>Common Symptoms</div>
                    <div style='margin-top:5px'>{pills_html}</div>
                </div>""", unsafe_allow_html=True)

            cm, cd, cw = st.columns(3)
            with cm:
                st.markdown("**💊 Medicines**")
                st.markdown("".join(f"<span class='pill pmed'>{m}</span>" for m in info.get('medicines',[])), unsafe_allow_html=True)
            with cd:
                st.markdown("**🥗 Diet**")
                st.markdown("".join(f"<span class='pill pd'>{d}</span>" for d in info.get('diet',[])), unsafe_allow_html=True)
            with cw:
                st.markdown("**🏃 Workout**")
                st.markdown("".join(f"<span class='pill pwk'>{w}</span>" for w in info.get('workout',[])), unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 5 — MODEL MONITORING
# ══════════════════════════════════════════════════════════════════════════════
elif page == "⚙️ Model Monitoring":
    st.markdown("""
    <div class='hero'>
        <div class='hero-title'>⚙️ Model Monitoring</div>
        <div class='hero-sub'>Model versioning · Cross-validation scores · Training configuration · Per-fold accuracy</div>
    </div>""", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    for col, (val, lbl) in zip([c1,c2,c3,c4], [
        (u.meta.get('model_version','v2.0'),             "Model Version"),
        (u.meta.get('training_date','N/A'),              "Training Date"),
        (f"{u.meta.get('cv_accuracy',0)*100:.2f}%",     "Best CV Accuracy"),
        (u.meta.get('prediction_count', u.meta.get('n_training_samples',0)), "Training Samples"),
    ]):
        with col:
            st.markdown(f"<div class='mcard'><div class='mcard-val' style='font-size:1.55rem'>{val}</div><div class='mcard-lbl'>{lbl}</div></div>", unsafe_allow_html=True)

    st.markdown("<div class='sh'>📈 Model Comparison (Cross-Validation)</div>", unsafe_allow_html=True)
    cc, ct = st.columns([3, 2])
    with cc:
        names  = list(u.cv_results.keys())
        means  = [u.cv_results[n]['cv_mean']*100 for n in names]
        stds   = [u.cv_results[n]['cv_std']*100  for n in names]
        colors = ['#1d4ed8','#06b6d4','#8b5cf6'][:len(names)]
        fig = go.Figure([go.Bar(
            name=n, x=[n], y=[m],
            error_y=dict(type='data', array=[s], visible=True, thickness=2),
            marker=dict(color=c, line=dict(width=0)),
            text=[f"{m:.2f}%"], textposition='outside',
            textfont=dict(size=12, color='#1e3a8a'),
        ) for n,m,s,c in zip(names,means,stds,colors)])
        fig.update_layout(
            height=320, showlegend=False,
            yaxis=dict(range=[88,104], title='Accuracy (%)', showgrid=True, gridcolor='#e5e7eb', color='#000000', tickfont=dict(color='#000000', size=12), title_font=dict(color='#000000')),
            xaxis=dict(showgrid=False, color='#000000', tickfont=dict(color='#000000', size=12)),
            paper_bgcolor='#fff', plot_bgcolor='#fff',
            margin=dict(t=28,b=8,l=10,r=10),
            font=dict(family='DM Sans', color='#000000'),
        )
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar':False})

    with ct:
        st.markdown("<div class='sh' style='margin-top:0'>Model Details</div>", unsafe_allow_html=True)
        for n in names:
            r    = u.cv_results[n]
            star = " ⭐" if n == u.meta.get('best_model_name') else ""
            fold_scores = ", ".join(f"{s*100:.1f}%" for s in r['scores'])
            st.markdown(f"""
            <div class='iblock'>
                <div class='iblock-lbl'>{n}{star}</div>
                <div class='iblock-val'>
                    CV Accuracy: <strong>{r['cv_mean']*100:.2f}%</strong><br>
                    Std Dev: ±{r['cv_std']*100:.2f}%<br>
                    Fold Scores: {fold_scores}
                </div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<div class='sh'>🗂️ Training Configuration</div>", unsafe_allow_html=True)
    ca, cb = st.columns(2)
    configs = [
        ('Best Model',        u.meta.get('best_model_name','N/A')),
        ('Training Samples',  f"{u.meta.get('n_training_samples',0):,}"),
        ('Diseases Covered',  u.meta.get('n_diseases',41)),
        ('Symptoms Tracked',  u.meta.get('n_symptoms',132)),
        ('CV Strategy',       '5-Fold Stratified K-Fold'),
        ('Random Seed',       '42'),
    ]
    for i, (lbl, val) in enumerate(configs):
        with (ca if i%2==0 else cb):
            st.markdown(f"""<div class='iblock'>
                <div class='iblock-lbl'>{lbl}</div>
                <div class='iblock-val' style='font-weight:700'>{val}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class='ai'>
        <strong style='color:#1d4ed8'>ℹ️ Note:</strong>
        <span style='color:#1e3a8a; font-size:0.88rem'> High CV accuracy (~99%) is achieved on a synthetic dataset.
        Real-world performance on clinical data will vary. This is transparently disclosed in the app.</span>
    </div>""", unsafe_allow_html=True)
