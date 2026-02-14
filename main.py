from openai import OpenAI
from streamlit_mic_recorder import mic_recorder
import streamlit as st
import time
from datetime import datetime
# ---- PWA MOBILE INSTALL SUPPORT ----
import streamlit as st

st.set_page_config(
    page_title="GT Pharma Intelligence",
    page_icon="static/favicon.png",
    layout="wide"
)

st.markdown("""
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#f97316">
<link rel="apple-touch-icon" href="/static/icon-192.png">
""", unsafe_allow_html=True)

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Pharma Intelligence", layout="centered")

# ---------------- SESSION STATE ----------------
if "news_feed" not in st.session_state:
    st.session_state.news_feed = []

if "last_scan" not in st.session_state:
    st.session_state.last_scan = 0

# ---------------- UI STYLE ----------------
st.markdown("""
<style>
body { background-color:#f7faf7; }
.header {
    background: linear-gradient(90deg,#16a34a,#22c55e);
    padding:20px;
    border-radius:12px;
    color:white;
    text-align:center;
    font-size:28px;
    font-weight:700;
}
.footer {
    background:#f97316;
    padding:14px;
    border-radius:12px;
    color:white;
    text-align:center;
    margin-top:30px;
}
.card {
    background:white;
    padding:16px;
    border-radius:16px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom:12px;
}
.big-input input {
    font-size:18px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">💊 Pharma Intelligence Assistant</div>', unsafe_allow_html=True)

# ---------------- AUTO REFRESH CHECK ----------------
def should_refresh():
    return time.time() - st.session_state.last_scan > 1800

# ---------------- NEWS SCAN (MOCK) ----------------
def scan_pharma_news():
    sample_news = [
        f"{datetime.now().strftime('%H:%M')} - FDA approval activity increasing globally",
        f"{datetime.now().strftime('%H:%M')} - Biotech funding surge observed",
        f"{datetime.now().strftime('%H:%M')} - Major pharma focusing on AI drug discovery"
    ]
    st.session_state.news_feed = sample_news + st.session_state.news_feed[:10]
    st.session_state.last_scan = time.time()

# silent auto refresh when user opens app
if should_refresh():
    scan_pharma_news()

# ---------------- MANUAL SCAN BUTTON ----------------
if st.button("🔄 Scan Global Pharma News"):
    scan_pharma_news()
    st.success("Latest intelligence updated")

# ---------------- NEWS FEED ----------------
st.subheader("📡 Live Pharma Alerts")

if not st.session_state.news_feed:
    st.info("No alerts yet. Run first scan.")

for item in st.session_state.news_feed:
    st.markdown(f'<div class="card">{item}</div>', unsafe_allow_html=True)

# ---------------- CEO DISCUSSION BUILDER ----------------
st.subheader("🧠 CEO Discussion Prep")
company = st.text_input("Enter Company Name", key="company_input")

if st.button("Generate Talking Points"):
    if company.strip() == "":
        st.warning("Please enter a company name")
    else:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write(f"Strategic conversation starters for **{company.title()}**:")
        st.write("• Ask about AI adoption in R&D")
        st.write("• Discuss regulatory expansion markets")
        st.write("• Explore pipeline commercialization strategy")
        st.write("• Mention recent biotech partnerships trend")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Grand Thornton Smart Auditor Companion</div>', unsafe_allow_html=True)
# ---------------- VOICE AI ASSISTANT ----------------

st.subheader("🎤 Speak to Pharma AI")

audio = mic_recorder(start_prompt="🎙️ Start Talking", stop_prompt="🛑 Stop")

if audio:
st.info("Voice received. Processing...")

```
voice_query = "Give latest risks, opportunities and discussion ideas in pharma industry"

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": voice_query}],
    temperature=0.5
)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.write(response.choices[0].message.content)
st.markdown('</div>', unsafe_allow_html=True)
```
