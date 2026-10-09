st.markdown("""
<style>

/* Main app background */
.stApp {
    background-color: #f3f6fc;
    color: #102448;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #102448;
}

[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

/* Welcome hero section */
.hero {
    background: linear-gradient(120deg, #102448, #2457a7);
    padding: 28px;
    border-radius: 16px;
    color: #ffffff !important;
    margin-bottom: 20px;
}

.hero h1,
.hero h2,
.hero h3 {
    color: #ffffff !important;
    margin-bottom: 8px;
}

.hero p,
.hero span {
    color: #e4edff !important;
    font-size: 16px;
}

/* Information cards */
.info-card {
    background-color: #ffffff;
    color: #102448 !important;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #dce5f4;
    margin-bottom: 12px;
}

.info-card h1,
.info-card h2,
.info-card h3,
.info-card p,
.info-card span,
.info-card li {
    color: #102448 !important;
}

/* Main page text */
.stApp p,
.stApp label,
.stApp [data-testid="stMarkdownContainer"] p {
    color: #102448;
}

/* Timetable tables */
[data-testid="stTable"],
[data-testid="stDataFrame"] {
    color: #102448 !important;
}

/* Buttons */
div.stButton > button {
    border-radius: 9px;
    font-weight: 600;
}

/* Mobile screen adjustments */
@media screen and (max-width: 768px) {
    .hero {
        padding: 18px;
    }

    .hero h1 {
        font-size: 24px !important;
    }

    .hero p {
        font-size: 15px !important;
    }

    .info-card {
        padding: 14px;
    }
}

</style>
""", unsafe_allow_html=True)
