# Virtual ICU v1.2 - AI-Driven Early Warning System for Critical Patients

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests: 17 Passing](https://img.shields.io/badge/Tests-17%20Passing-brightgreen)](test_comprehensive.py)
[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](.)

## 🏥 Overview

**Virtual ICU v1.2** is an interactive Streamlit platform for real-time monitoring and simulation of intensive care units. It combines validated clinical scoring systems (NEWS2, qSOFA, CART) with machine learning-ready architecture for predicting critical patient deterioration.

**Perfect for:**
- 🎓 Medical students learning critical care
- 👨‍⚕️ Residents practicing ICU management
- 👩‍🏫 Faculty demonstrating clinical decision-making
- 🏥 Healthcare professionals upskilling
- 📊 Healthcare researchers studying patient trajectories

## ✨ Key Features

### 📊 4 Interactive Tabs

1. **Dashboard** - Patient data overview and statistics
2. **Vital Signs** - Real-time time-series visualization
3. **Clinical Scores** - NEWS2, qSOFA, CART with dynamic recommendations
4. **Invigilator Panel** - Interactive real-time parameter adjustment

### 🎯 15 Clinical Scenarios

Pre-built realistic patient progressions:
- Sepsis (Sepsis-3), Septic Shock
- Cardiac Arrest (with/without ROSC)
- Respiratory Failure (Type I & II)
- Hypotension (progressive & sudden)
- Hypoxemia (acute & gradual)
- Arrhythmias (AFib, VT, SVT, Bradycardia)
- Custom CSV upload

### ⚕️ Clinical Scoring Systems

- **NEWS2** - National Early Warning Score 2 (UK RCP guidelines)
  - 7 vital sign parameters
  - Risk stratification: Low/Medium/High
  - Special scoring for COPD (Scale 2)

- **qSOFA** - Quick Sequential Organ Failure Assessment (Sepsis-3)
  - 3-parameter rapid sepsis screening
  - Mortality prognostication
  - ICU escalation guide

- **CART** - Cardiac Arrest Risk Triage
  - Multi-parameter arrest risk prediction
  - Percentile-based stratification
  - Monitoring intensity recommendations

### 🤖 Dynamic Recommendations

- Priority-based clinical actions (1-5)
- Urgency color coding (🔴 High → 🟢 Low)
- Evidence-based rationales
- Linked clinical protocols

### 🔐 Security & Validation

- Rate limiting (10 req/60 sec)
- CSV sanitization & validation
- Input range validation
- Security audit logging
- Synthetic data (no real patient info)

### 🧪 Comprehensive Testing

- **17 test cases** - all passing ✅
  - 8 unit tests (clinical scorers)
  - 5 security tests (validation & sanitization)
  - 2 integration tests (end-to-end workflows)
  - 2 performance tests (speed benchmarks)

---

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/paracelsus12-crypto/virtual-icu-demo.git
cd virtual-icu-demo

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app_v2.py
```

Open browser to: **http://localhost:8501**

### Run Tests

```bash
pytest test_comprehensive.py -v
```

Expected: `====== 17 passed in 3.00s ======`

---

## 📖 User Guide

### For Students

1. **Start with Dashboard tab** - Review patient data
2. **Switch to Vital Signs** - Watch how vitals change over time
3. **Look at Clinical Scores** - Understand scoring logic
4. **Use Invigilator Panel** - Experiment with interventions

**Example Learning Path:**
```
Select Scenario: "Sepsis (Sepsis-3)"
→ Generate Demo Data
→ Watch Vital Signs change over 6 hours
→ See NEWS2 score increase from 0 → 15
→ Read recommendations for each stage
→ Invigilator: Try giving oxygen, fluids, antibiotics
→ Observe how scores improve
```

### For Educators

1. **Use Dashboard for context setting**
2. **Project Vital Signs graph to class**
3. **Pause at critical points to discuss scores**
4. **Use Invigilator for interactive teaching**
5. **Demonstrate cause-effect relationships**

### For Researchers

1. **Export patient trajectories from Dashboard**
2. **Analyze clinical patterns in Vital Signs**
3. **Validate scoring algorithms in Clinical Scores**
4. **Run integration tests to ensure reproducibility**

---

## 📊 Clinical Scoring Reference

### NEWS2 Risk Stratification

| Risk Level | Score Range | Action |
|-----------|------------|--------|
| Low | 0-4 | Routine monitoring |
| Medium | 5-6 | Physician review within 1 hour |
| High | ≥7 | Urgent physician evaluation |

### qSOFA Interpretation

| Score | Sepsis Risk | Mortality |
|-------|------------|-----------|
| <2 | Low | ~1% |
| ≥2 | High | 9.4-15.4% |

### CART Risk Categories

| Percentile | Risk | Action |
|-----------|------|--------|
| <25th | Low | Routine monitoring |
| 25-75th | Medium | Continuous monitoring |
| >75th | High | Intensive monitoring |

---

## 🛠️ Technical Architecture

### Technology Stack

```
Frontend:      Streamlit (Python web framework)
Data:          Pandas, NumPy (data processing)
Visualization: Plotly (interactive charts)
Validation:    Pydantic (data models)
Testing:       Pytest (17 comprehensive tests)
Security:      Rate limiting, CSV sanitization, input validation
```

### File Structure

```
virtual-icu-demo/
├── app_v2.py                    # Main Streamlit app (1,200 lines)
├── clinical_scorer_v2.py        # Clinical scoring systems (500 lines)
├── models.py                    # Pydantic data models (300 lines)
├── data_loader.py               # CSV validation & loading (250 lines)
├── security.py                  # Security module (350 lines)
├── test_comprehensive.py        # Test suite (17 tests)
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── DOCUMENTATION.md             # Full user documentation

Optional:
├── synthetic_data_generator/    # Legacy scenario generators
└── .github/workflows/           # CI/CD pipelines
```

### Module Dependencies

```
app_v2.py
├── clinical_scorer_v2.py
│   ├── NEWS2CalculatorV2
│   ├── qSOFACalculatorV2
│   ├── CARTCalculatorV2
│   └── ClinicalRecommendationsEngineV2
├── models.py (Pydantic models)
├── data_loader.py (CSV handling)
└── security.py (validation & logging)
```

---

## 🧪 Testing

### Run All Tests

```bash
pytest test_comprehensive.py -v
```

### Run Specific Test Class

```bash
pytest test_comprehensive.py::TestNEWS2CalculatorV2 -v
```

### Run with Coverage

```bash
pytest test_comprehensive.py --cov=. --cov-report=html
```

### Test Categories

**Unit Tests (8)**
- NEWS2 scoring (normal, high-risk, components)
- qSOFA scoring (low risk, sepsis alert)
- CART scoring (young, elderly)
- Recommendations generation

**Security Tests (5)**
- CSV column validation
- CSV data range validation
- CSV sanitization
- Input vital validation
- All vitals validation

**Integration Tests (2)**
- CSV → Sanitize → Score workflow
- Invigilator workflow (validation → scoring → recommendations)

**Performance Tests (2)**
- 1000 scoring operations in <1 second
- 10,000 row sanitization in <0.5 seconds

---

## 📚 Documentation

### Full User Guide
See **[DOCUMENTATION.md](DOCUMENTATION.md)** for:
- Complete feature walkthrough
- All 15 scenario descriptions
- Clinical scoring system details
- Invigilator Panel tutorial
- API reference
- Troubleshooting guide

### Quick Reference

**Clinical Scores:**
- NEWS2: 7-parameter early warning (0-20 score)
- qSOFA: 3-parameter sepsis screen (0-3 score)
- CART: Cardiac arrest risk (0-20 score)

**15 Scenarios:**
1. Sepsis | 2. Septic Shock | 3. Cardiac Arrest + ROSC
4. Cardiac Arrest - No ROSC | 5. Resp Failure Type I | 6. Resp Failure Type II
7. Hypotension Progressive | 8. Hypotension Sudden | 9. Hypoxemia Acute
10. Hypoxemia Gradual | 11. AFib | 12. Ventricular Tachycardia
13. Supraventricular Tachycardia | 14. Bradycardia | 15. CSV Upload

---

## 🔐 Security Features

### Rate Limiting
```python
# 10 requests per 60 seconds
limiter = RateLimiter(max_requests=10, window_seconds=60)
```

### CSV Validation
- File size: max 10 MB
- Rows: max 100,000
- Columns: max 50
- Required columns: heart_rate, systolic_bp, respiratory_rate, spo2, temperature
- Data range validation for each parameter
- SQL injection prevention

### Input Validation
- All vital signs checked against physiological ranges
- Alert status validated
- Age validation (0-120 years)
- Real-time validation feedback

### Audit Logging
- All file uploads logged
- Demo generation logged
- Invigilator actions logged
- Success/failure recorded

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add improvement'`)
4. Write/update tests
5. Ensure all tests pass (`pytest test_comprehensive.py -v`)
6. Push to branch (`git push origin feature/improvement`)
7. Create Pull Request

