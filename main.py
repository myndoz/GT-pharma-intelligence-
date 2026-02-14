import streamlit as st
from openai import OpenAI
from streamlit_mic_recorder import mic_recorder
import time
from datetime import datetime

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="GT Pharma Intelligence",
    page_icon="static/icon-192.png",
    layout="centered"
)

# ================= PWA MOBILE SUPPORT =================
st.markdown("""
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#16a34a">
<link rel="apple-touch-icon" href="/static/icon-192.png">
""", unsafe_allow_html=True)

# ================= OPENAI CLIENT =================
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ================= SESSION STATE =================
if "news_feed" not in st.session_state:
    st.session_state.news_feed = []

if "last_scan" not in st.session_state:
    st.session_state.last_scan = 0

# ================= UI STYLE =================
st.markdown("""
<style>
body { background-color:#f4faf4; font-family: Arial, sans-serif; }

.header {
    background: linear-gradient(90deg,#16a34a,#22c55e);
    padding:18px;
    border-radius:14px;
    color:white;
    text-align:center;
    font-size:26px;
    font-weight:bold;
    margin-bottom:20px;
}

.footer {
    background:#f97316;
    padding:14px;
    border-radius:14px;
    color:white;
    text-align:center;
    margin-top:30px;
    font-size:14px;
}

.card {
    background:white;
    padding:16px;
    border-radius:16px;
    box-shadow:0px 4px 14px rgba(0,0,0,0.08);
    margin-bottom:12px;
    color:black;
    font-size:16px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">💊 GT Pharma Intelligence</div>', unsafe_allow_html=True)

# ================= NEWS FUNCTION =================
def scan_pharma_news():
    now = datetime.now().strftime("%H:%M")
    sample_news = [
        f"{now} - FDA approvals increasing globally",
        f"{now} - AI drug discovery investments rising",
        f"{now} - Pharma M&A activity accelerating"
    ]
    st.session_state.news_feed = sample_news
    st.session_state.last_scan = time.time()

# ================= NEWS SECTION =================
st.subheader("📡 Live Pharma Alerts")

if st.button("Refresh Intelligence"):
    scan_pharma_news()

if len(st.session_state.news_feed) == 0:
    st.info("No alerts yet")

for item in st.session_state.news_feed:
    st.markdown(f'<div class="card">{item}</div>', unsafe_allow_html=True)

# ================= CEO MEETING AI =================
st.subheader("🧠 CEO Meeting Intelligence")

company = st.text_input("Enter Pharma Company Name")

if st.button("Generate AI Briefing") and company.strip() != "":
    prompt = f"Prepare executive meeting talking points, risks and smart discussion ideas for the CEO of pharmaceutical company {company}"

    with st.spinner("Analyzing company intelligence..."):
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role":"user","content":prompt}],
            temperature=0.4
        )

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write(response.choices[0].message.content)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= VOICE AI =================
st.subheader("🎤 Speak with Pharma AI")

audio = mic_recorder(start_prompt="Start Talking", stop_prompt="Stop Recording")

if audio:
    voice_prompt = "Give latest risks and opportunities in pharmaceutical industry for executive discussion"

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":voice_prompt}],
        temperature=0.5
    )

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write(response.choices[0].message.content)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Grand Thornton AI Companion</div>', unsafe_allow_html=True)
