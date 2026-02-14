import streamlit as st
from openai import OpenAI
import time
from datetime import datetime

# ---------- CONFIG ----------

st.set_page_config(page_title="GT Pharma Intelligence", layout="centered", page_icon="static/favicon.png")

# Load API key from Streamlit secrets

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ---------- UI STYLE ----------

st.markdown("""

<style>
html, body, [data-testid="stAppViewContainer"] {
    background:#f4fff6;
    color:black !important;
}
.header {
    background: linear-gradient(90deg,#16a34a,#22c55e);
    padding:22px;
    border-radius:18px;
    color:white;
    text-align:center;
    font-size:28px;
    font-weight:700;
    margin-bottom:20px;
}
.card {
    background:white;
    padding:18px;
    border-radius:18px;
    box-shadow:0px 4px 14px rgba(0,0,0,0.08);
    margin-bottom:14px;
    color:black !important;
}
.footer {
    background:#f97316;
    padding:16px;
    border-radius:18px;
    color:white;
    text-align:center;
    margin-top:35px;
}
</style>

""", unsafe_allow_html=True)

st.markdown('<div class="header">💊 GT Pharma Intelligence</div>', unsafe_allow_html=True)

# ---------- COMPANY RESEARCH ----------

st.subheader("🧠 CEO Meeting Intelligence")

company = st.text_input("Enter Company Name")

if st.button("Generate Strategic Briefing"):
if company.strip() == "":
st.warning("Please enter company name")
else:
with st.spinner("Analyzing global pharma intelligence..."):

```
        prompt = f"""
```

You are a senior Big4 consulting partner preparing a client meeting.

Company: {company}

Prepare a sharp executive briefing including:

1. Latest global pharma trends affecting them
2. Possible CEO concerns
3. Intelligent discussion questions
4. Audit & risk red flags
5. What valuation factors matter now
6. How AI impacts their future

Write concise professional talking points.
"""

```
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role":"user","content":prompt}],
            temperature=0.4
        )

        result = response.choices[0].message.content

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(result)
        st.markdown('</div>', unsafe_allow_html=True)
```

# ---------- GENERAL AI ASSISTANT ----------

st.subheader("💬 Ask Pharma AI Anything")

query = st.text_input("Ask about any pharma company, regulation, fraud risk, valuation, industry trend...")

if st.button("Ask AI"):
if query.strip():
with st.spinner("Thinking..."):
response = client.chat.completions.create(
model="gpt-4.1-mini",
messages=[{"role":"user","content":query}],
temperature=0.5
)

```
        answer = response.choices[0].message.content
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write(answer)
        st.markdown('</div>', unsafe_allow_html=True)
```

st.markdown('<div class="footer">Grand Thornton Smart Auditor Companion</div>', unsafe_allow_html=True)
