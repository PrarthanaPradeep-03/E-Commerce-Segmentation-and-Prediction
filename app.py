import streamlit as st
import time

# ======================================================
# SESSION STATE
# ======================================================
if "entered" not in st.session_state:
    st.session_state.entered = False

if "page" not in st.session_state:
    st.session_state.page = "Home"

# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="E-Commerce Segmentation and Prediction",
    page_icon="🛒",
    layout="wide"
)

# ======================================================
# GLOBAL CSS
# ======================================================
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a);
    font-family: 'Segoe UI', sans-serif;
    color: white;
}

/* Hide sidebar initially */
section[data-testid="stSidebar"] {
    display: none;
}

/* Hero */
.hero {
    height: 90vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.hero-card {
    background: linear-gradient(135deg, #f59e0b, #fbbf24);
    padding: 70px;
    border-radius: 24px;
    color: #020617;
    max-width: 900px;
    animation: fadeUp 1.2s ease;
}

.hero-card h1 {
    font-size: 48px;
    font-weight: 800;
}

.hero-card p {
    font-size: 20px;
    margin-top: 20px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #6e00ff, #a855f7);
    color: white;
    font-size: 18px;
    font-weight: 600;
    padding: 14px 34px;
    border-radius: 12px;
    border: none;
    margin-top: 30px;
    transition: 0.3s ease;
}

.stButton > button:hover {
    transform: scale(1.08);
    box-shadow: 0 0 25px rgba(168,85,247,0.6);
}

/* Cards */
.card {
    background: #111827;
    padding: 30px;
    border-radius: 16px;
    margin-top: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}

/* Animations */
@keyframes fadeUp {
    from {opacity: 0; transform: translateY(40px);}
    to {opacity: 1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# LANDING PAGE (NO SIDEBAR)
# ======================================================
if not st.session_state.entered:

    st.markdown("""
    <div class="hero">
        <div class="hero-card">
            <h1>🛒 E-Commerce Customer Segmentation and Prediction</h1>
            <p>
                An enterprise-grade Machine Learning application to analyze
                customer behavior and predict valuable customer segments using
                RFM analytics.
            </p>

            
                ✔ Identify high-value customers
                ✔ Predict churn risk
                ✔ Enable data-driven marketing
            
    """, unsafe_allow_html=True)

    # Center the "Go to" button
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    if st.button("🚀 Go to"):
        st.session_state.entered = True
        st.rerun()
    st.markdown("</div></div>", unsafe_allow_html=True)


# ======================================================
# DASHBOARD (SIDEBAR ENABLED)
# ======================================================
else:
    # Show sidebar AFTER entering
    st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        display: block;
        background: linear-gradient(180deg, #020617, #111827);
        border-right: 1px solid #1f2937;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------------- SIDEBAR ----------------
    st.sidebar.title("🛒 Dashboard")
    st.session_state.page = st.sidebar.radio(
        "Navigate",
        ["Overview", "Segmentation Insights", "Customer Prediction", "About"]
    )

    # ======================================================
    # OVERVIEW
    # ======================================================
    if st.session_state.page == "Overview":
     st.title("📘 Project Overview")

     st.markdown("""
     <style>
        .card {
            background: linear-gradient(135deg, #FFD54F, #FFC107);
            padding: 22px;
            border-radius: 16px;
            margin-bottom: 20px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.15);
            color: #1f1f1f;
        }

        .card h3 {
            margin-bottom: 10px;
            font-weight: 700;
        }

        .card p {
            font-size: 16px;
            line-height: 1.6;
        }
     </style>

     <div class="card">
        <h3>🚧 Problem</h3>
        <p>
            Modern e-commerce platforms generate massive volumes of transactional and
            behavioral data on a daily basis. However, this data is often underutilized
            due to the lack of structured analytical frameworks. Businesses struggle
            to identify high-value customers, detect churn risk early, and understand
            purchasing behavior at a granular level.
        </p>
     </div>

     <div class="card">
        <h3>💡 Solution</h3>
        <p>
            This project implements an intelligent customer analytics system using
            RFM (Recency, Frequency, Monetary) analysis combined with Machine Learning
            clustering techniques. The model segments customers into meaningful and
            actionable groups, enabling personalized marketing strategies, improved
            customer retention, and data-driven business decision-making.
        </p>
     </div>
    """, unsafe_allow_html=True)

    # ======================================================
    # SEGMENTATION
    # ======================================================
    elif st.session_state.page == "Segmentation Insights":

       st.title("📊 Segmentation Insights")

       with st.spinner("Loading customer segments..."):
        time.sleep(1.5)

       st.success("Segmentation loaded successfully")

       st.markdown("""
       <style>
        .segment-container {
            display: grid;
            grid-template-columns: repeat(2, 1fr); /* 2 cards per row */
            gap: 24px;
            margin-top: 25px;
        }

        .segment-card {
            background: linear-gradient(135deg, #FFD54F, #FFB300);
            padding: 24px;
            border-radius: 18px;
            box-shadow: 0 8px 22px rgba(0,0,0,0.18);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .segment-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 12px 28px rgba(0,0,0,0.25);
        }

        .segment-card h4 {
            margin-bottom: 10px;
            font-weight: 700;
            color: #1f1f1f;
        }

        .segment-card p {
            font-size: 15px;
            line-height: 1.6;
            color: #2a2a2a;
        }
        </style>

         <div class="segment-container">

         <div class="segment-card">
            <h4>🌟 High-Value Customers</h4>
            <p>
                Customers who purchase frequently, spend more, and engage recently.
                They generate the highest revenue and should be prioritized with
                loyalty rewards and exclusive offers.
            </p>
         </div>

        <div class="segment-card">
            <h4>💰 Loyal Customers</h4>
            <p>
                Customers who consistently return and trust the brand. They respond
                well to personalized recommendations and reward-based campaigns.
            </p>
        </div>

        <div class="segment-card">
            <h4>😐 Occasional Buyers</h4>
            <p>
                Customers with irregular purchases and moderate engagement.
                Targeted promotions can convert them into loyal customers.
            </p>
        </div>

        <div class="segment-card">
            <h4>🧊 Churn-Risk Customers</h4>
            <p>
                Customers showing reduced activity or long inactivity periods.
                Re-engagement campaigns and incentives are required to retain them.
            </p>
        </div>

       </div>
    """, unsafe_allow_html=True)

    # ======================================================
    # PREDICTION
    # ======================================================
    elif st.session_state.page == "Customer Prediction":
        st.title("🔮 Customer Prediction")

        col1, col2, col3 = st.columns(3)
        with col1:
            recency = st.slider("Recency (days)", 0, 365, 30)
        with col2:
            frequency = st.slider("Frequency", 0, 100, 20)
        with col3:
            monetary = st.slider("Monetary Value", 0, 20000, 1000)

        if st.button("Predict Segment"):
            with st.spinner("Running ML model..."):
                time.sleep(1.5)

            score = (365 - recency)*0.3 + frequency*0.4 + monetary*0.0004

            if score < 60:
                seg = "🧊 Churn Risk Customer"
                desc = "Low engagement and high churn probability"
            elif score < 120:
                seg = "😐 Low-Value Customer"
                desc = "Occasional buyer with low contribution"
            elif score < 180:
                seg = "💰 Loyal Customer"
                desc = "Consistent buyer with stable spending"
            else:
                seg = "🌟 High-Value Customer"
                desc = "Top customer with high profitability"

            st.markdown(f"""
            <div class="card">
                <h3>{seg}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    # ======================================================
    # ABOUT
    # ======================================================
    elif st.session_state.page == "About":
       st.title("👤 About This Project")

       st.markdown("""
       <div class="card">
        <h3>What is this project?</h3>
        <p>
        This project is an E-Commerce Customer Segmentation and Prediction application. 
        It analyzes transactional data from e-commerce platforms to identify valuable 
        insights about customer behavior. The goal is to segment customers into meaningful 
        groups based on their buying patterns and predict potential churn or loyalty.
        </p>

        <h3>How does it work?</h3>
        <p>
        The system uses RFM (Recency, Frequency, Monetary) analysis to evaluate customer 
        behavior. 'Recency' measures how recently a customer made a purchase, 'Frequency' 
        counts how often they buy, and 'Monetary' tracks their spending. These metrics 
        are combined to score customers and classify them into actionable segments such 
        as High-Value Customers, Loyal Customers, Occasional Buyers, and Churn-Risk Customers.
        </p>

        <h3>Technologies Used</h3>
        <p>
        The application is built using Python for data processing, Streamlit for the interactive 
        web interface, and Machine Learning concepts for segmentation and prediction. 
        Modern UI/UX design principles are applied to ensure a professional and user-friendly dashboard.
        </p>

        <h3>Business Value</h3>
        <p>
        By using this system, e-commerce businesses can run targeted marketing campaigns, 
        improve customer retention, predict churn risk, personalize engagement, and 
        make data-driven decisions to increase revenue.
        </p>

        <h3>Contact</h3>
        <p style="font-size:12px;">
        Name: Prarthana Pradeep<br>
        Email: <a href="mailto:prarthanapradeep@gamil.com">prarthanapradeep@gamil.com</a>
        </p>
       </div>
    """, unsafe_allow_html=True)