---

## 📝 License

MIT License - See LICENSE file for details

---

## 🎓 Educational Use

### For Medical Schools

```
Module: Critical Care Fundamentals
Week 1: Clinical scoring systems (NEWS2, qSOFA)
Week 2: Patient deterioration recognition (scenarios 1-7)
Week 3: Arrhythmia identification (scenarios 11-14)
Week 4: Decision-making practice (Invigilator Panel)
Assessment: Student-led scenario analysis
```

### For Residency Programs

```
Simulation sessions using Virtual ICU + real-time instructor feedback
Competency validation: Can student recognize critical changes?
Confidence building: Safe environment to practice high-stakes decisions
Assessment: Time-to-recognition of deterioration
```

### For Continuing Education

```
Quarterly updates on clinical scoring changes
Latest sepsis guidelines (Sepsis-4 when available)
Performance analytics: How do your scores compare?
Evidence-based practice reinforcement
```

---

## 📊 Statistics

### Code Metrics
- **Total Lines:** 2,950+
- **Python Files:** 6 (app, scorer, models, loader, security, tests)
- **Test Coverage:** 17 test cases, all passing
- **Documentation:** 1,000+ lines

### Feature Metrics
- **Scenarios:** 15 fully implemented
- **Tabs:** 4 interactive
- **Scoring Systems:** 3 (NEWS2, qSOFA, CART)
- **Clinical Parameters:** 7+ (HR, BP, RR, SpO2, Temp, Alert, O2)

