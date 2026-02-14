# Pharma Intelligence Auditor - Advanced Version
# Mobile-first UI + Auto news refresh + CEO brief builder

import streamlit as st
import requests
import feedparser
from datetime import datetime
from openai import OpenAI

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Pharma Intelligence Auditor", layout="centered")

# Auto refresh every 30 minutes (simulate notifications)
st.experimental_rerun
from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=1800000, key="news_refresh")

# OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ---------------- UI STYLE ----------------
st.markdown("""
<style>
body {background: #f6fff9;}
.main-title {font-size:32px;font-weight:700;color:white;padding:20px;text-align:center;}
.header {background: linear-gradient(90deg,#ff7a18,#ffb347);border-radius:15px;margin-bottom:15px;}
.card {background:white;border-radius:18px;padding:18px;margin:12px 0;box-shadow:0 4px 12px rgba(0,0,0,0.08);} 
.button-primary button {background:#00a86b;color:white;font-size:18px;border-radius:12px;padding:10px 18px;}
.footer {position:fixed;bottom:0;width:100%;background:#ff7a18;color:white;text-align:center;padding:10px;font-weight:600;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header"><div class="main-title">Pharma Intelligence Auditor</div></div>', unsafe_allow_html=True)

# ---------------- NEWS FEED ----------------
def fetch_pharma_news():
    feed = feedparser.parse("https://news.google.com/rss/search?q=pharmaceutical+industry&hl=en-IN&gl=IN&ceid=IN:en")
    articles = []
    for entry in feed.entries[:10]:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        })
    return articles

st.markdown("### 🔔 Live Pharma Alerts")
news = fetch_pharma_news()

for item in news:
    st.markdown(f'<div class="card">📢 <b>{item["title"]}</b><br><a href="{item["link"]}">Read more</a><br><small>{item["published"]}</small></div>', unsafe_allow_html=True)

# ---------------- COMPANY INTELLIGENCE ----------------
st.markdown("### 🧠 CEO Meeting Intelligence")
company = st.text_input("Enter Pharma Company Name")

if st.button("Generate CEO Brief"):
    if company:
        prompt = f"""
You are a Big4 consulting partner preparing for a CEO meeting.
Company: {company}
Provide:
1) Latest market developments
2) Risk areas
3) Strategic questions to ask CEO
4) Smart opinions to impress leadership
"""
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        st.markdown(f'<div class="card">{response.choices[0].message.content}</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown('<div class="footer">Grand Thornton Intelligent Assistant</div>', unsafe_allow_html=True)
