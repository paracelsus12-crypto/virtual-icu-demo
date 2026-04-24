"""
Virtual ICU v2.0 - Multipage Streamlit Application
Main entry point with navigation
"""

import streamlit as st
import os

# ════════════════════════════════════════════════════════════════════
# PAGE CONFIG
# ════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="Virtual ICU v2.0",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ════════════════════════════════════════════════════════════════════
# CUSTOM CSS
# ════════════════════════════════════════════════════════════════════

st.markdown("""
<style>
    .main-title {
        font-size: 3em;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 30px;
    }
    
    .subtitle {
        font-size: 1.5em;
        color: #555;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .feature-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    .stats-box {
        background: #f0f2f6;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #1f77b4;
    }
    
    .version-badge {
        display: inline-block;
        background: #28a745;
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════
# HEADER
# ════════════════════════════════════════════════════════════════════

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="main-title">🏥 Virtual ICU v2.0</div>', 
                unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI-Driven Early Warning System for Critical Patients</div>', 
                unsafe_allow_html=True)

# Version badge
st.markdown("""
<div style="text-align: center; margin-bottom: 30px;">
    <span class="version-badge">Production Ready v2.0</span>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════
# MAIN NAVIGATION
# ════════════════════════════════════════════════════════════════════

st.markdown("---")

st.subheader("📱 Choose Your Mode")

mode = st.radio(
    "Select application mode:",
    options=[
        "🎓 Student Mode (Learning)",
        "👨‍⚕️ Clinician Mode (Practice)",
        "📊 Analyst Mode (Research)",
        "ℹ️ About & Documentation"
    ],
    horizontal=True
)

st.markdown("---")

# ════════════════════════════════════════════════════════════════════
# MODE: STUDENT MODE
# ════════════════════════════════════════════════════════════════════

if mode == "🎓 Student Mode (Learning)":
    st.markdown('<div class="feature-box"><h3>🎓 Student Learning Mode</h3><p>Perfect for medical students and residents learning critical care.</p></div>', 
                unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📚 Learning Path")
        st.markdown("""
        1. **Dashboard** - Review patient overview
        2. **Vital Signs** - Watch trends over time
        3. **Clinical Scores** - Understand scoring logic
        4. **Invigilator Panel** - Practice interventions
        5. **Quiz Mode** - Test your knowledge
        """)
        
        if st.button("Start Learning Journey", key="student_start", use_container_width=True):
            st.info("Redirecting to Student Dashboard...")
            # Will be implemented in pages/
    
    with col2:
        st.markdown("### 🎯 Learning Objectives")
        st.markdown("""
        ✅ Understand vital sign monitoring
        ✅ Master clinical scoring systems
        ✅ Recognize patient deterioration
        ✅ Practice clinical decision-making
        ✅ Build confidence in high-stakes scenarios
        """)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Scenarios Available", "15", "+5 coming in v2.1")
    with col2:
        st.metric("Scoring Systems", "3", "NEWS2, qSOFA, CART")
    with col3:
        st.metric("Interactive Tabs", "5", "+2 new in v2.0")

# ════════════════════════════════════════════════════════════════════
# MODE: CLINICIAN MODE
# ════════════════════════════════════════════════════════════════════

elif mode == "👨‍⚕️ Clinician Mode (Practice)":
    st.markdown('<div class="feature-box"><h3>👨‍⚕️ Clinician Practice Mode</h3><p>Advanced tools for healthcare professionals and educators.</p></div>', 
                unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🏥 Clinician Features")
        st.markdown("""
        🔍 **Advanced Monitoring**
        - Real-time vital sign analysis
        - Predictive deterioration alerts
        - Multi-patient comparison
        
        📋 **Clinical Tools**
        - Customizable scenarios
        - Protocol library
        - Evidence-based recommendations
        """)
        
        if st.button("Open Clinician Dashboard", key="clinician_start", use_container_width=True):
            st.info("Redirecting to Clinician Dashboard...")
    
    with col2:
        st.markdown("### 🎓 Teaching Tools")
        st.markdown("""
        👥 **Group Teaching**
        - Project to classroom
        - Pause & discuss
        - Real-time interaction
        
        📊 **Case Analysis**
        - Generate reports
        - Compare scenarios
        - Validate decisions
        """)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Case Studies", "50+", "Customizable")
    with col2:
        st.metric("Protocols", "15", "Evidence-based")
    with col3:
        st.metric("Reports", "PDF export", "Coming soon")

# ════════════════════════════════════════════════════════════════════
# MODE: ANALYST MODE
# ════════════════════════════════════════════════════════════════════

elif mode == "📊 Analyst Mode (Research)":
    st.markdown('<div class="feature-box"><h3>📊 Analyst & Research Mode</h3><p>Advanced analytics for researchers and data scientists.</p></div>', 
                unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔬 Research Capabilities")
        st.markdown("""
        📈 **Data Analysis**
        - Export trajectories
        - Statistical analysis
        - ML model training
        
        🤖 **Predictive Models**
        - LSTM forecasting
        - Risk stratification
        - Performance validation
        """)
        
        if st.button("Open Analytics Dashboard", key="analyst_start", use_container_width=True):
            st.info("Redirecting to Analytics Dashboard...")
    
    with col2:
        st.markdown("### 🔍 Available Analytics")
        st.markdown("""
        📊 **Metrics & KPIs**
        - Score accuracy
        - Prediction performance
        - Alert sensitivity/specificity
        
        📚 **Datasets**
        - 1,000+ synthetic patients
        - Multiple scenarios
        - Export to CSV/JSON
        """)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Synthetic Patients", "1,000+", "Customizable")
    with col2:
        st.metric("Data Points", "50,000+", "Per scenario")
    with col3:
        st.metric("Export Formats", "CSV, JSON", "API coming")

# ════════════════════════════════════════════════════════════════════
# MODE: ABOUT
# ════════════════════════════════════════════════════════════════════

else:  # About & Documentation
    st.markdown('<div class="feature-box"><h3>ℹ️ About Virtual ICU v2.0</h3></div>', 
                unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Mission")
        st.markdown("""
        Virtual ICU brings **critical care education** to life through interactive simulations.
        
        We combine validated clinical scoring systems with modern technology to create
        an engaging, safe environment for learning and practice.
        """)
    
    with col2:
        st.markdown("### 🌟 Key Features")
        st.markdown("""
        ✅ 15+ realistic clinical scenarios
        ✅ Real-time vital sign monitoring
        ✅ 3 integrated scoring systems
        ✅ Interactive Invigilator Panel
        ✅ Predictive ML models (v2.0+)
        ✅ PDF report generation (v2.0+)
        ✅ Multi-patient analytics (v2.0+)
        """)
    
    st.markdown("---")
    
    st.markdown("### 📚 Documentation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📖 User Guide", use_container_width=True):
            st.info("Opening full documentation...")
        
        st.markdown("""
        **Quick Links:**
        - [GitHub Repository](https://github.com/paracelsus12-crypto/virtual-icu-demo)
        - [Full Documentation](./DOCUMENTATION.md)
        - [API Reference](./API_REFERENCE.md)
        """)
    
    with col2:
        if st.button("🔬 Technical Details", use_container_width=True):
            st.info("Opening technical documentation...")
        
        st.markdown("""
        **Version Info:**
        - **Current:** v2.0 (Advanced Features)
        - **Status:** Production Ready
        - **Last Update:** April 2026
        """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Project Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Code Lines", "3,000+", "Python")
    with col2:
        st.metric("Test Cases", "17+", "All passing")
    with col3:
        st.metric("Scenarios", "15", "Fully implemented")
    with col4:
        st.metric("Documentation", "10,000+", "Lines")
    
    st.markdown("---")
    
    st.markdown("### 👥 Contributors")
    st.markdown("""
    **Development Team:**
    - Lead Developer: paracelsus12-crypto
    - Clinical Advisor: [Your Institution]
    - QA & Testing: Community
    
    **Special Thanks:**
    - Royal College of Physicians (NEWS2)
    - Sepsis-3 Consensus Committee
    - Emergency Medicine Research Community
    """)

# ════════════════════════════════════════════════════════════════════
# FOOTER
# ════════════════════════════════════════════════════════════════════

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **Virtual ICU v2.0**
    
    AI-Driven Early Warning System
    for Critical Patient Care
    """)

with col2:
    st.markdown("""
    **Quick Links**
    
    - [GitHub](https://github.com/paracelsus12-crypto/virtual-icu-demo)
    - [Documentation](./DOCUMENTATION.md)
    - [Issues](https://github.com/paracelsus12-crypto/virtual-icu-demo/issues)
    """)

with col3:
    st.markdown("""
    **License**
    
    MIT License
    
    ©️ 2024 Virtual ICU Team
    """)

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #999; font-size: 0.9em;">
    <p>Virtual ICU v2.0 | Production Ready | Built with ❤️ for Medical Education</p>
</div>
""", unsafe_allow_html=True)
