"""
Virtual ICU - Main Application Entry Point

This is the main Streamlit application for the Virtual ICU system.
"""

import streamlit as st
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="Virtual ICU - AI-Driven Monitoring",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)


def main():
    """Main application"""
    
    # Sidebar
    st.sidebar.title("🏥 Virtual ICU")
    st.sidebar.markdown("---")
    
    # Navigation menu
    page = st.sidebar.radio(
        "Select Page",
        ["🏠 Home", "📊 Dashboard", "👁️ Monitoring", "👨‍🏫 Invigilator", "📚 Education"],
        help="Choose a page to navigate"
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info(
        "**Virtual ICU v0.1.0-alpha**\n\n"
        "Educational demonstration of AI-driven ICU monitoring.\n\n"
        "[GitHub](https://github.com/paracelsus12-crypto/virtual-icu-demo)"
    )
    
    # Route to pages
    if page == "🏠 Home":
        show_home()
    elif page == "📊 Dashboard":
        show_dashboard()
    elif page == "👁️ Monitoring":
        show_monitoring()
    elif page == "👨‍🏫 Invigilator":
        show_invigilator()
    elif page == "📚 Education":
        show_education()


def show_home():
    """Home page"""
    st.title("🏥 Virtual ICU - AI-Driven Patient Monitoring")
    
    st.markdown("""
    ### Welcome to Virtual ICU
    
    This educational platform demonstrates **AI-powered patient monitoring** in intensive care settings.
    
    #### Features
    - 🏥 **6 Clinical Scenarios** — Sepsis, Cardiac Arrest, Respiratory Failure, Hypotension, Hypoxemia, Arrhythmias
    - 🤖 **AI Predictions** — NEWS2, qSOFA, CART scoring systems
    - 📊 **Real-Time Visualization** — Interactive vital signs charts
    - 🎓 **Interactive Teaching** — Invigilator control panel for demonstrations
    - 💻 **100% Local** — No cloud, no patient data, 100% synthetic
    
    #### Quick Start
    1. **Choose a Page** from the sidebar
    2. **Dashboard** — View patient vital signs & AI predictions
    3. **Monitoring** — Real-time vital signs tracking
    4. **Invigilator** — Simulate clinical scenarios for teaching
    5. **Education** — Learn about critical care concepts
    """)
    
    # Statistics cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Clinical Scenarios", "6", "+100% synthetic")
    with col2:
        st.metric("Scoring Systems", "3", "NEWS2, qSOFA, CART")
    with col3:
        st.metric("Vital Parameters", "8+", "Real-time tracking")
    with col4:
        st.metric("Students", "∞", "Safe learning")


def show_dashboard():
    """Dashboard page"""
    st.title("📊 Patient Dashboard")
    st.info("Dashboard page placeholder - Coming in Phase 2")
    st.write("This will show real-time patient vital signs and risk scores.")


def show_monitoring():
    """Monitoring page"""
    st.title("👁️ Vital Signs Monitoring")
    st.info("Monitoring page placeholder - Coming in Phase 2")
    st.write("Real-time vital signs charts and trends.")


def show_invigilator():
    """Invigilator control panel"""
    st.title("👨‍🏫 Invigilator Control Panel")
    st.warning("Invigilator page placeholder - Coming in Phase 2")
    st.write("""
    This panel allows instructors to:
    - Select clinical scenarios
    - Simulate patient deterioration over time
    - Demonstrate model responsiveness
    - Create teachable moments
    """)


def show_education():
    """Education page"""
    st.title("📚 Educational Resources")
    st.success("Education page placeholder - Coming in Phase 2")
    st.write("""
    Learning resources about:
    - Critical care concepts
    - Clinical scoring systems
    - Emergency response protocols
    - Case studies
    """)


if __name__ == "__main__":
    main()
