from openai import OpenAI
from streamlit_mic_recorder import mic_recorder
import streamlit as st
import time
from datetime import datetime

# ---------------- OPENAI CLIENT ----------------

client = OpenAI()

# ---------------- PAGE CONFIG (ONLY ONCE) ----------------

st.set_page_config(
page_title="GT Pharma Intelligence",
page_icon="static/favicon.png",
layout="centered"
)

# ---------------- PWA MOBILE SUPPORT ----------------

st.markdown("""

<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#f97316">
<link rel="apple-touch-icon" href="/static/icon-192.png">
""", unsafe_allow_html=True)

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
    color:black;
    padding:16px;
    border-radius:16px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom:12px;
}
</style>

""", unsafe_allow_html=True)

st.markdown('<div class="header">💊 GT Pharma Intelligence</div>', unsafe_allow_html=True)

# ---------------- AUTO REFRESH ----------------

def should_refresh():
return time.time() - st.session_state.last_scan > 1800

def scan_pharma_news():
sample_news = [
f"{datetime.now().strftime('%H:%M')} - FDA approval activity increasing globally",
f"{datetime.now().strftime('%H:%M')} - Biotech funding surge observed",
f"{datetime.now().strftime('%H:%M')} - AI driven drug discovery expanding"
]
st.session_state.news_feed = sample_news + st.session_state.news_feed[:10]
st.session_state.last_scan = time.time()

if should_refresh():
scan_pharma_news()

# ---------------- NEWS SECTION ----------------

st.subheader("📡 Live Pharma Alerts")

if st.button("🔄 Scan Global Pharma News"):
scan_pharma_news()
st.success("Latest intelligence updated")

if not st.session_state.news_feed:
st.info("No alerts yet")

for item in st.session_state.news_feed:
st.markdown(f'<div class="card">{item}</div>', unsafe_allow_html=True)

# ---------------- CEO DISCUSSION BUILDER ----------------

st.subheader("🧠 CEO Discussion Prep")
company = st.text_input("Enter Company Name")

if st.button("Generate Talking Points"):
if company.strip() == "":
st.warning("Please enter a company name")
else:
prompt = f"Prepare CEO meeting talking points, risks, opportunities and smart discussion ideas for pharma company {company}"

```
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write(response.choices[0].message.content)
    st.markdown('</div>', unsafe_allow_html=True)
```

# ---------------- VOICE AI ASSISTANT ----------------

st.subheader("🎤 Speak to Pharma AI")

audio = mic_recorder(start_prompt="🎙️ Start Talking", stop_prompt="🛑 Stop")

if audio:
st.info("Voice received. Generating intelligence...")

```
voice_prompt = "Give latest pharma industry risks and opportunities for a business discussion"

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": voice_prompt}],
    temperature=0.5
)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.write(response.choices[0].message.content)
st.markdown('</div>', unsafe_allow_html=True)
```

st.markdown('<div class="footer">Grand Thornton Smart Auditor Companion</div>', unsafe_allow_html=True)
