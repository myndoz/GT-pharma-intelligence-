# ========================= IMPORTS =========================
import streamlit as st
from openai import OpenAI
from streamlit_mic_recorder import mic_recorder
import time
from datetime import datetime
import pytz

# ========================= PAGE CONFIG =========================
st.set_page_config(
    page_title="GT Pharma Intelligence",
    page_icon="static/icon-192.png",
    layout="centered"
)

# ========================= PWA MOBILE SUPPORT =========================
st.markdown("""
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#16a34a">
<link rel="apple-touch-icon" href="/static/icon-192.png">
""", unsafe_allow_html=True)

# ========================= OPENAI CLIENT =========================
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ========================= SESSION STATE =========================
if "news_feed" not in st.session_state:
    st.session_state.news_feed = []

if "last_scan" not in st.session_state:
    st.session_state.last_scan = 0

# ========================= UI STYLE =========================
st.markdown("""
<style>
body { background-color:#f4faf4; }

.header {
    background: linear-gradient(90deg,#16a34a,#22c55e);
    padding:18px;
    border-radius:14px;
    color:white;
    text-align:center;
    font-size:26px;
    font-weight:700;
    margin-bottom:20px;
}

.footer {
    background:#f97316;
    padding:14px;
    border-radius:14px;
    color:white;
    text-align:center;
    margin-top:30px;
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

.stButton>button {
    border-radius:18px;
    height:50px;
    width:100%;
    font-weight:bold;
    font-size:16px;
    background: linear-gradient(90deg,#16a34a,#22c55e);
    color:white;
    border:none;
}

.stTextInput>div>div>input {
    border-radius:16px;
    padding:14px;
    font-size:16px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">💊 GT Pharma Intelligence</div>', unsafe_allow_html=True)
import feedparser
import pytz

def should_refresh():
    return time.time() - st.session_state.last_scan > 1800

def scan_pharma_news():

    feeds = [
        "https://www.fiercepharma.com/rss/xml",
        "https://www.biopharmadive.com/feeds/news/",
        "https://www.fda.gov/about-fda/contact-fda/stay-informed/rss-feeds/biologics/rss.xml"
    ]

    ist = pytz.timezone("Asia/Kolkata")
    collected_news = []

    for url in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            time_now = datetime.now(ist).strftime("%H:%M IST")
            collected_news.append(f"{time_now} — {entry.title}")

    st.session_state.news_feed = collected_news[:15]
    st.session_state.last_scan = time.time()

# ========================= NEWS SECTION =========================
st.subheader("📡 Live Pharma Alerts")

if st.button("🔄 Refresh Intelligence"):
    scan_pharma_news()
    st.success("Latest intelligence updated")

if not st.session_state.news_feed:
    st.info("No alerts yet")

for item in st.session_state.news_feed:
    st.markdown(f'<div class="card">{item}</div>', unsafe_allow_html=True)

# ========================= CEO DISCUSSION BUILDER =========================
st.subheader("🧠 CEO Meeting Intelligence")

company = st.text_input("Enter Pharma Company Name")

if st.button("Generate AI Briefing"):

    if company.strip() == "":
        st.warning("Please enter company name")

    else:
        prompt = f"""
You are a strategy consultant preparing for a CEO meeting with {company}.

Provide:
• Latest industry trends relevant to them
• Business risks they face
• Smart discussion topics
• One impressive question to ask CEO
"""

        with st.spinner("Analyzing company intelligence..."):
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4
            )

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write(response.choices[0].message.content)
        st.markdown('</div>', unsafe_allow_html=True)

# ========================= VOICE AI =========================
st.subheader("🎤 Speak with Pharma AI")

audio = mic_recorder(start_prompt="Start Talking", stop_prompt="Stop Recording")

if audio is not None:
    st.info("Voice received. Generating insights...")

    voice_prompt = """
Provide latest pharma industry risks, opportunities and talking points
for consultants meeting pharma executives.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": voice_prompt}],
        temperature=0.5
    )

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write(response.choices[0].message.content)
    st.markdown('</div>', unsafe_allow_html=True)

# ========================= FOOTER =========================
st.markdown('<div class="footer">Grand Thornton AI Companion</div>', unsafe_allow_html=True)