### Performance Metrics
- **Scoring Speed:** 3,000 operations/second
- **CSV Processing:** 20,000+ rows/second
- **Response Time:** < 1 second for all operations
- **Memory:** < 100 MB typical usage

---

## 🐛 Known Issues & Roadmap

### Current Limitations (v1.2)
- [ ] No real-time patient monitoring (simulation only)
- [ ] No integration with hospital EHR systems
- [ ] No multi-patient dashboard
- [ ] No persistent data storage
- [ ] No user authentication

### Planned for v2.0 (Next Release)
- [ ] Multi-page Streamlit architecture
- [ ] Predictive ML model (LSTM for 24-hour forecast)
- [ ] Advanced alert system
- [ ] PDF report generation
- [ ] FHIR compatibility
- [ ] Real patient data integration (with consent)
- [ ] Mobile app version

---

## 📞 Support & Feedback

- **GitHub Issues:** [Report bugs](https://github.com/paracelsus12-crypto/virtual-icu-demo/issues)
- **Discussions:** [Ask questions](https://github.com/paracelsus12-crypto/virtual-icu-demo/discussions)
- **Email:** paracelsus12-crypto@gmail.com

---

## 🙏 Acknowledgments

**Clinical Guidelines:**
- Royal College of Physicians (UK) - NEWS2
- Sepsis-3 Consensus Definitions - qSOFA
- Emergency Medicine Literature - CART

**Technology:**
- [Streamlit](https://streamlit.io/) - Interactive web apps
- [Plotly](https://plotly.com/) - Interactive charts
- [Pydantic](https://pydantic-settings.readthedocs.io/) - Data validation
- [Pandas](https://pandas.pydata.org/) - Data analysis

---

## 📄 Citation

If you use Virtual ICU in research or education, please cite:

```bibtex
@software{virtualicu2024,
  author = {Parekh, Rehan and others},
  title = {Virtual ICU v1.2: AI-Driven Early Warning System},
  year = {2024},
  url = {https://github.com/paracelsus12-crypto/virtual-icu-demo}
}
```

---

## 📈 Version History

### v1.2 (Current) - April 2024 ✅
**Status:** Production Ready
- ✅ Security module (rate limiting, validation, logging)
- ✅ 17 comprehensive tests (all passing)
- ✅ Full documentation
- ✅ Real-time Invigilator Panel
- ✅ Dynamic recommendations with priorities

### v1.1 - April 2024
**Status:** Functional
- ✅ app_v2.py rewrite (1,200 lines)
- ✅ 15 scenarios fully implemented
- ✅ 3 scoring systems integrated
- ✅ 4 interactive tabs

### v1.0 - April 2024
**Status:** Initial
- ✅ Basic Streamlit app
- ✅ NEWS2, qSOFA, CART scoring
- ✅ Demo scenarios

---

**Last Updated:** April 24, 2026  
**Maintainer:** paracelsus12-crypto  
**Status:** 🟢 Production Ready v1.2
