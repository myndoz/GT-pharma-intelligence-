import streamlit as st

st.set_page_config(
    page_title="Pharma Auditor AI",
    page_icon="💊",
    layout="centered"
)

# Mobile CSS
st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
    padding-bottom: 6rem;
}
.stButton>button {
    width:100%;
    height:60px;
    border-radius:18px;
    font-size:18px;
    font-weight:600;
}
.card {
    padding:18px;
    border-radius:18px;
    background:#f7f9fc;
    margin-bottom:12px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
}
.big-title {
    font-size:28px;
    font-weight:800;
    text-align:center;
    margin-bottom:10px;
}
.subtitle {
    text-align:center;
    color:gray;
    margin-bottom:25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>💊 Pharma Auditor AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Grand Thornton Intelligent Assistant</div>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs([
    "📰 News Alerts",
    "🚨 Fraud Radar",
    "🏢 Company Research",
    "🎯 CEO Talking Points"
])

with tab1:
    st.markdown("### Global Pharma Intelligence")
    if st.button("Scan Worldwide Pharma News"):
        st.info("AI will scan global industry updates here")

with tab2:
    st.markdown("### Risk & Fraud Detection")
    if st.button("Check Fraud Signals"):
        st.warning("AI will detect compliance & fraud alerts")

with tab3:
    company = st.text_input("Enter Client Company Name")
    if st.button("Deep Research Company"):
        st.success("AI will prepare auditor briefing")

with tab4:
    topic = st.text_input("Enter discussion topic (valuation, risk, expansion...)")
    if st.button("Generate CEO Talking Points"):
        st.success("AI will generate strategic discussion guidance")
