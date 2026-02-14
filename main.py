import streamlit as st
from openai import OpenAI

# Load API key securely
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Pharma Intelligence Auditor", layout="wide")

# Title
st.markdown("""
<h1 style='text-align:center;color:white;'>🧠 Pharma Intelligence Auditor</h1>
<h4 style='text-align:center;color:#dddddd;'>Strategic AI Assistant for Client Discussions</h4>
""", unsafe_allow_html=True)

st.divider()

company = st.text_input("Enter Pharma Company Name")

if st.button("Generate Strategic Intelligence"):

    prompt = f"""
You are a Big4 audit partner and pharma industry specialist.

Prepare a strategic client discussion brief for {company}.

Include:
- Business overview
- Risk areas
- Compliance red flags
- CEO questions to ask
- Audit focus areas
- Investor perception
- Competitor threats

Make it boardroom ready, crisp and intelligent.
"""

    with st.spinner("Analyzing company intelligence..."):
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )

    st.subheader("📊 Strategic Discussion Brief")
    st.write(response.choices[0].message.content)
