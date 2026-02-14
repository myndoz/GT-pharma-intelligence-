import streamlit as st
import time
from datetime import datetime
from openai import OpenAI
from streamlit_mic_recorder import mic_recorder

client = OpenAI()

st.set_page_config(
page_title="GT Pharma Intelligence",
page_icon="static/favicon.png",
layout="centered"
)

# ---------------- SESSION STATE ----------------

if "news_feed" not in st.session_state:
st.session_state.news_feed = []

if "last_scan" not in st.session_state:
st.session_state.last_scan = 0

# ---------------- UI ----------------

st.title("💊 GT Pharma Intelligence")

# ---------------- NEWS ----------------

def scan_pharma_news():
sample_news = [
f"{datetime.now().strftime('%H:%M')} - FDA approvals increasing",
f"{datetime.now().strftime('%H:%M')} - AI drug discovery growth",
f"{datetime.now().strftime('%H:%M')} - Biotech funding surge"
]
st.session_state.news_feed = sample_news

if st.button("Scan Pharma News"):
scan_pharma_news()

for item in st.session_state.news_feed:
st.write(item)

# ---------------- COMPANY ANALYSIS ----------------

company = st.text_input("Enter Company Name")

if st.button("Analyze Company"):
if company.strip() != "":
response = client.chat.completions.create(
model="gpt-4.1-mini",
messages=[{"role":"user","content":f"Give key business insights about pharma company {company}"}]
)
st.write(response.choices[0].message.content)

# ---------------- VOICE ----------------

st.subheader("🎤 Voice Ask")

audio = mic_recorder(start_prompt="Start Talking", stop_prompt="Stop")

if audio:
st.write("Voice captured successfully")
