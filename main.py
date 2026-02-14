import streamlit as st
import requests

st.set_page_config(page_title="Pharma Intelligence Auditor Assistant")

st.title("💊 Pharma Intelligence & Auditor Research Assistant")

st.write("Welcome! This system will scan global pharma news and help auditors prepare for client discussions.")

# -------------------------------
# NEWS SECTION
# -------------------------------

def fetch_news():
    url = "https://newsapi.org/v2/everything?q=pharmaceutical OR pharma OR FDA OR drug industry&language=en&sortBy=publishedAt&pageSize=5&apiKey=demo"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get("articles", [])
    except:
        return []

st.header("🌍 Latest Pharma News")

if st.button("Scan Global Pharma News"):
    articles = fetch_news()
    if not articles:
        st.warning("News API will be connected later. App working correctly.")
    else:
        for a in articles:
            st.subheader(a["title"])
            st.write(a["description"])
            st.write("---")

# -------------------------------
# COMPANY RESEARCH
# -------------------------------

st.header("🧠 Auditor Smart Discussion Builder")

company = st.text_input("Enter Client Company Name")

if st.button("Generate Meeting Intelligence"):
    if company:
        st.markdown(f"""
### Strategic Talking Points for {company}

**Possible CEO Questions**
- How is the global pharma market shifting?
- What risks affect our valuation?
- Regulatory exposure areas?
- Expansion opportunities?

**Auditor Smart Opinions**
- Focus on compliance strength
- Highlight R&D positioning
- Discuss global competition
- Mention investor confidence factors

**Red Flag Areas to Check**
- Related party transactions
- Regulatory notices
- Revenue recognition
- Export dependency
""")
    else:
        st.warning("Please enter company name")
