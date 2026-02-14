import streamlit as st

st.set_page_config(
    page_title="Pharma Intelligence",
    page_icon="💊",
    layout="centered"
)

# -------- THEME ----------
st.markdown("""
<style>

/* App Background */
.stApp {
    background: linear-gradient(180deg, #1a0128 0%, #2d014d 40%, #ff6a00 140%);
    color: white;
}

/* Remove top spacing */
.block-container {
    padding-top: 1rem;
    padding-bottom: 5rem;
}

/* Header Title */
.title {
    font-size: 40px;
    font-weight: 800;
    text-align: center;
    margin-top: 10px;
    margin-bottom: 0px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    opacity: 0.85;
    margin-bottom: 30px;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    font-size:18px;
    font-weight:600;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
    margin-bottom:18px;
    backdrop-filter: blur(10px);
}

/* Buttons */
.stButton>button {
    width:100%;
    height:65px;
    border-radius:18px;
    border:none;
    font-size:20px;
    font-weight:700;
    background: linear-gradient(90deg,#ff7a18,#ffb347);
    color:white;
}

/* Inputs */
.stTextInput>div>div>input {
    height:60px;
    border-radius:15px;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)


# HEADER
st.markdown("<div class='title'>💊 Pharma Intelligence Auditor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Strategic AI Assistant for Client Discussions</div>", unsafe_allow_html=True)


# TABS
tab1, tab2, tab3, tab4 = st.tabs([
    "📰 Industry Alerts",
    "🚨 Risk Radar",
    "🏢 Company Intel",
    "🎯 Boardroom Prep"
])


# -------- TAB 1 ----------
with tab1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Global Pharma Monitoring")
    if st.button("Scan Worldwide Pharma Developments"):
        st.info("AI industry monitoring will appear here")
    st.markdown("</div>", unsafe_allow_html=True)


# -------- TAB 2 ----------
with tab2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Fraud & Compliance Signals")
    if st.button("Detect Regulatory & Fraud Risks"):
        st.warning("Risk alerts will appear here")
    st.markdown("</div>", unsafe_allow_html=True)


# -------- TAB 3 ----------
with tab3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Client Company Research")

    company = st.text_input("Enter Client Company Name")

    if st.button("Prepare Auditor Briefing"):
        st.success("Deep research analysis will appear here")

    st.markdown("</div>", unsafe_allow_html=True)


# -------- TAB 4 ----------
with tab4:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("CEO Discussion Strategy")

    topic = st.text_input("Enter discussion topic (valuation, risk, expansion...)")

    if st.button("Generate Strategic Talking Points"):
        st.success("Boardroom discussion guidance will appear here")

    st.markdown("</div>", unsafe_allow_html=True)
