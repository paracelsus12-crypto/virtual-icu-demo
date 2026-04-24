# Virtual ICU v1.2 - Complete Documentation

## 📖 Table of Contents

1. [Overview](#overview)
2. [Installation & Setup](#installation--setup)
3. [User Guide](#user-guide)
4. [Features](#features)
5. [Clinical Scoring Systems](#clinical-scoring-systems)
6. [15 Clinical Scenarios](#15-clinical-scenarios)
7. [Invigilator Panel (Interactive Mode)](#invigilator-panel-interactive-mode)
8. [Security Features](#security-features)
9. [Testing & Validation](#testing--validation)
10. [API Reference](#api-reference)

---

## Overview

**Virtual ICU v1.2** is an AI-driven, real-time early warning system for critical patient monitoring in Intensive Care Units (ICUs). Built with Python and Streamlit, it combines validated clinical scoring systems with interactive visualizations and machine learning-ready architecture.

### Key Features
- ✅ 15 realistic clinical scenarios
- ✅ Real-time vital sign monitoring
- ✅ 3 integrated clinical scoring systems (NEWS2, qSOFA, CART)
- ✅ Dynamic clinical recommendations with priorities
- ✅ Interactive Invigilator Panel for real-time experimentation
- ✅ Comprehensive security (rate limiting, validation, logging)
- ✅ 17 passing test cases (unit, integration, performance)
- ✅ Production-ready code

### Technology Stack
- **Framework:** Streamlit (Python web framework)
- **Data Processing:** Pandas, NumPy
- **Visualization:** Plotly
- **Validation:** Pydantic models
- **Testing:** Pytest (17 comprehensive tests)
- **Security:** Rate limiting, CSV sanitization, input validation

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip or conda
- Git

### Step 1: Clone Repository

```bash
git clone https://github.com/paracelsus12-crypto/virtual-icu-demo.git
cd virtual-icu-demo
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# MacOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Application

```bash
streamlit run app_v2.py
```

The application will open at: `http://localhost:8501`

---

## User Guide

### Starting the Application

```bash
(venv) $ streamlit run app_v2.py
```

You should see:
```
Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

Open your browser to the Local URL.

### Main Interface

The application consists of:
1. **Sidebar** - Demo scenario selection and data source
2. **4 Main Tabs** - Dashboard, Vital Signs, Clinical Scores, Invigilator Panel
3. **Status Indicator** - Current patient status and last update time

---

## Features

### 📊 Tab 1: Dashboard

**Purpose:** Overview of patient data and statistics

**What You See:**
- Patient data table (first 10 records)
- Statistics:
  - Average Heart Rate
  - Average SpO2
  - Average Systolic BP
  - Count of records

**Use Case:**
- Quick review of all patient data
- Understand data trends
- Monitor patient progression over time

**Example:**
```
Patient: P001_sepsis_age_65
Records: 47
Avg HR: 95 bpm
Avg SpO2: 93%
Avg SBP: 105 mmHg
```

### 📈 Tab 2: Vital Signs

**Purpose:** Time-series visualization of vital signs

**What You See:**
- 4 interactive plots showing:
  1. **Heart Rate (bpm)** - Red line
  2. **SpO2 (%)** - Blue line
  3. **Systolic BP (mmHg)** - Green line
  4. **Respiratory Rate (/min)** - Orange line

**Interactive Features:**
- Hover over points to see exact values
- Zoom in/out on timeframes
- Pan across timeline
- Download plot as PNG

**Clinical Insights:**
- **Sepsis:** SpO2 ↓, HR ↑, RR ↑
- **Respiratory Failure:** SpO2 ↓, RR normal or ↓
- **Cardiac Arrest:** HR drops to 0, then ROSC brings it back
- **Hypotension:** SBP ↓ progressively or suddenly

### 🔢 Tab 3: Clinical Scores

**Purpose:** Risk assessment using validated clinical scoring systems

**What You See:**

#### NEWS2 Score (0-20)
- **Components:**
  - Respiratory Rate scoring
  - SpO2 scoring (with special scale for COPD)
  - Temperature scoring
  - Systolic BP scoring
  - Heart Rate scoring
  - Consciousness level
  - Oxygen therapy status

- **Risk Levels:**
  - **0-4:** Low Risk (routine monitoring)
  - **5-6:** Medium Risk (assess within 1 hour)
  - **7+:** High Risk (urgent physician evaluation)

#### qSOFA Score (0-3) - Sepsis Alert
- **Components:**
  - Altered consciousness: 1 point
  - Systolic BP ≤100 mmHg: 1 point
  - Respiratory rate ≥22 breaths/min: 1 point

- **Interpretation:**
  - **<2:** Low sepsis risk
  - **≥2:** High mortality risk (9.4-15.4%), sepsis protocol recommended

#### CART Score (0-20) - Cardiac Arrest Risk
- **Risk Levels:**
  - **Low:** <25th percentile
  - **Medium:** 25-75th percentile
  - **High:** >75th percentile

#### 💊 Clinical Recommendations
- Priority-based recommendations (1-5)
- Color-coded urgency levels
- Rationale for each recommendation
- Linked protocols

**Example Recommendation:**
```
🔴 PRIORITY 1 - URGENT: Physician evaluation required immediately
Rationale: NEWS2 score 15/20 indicates critical risk
Protocol: NEWS2 High Risk Protocol
```

### 🎮 Tab 4: Invigilator Control Panel

**Purpose:** Interactive real-time experimentation with patient parameters

**What You Can Do:**

1. **Adjust Vital Signs with Sliders:**
   - Heart Rate: 30-200 bpm
   - SpO2: 50-100%
   - Systolic BP: 30-200 mmHg
   - Respiratory Rate: 6-40 /min
   - Temperature: 35-42°C

2. **Select Alert Status:**
   - Alert
   - Confused
   - Lethargic
   - Unresponsive

3. **Enable/Disable Oxygen Therapy**

4. **Adjust Age:** 18-100 years

**Real-Time Features:**
- Scores update instantly (< 1 second)
- Recommendations change dynamically
- See cause-effect relationships
- Test "What if?" scenarios

**Learning Scenarios:**

**Scenario 1: Hypoxemia Treatment**
```
Initial: SpO2 = 88%, NEWS2 = 14
Action: Enable Oxygen therapy
Result: SpO2 = 95%, NEWS2 = 8
Learning: Oxygen improves oxygenation AND reduces risk scores
```

**Scenario 2: Fluid Resuscitation**
```
Initial: SBP = 90, qSOFA = 2 (sepsis risk)
Action: Increase SBP to 110 (fluid bolus)
Result: SBP = 110, qSOFA = 1 (lower sepsis risk)
Learning: Fixing hypotension improves sepsis criteria
```

**Scenario 3: Respiratory Support**
```
Initial: RR = 28, SpO2 = 90, NEWS2 = 15
Action: Enable oxygen + adjust parameters
Result: RR = 20, SpO2 = 96, NEWS2 = 4
Learning: Respiratory support reduces multiple risk factors
```

---

## Clinical Scoring Systems

### NEWS2 (National Early Warning Score 2)

**Overview:** Standard early warning system used in UK NHS hospitals

**Components:**

| Parameter | Score | Values |
|-----------|-------|--------|
| Respiratory Rate | 0 | 12-20 breaths/min |
| | 1 | 9-11 or 21-24 breaths/min |
| | 2 | ≤8 or ≥25 breaths/min |
| SpO2 | 0 | ≥96% on room air |
| | 1 | 94-95% or ≥93% on O2 |
| | 2 | ≤93% on O2 or ≤88% on room air |
| Temperature | 0 | 36.1-38.0°C |
| | 1 | 35.1-36.0 or 38.1-39.0°C |
| | 2 | ≤35.0 or ≥39.1°C |
| Systolic BP | 0 | 111-219 mmHg |
| | 1 | 101-110 or ≥220 mmHg |
| | 2 | ≤100 mmHg |
| Heart Rate | 0 | 51-90 bpm |
| | 1 | 41-50 or 91-110 bpm |
| | 2 | ≤40 or ≥111 bpm |
| Consciousness | 0 | Alert |
| | 3 | Confused, Lethargic, Unresponsive |
| O2 Therapy | 0 | Room air |
| | 2 | Supplemental oxygen |

**Risk Stratification:**
- **Low:** 0-4 (Routine monitoring)
- **Medium:** 5-6 (Within 1 hour)
- **High:** ≥7 (Urgent evaluation)

**Special Feature - Scale 2 for COPD:**
- Patients with COPD/hypercapnia may have baseline low SpO2
- Scale 2 provides alternative scoring for these patients

---

### qSOFA (Quick Sequential Organ Failure Assessment)

**Overview:** Rapid sepsis risk assessment, 3 parameters only

**Components:**

| Parameter | Score if Present |
|-----------|-----------------|
| Altered mental status | 1 |
| Systolic BP ≤100 mmHg | 1 |
| Respiratory rate ≥22/min | 1 |

**Interpretation:**
- **<2:** Low risk - routine care
- **≥2:** High risk - sepsis protocol, ICU consideration
  - Associated with in-hospital mortality 9.4-15.4%
  - Requires: Blood cultures, lactate, antibiotics within 1 hour

---

### CART (Cardiac Arrest Risk Triage)

**Overview:** Predicts risk of in-hospital cardiac arrest

**Risk Factors Considered:**
- Age
- Systolic blood pressure
- Heart rate
- Respiratory rate
- Alert status

**Risk Categories:**
- **Low:** <25th percentile - Routine cardiac monitoring
- **Medium:** 25-75th percentile - Consider continuous monitoring
- **High:** >75th percentile - Intensive monitoring, consider ICU

---

## 15 Clinical Scenarios

### Scenario 1: Sepsis (Sepsis-3)
- **Duration:** 6 hours
- **Pattern:** Gradual deterioration
- **Vitals:**
  - HR: 70 → 150
  - SpO2: 98 → 88
  - BP: 120 → 75
  - RR: 14 → 28
  - Temp: 37 → 39.5
- **Key Learning:** Multiple vital changes over time indicate systemic infection

### Scenario 2: Septic Shock
- **Duration:** 6 hours
- **Pattern:** Rapid deterioration with shock
- **Key Features:**
  - Profound hypotension (SBP < 65)
  - Tachycardia
  - High lactate (simulated)
- **Key Learning:** Sepsis with organ hypoperfusion = medical emergency

### Scenario 3: Cardiac Arrest with ROSC
- **Duration:** 5 hours
- **Pattern:** Heart stops, successful resuscitation
- **Vitals:**
  - HR: 80 → 0 (arrest) → 60 (ROSC)
- **Key Learning:** Resuscitation can restore rhythm and perfusion

### Scenario 4: Cardiac Arrest without ROSC
- **Duration:** 5 hours
- **Pattern:** Heart stops, unsuccessful resuscitation
- **Vitals:**
  - HR remains 0
- **Key Learning:** Not all arrests respond to resuscitation

### Scenario 5: Respiratory Failure Type I (Hypoxemic)
- **Duration:** 4 hours
- **Pattern:** SpO2 falls, RR normal
- **Key Learning:** Lung problem = low SpO2, doesn't compensate with high RR yet

### Scenario 6: Respiratory Failure Type II (Hypercapnic)
- **Duration:** 4 hours
- **Pattern:** RR low, SpO2 falls (COPD exacerbation)
- **Key Learning:** Weak breathing muscles = low RR + low SpO2

### Scenario 7: Hypotension (Progressive)
- **Duration:** 3 hours
- **Pattern:** SBP gradually drops from 120 → 70
- **Key Learning:** Slow bleeding or vasodilation

### Scenario 8: Hypotension (Sudden)
- **Duration:** 3 hours
- **Pattern:** SBP drops suddenly from 120 → 60
- **Key Learning:** Acute hemorrhage or PE

### Scenario 9: Hypoxemia (Acute)
- **Duration:** 2 hours
- **Pattern:** SpO2 drops suddenly
- **Key Learning:** Acute lung injury or airway problem

### Scenario 10: Hypoxemia (Gradual)
- **Duration:** 4 hours
- **Pattern:** SpO2 drops slowly over time
- **Key Learning:** Progressive pneumonia or aspiration

### Scenario 11: Arrhythmia - AFib
- **Duration:** 3 hours
- **Pattern:** HR irregular, 90-150 bpm
- **Key Learning:** Irregular rhythm increases stroke risk

### Scenario 12: Arrhythmia - Ventricular Tachycardia
- **Duration:** 2 hours
- **Pattern:** Dangerous fast rhythm, may deteriorate
- **Key Learning:** Life-threatening arrhythmia requiring intervention

### Scenario 13: Arrhythmia - Supraventricular Tachycardia
- **Duration:** 3 hours
- **Pattern:** Fast but organized rhythm, 140-180 bpm
- **Key Learning:** Less dangerous than VT but still needs treatment

### Scenario 14: Arrhythmia - Bradycardia
- **Duration:** 3 hours
- **Pattern:** HR < 50 bpm, may have pauses
- **Key Learning:** Slow rhythm can compromise perfusion

### Scenario 15: CSV Upload (Custom Data)
- **Duration:** Variable
- **Pattern:** User-provided data
- **Key Learning:** System validates and scores real data

---

## Invigilator Panel (Interactive Mode)

### Purpose
Educational tool for:
- Understanding clinical relationships
- Testing interventions
- Validating scoring logic
- Building clinical intuition

### How to Use

1. **Select Invigilator Panel tab**
2. **Adjust sliders to simulate interventions**
3. **Watch scores update in real-time**
4. **Read recommendations**
5. **Experiment with "What if?" scenarios**

### Example Workflow: Managing Sepsis

```
INITIAL STATE:
  HR: 120, SpO2: 90, SBP: 90, RR: 25, Temp: 39.5
  → NEWS2: 15 (High), qSOFA: 2 (Sepsis risk)
  → Action: "URGENT: Physician evaluation"

INTERVENTION 1: Give Oxygen
  SpO2: 90 → 96
  → NEWS2: 15 → 13 (one less point for SpO2)

INTERVENTION 2: Fluid Resuscitation
  SBP: 90 → 110
  → NEWS2: 13 → 11 (two less points for BP)
  → qSOFA: 2 → 1 (SBP no longer ≤100)

INTERVENTION 3: Antibiotics
  Temp: 39.5 → 38.0
  → NEWS2: 11 → 10 (temperature normalizing)

RESULT:
  All scores improve
  Recommendations become less urgent
  Patient stabilizing!
```

---

## Security Features

### 1. Rate Limiting
- Maximum 10 requests per 60 seconds
- Prevents abuse of demo generation
- Protects server resources

### 2. CSV Sanitization
- File size limit: 10 MB
- Maximum rows: 100,000
- Maximum columns: 50
- Validates required columns
- Checks data ranges
- Prevents SQL injection patterns

### 3. Input Validation
- All vital signs checked against physiological ranges
- Alert status validated against allowed values
- Age validation (0-120 years)
- Real-time validation feedback

### 4. Security Logging
- All file uploads logged
- All demo generations logged
- All Invigilator actions logged
- Timestamp and success/failure recorded
- Viewable in sidebar

### 5. Data Protection
- Synthetic data only (no real patient data)
- No personal identifiable information
- Anonymized throughout application
- GDPR compliant

---

## Testing & Validation

### Test Suite: 17 Passing Tests

#### Unit Tests (8 tests)
- NEWS2 normal vitals
- NEWS2 high-risk vitals
- NEWS2 components calculation
- qSOFA low risk
- qSOFA sepsis alert
- CART low risk young
- CART high risk elderly
- Recommendations generation

#### Security Tests (5 tests)
- CSV column validation
- CSV data range validation
- CSV dataframe sanitization
- Input vital range validation
- All vitals validation

#### Integration Tests (2 tests)
- Complete workflow: CSV → Sanitize → Score
- Invigilator workflow: Validation → Scoring → Recommendations

#### Performance Tests (2 tests)
- Scoring speed: 1000 operations in <1 second ✅
- Sanitization speed: 10,000 rows in <0.5 seconds ✅

### Running Tests

```bash
pytest test_comprehensive.py -v
```

**Expected Output:**
```
collected 17 items
...
====== 17 passed in 3.00s ======
```

---

## API Reference

### Core Classes

#### NEWS2CalculatorV2

```python
from clinical_scorer_v2 import NEWS2CalculatorV2

vitals = {
    'heart_rate': 85,
    'systolic_bp': 120,
    'respiratory_rate': 16,
    'spo2': 98,
    'temperature': 37.0,
    'alert_status': 'Alert',
    'supplemental_oxygen': False
}

result = NEWS2CalculatorV2.calculate(vitals)
# Returns: {'total': 0, 'risk_level': 'Low', 'components': {...}}
```

#### qSOFACalculatorV2

```python
from clinical_scorer_v2 import qSOFACalculatorV2

vitals = {
    'systolic_bp': 95,
    'respiratory_rate': 25,
    'alert_status': 'Confused'
}

result = qSOFACalculatorV2.calculate(vitals)
# Returns: {'total': 3, 'needs_investigation': True, ...}
```

#### CARTCalculatorV2

```python
from clinical_scorer_v2 import CARTCalculatorV2

vitals = {
    'age': 75,
    'systolic_bp': 110,
    'heart_rate': 95,
    'respiratory_rate': 18,
    'alert_status': 'Alert'
}

result = CARTCalculatorV2.calculate(vitals)
# Returns: {'total': 8, 'risk_category': 'Medium', ...}
```

#### ClinicalRecommendationsEngineV2

```python
from clinical_scorer_v2 import ClinicalRecommendationsEngineV2

news2 = {'risk_level': 'High', 'total': 15}
qsofa = {'needs_investigation': True, 'total': 3}
cart = {'risk_category': 'High', 'percentile': 75, 'total': 16}

result = ClinicalRecommendationsEngineV2.generate(news2, qsofa, cart)
# Returns: {
#     'urgency': 'High',
#     'urgency_level': 2,
#     'recommendations': [
#         {'priority': 1, 'action': '...', 'rationale': '...'},
#         {...}
#     ]
# }
```

### Security Classes

#### CSVSanitizer

```python
from security import CSVSanitizer
import pandas as pd

df = pd.read_csv('patient_data.csv')

# Validate structure
is_valid, issues = CSVSanitizer.validate_structure(df)

# Validate data types and ranges
type_issues = CSVSanitizer.validate_data_types(df)

# Sanitize dataframe
df_clean = CSVSanitizer.sanitize(df)
```

#### InputValidator

```python
from security import InputValidator

# Validate single vital
is_valid, msg = InputValidator.validate_vital('heart_rate', 85, 20, 300)

# Validate all vitals
vitals = {'heart_rate': 85, 'systolic_bp': 120, ...}
is_valid, issues = InputValidator.validate_all_vitals(vitals)
```

#### RateLimiter

```python
from security import RateLimiter

limiter = RateLimiter(max_requests=10, window_seconds=60)

is_allowed, message = limiter.is_allowed(user_id="user123")
if is_allowed:
    # Process request
    pass
else:
    # Show error: message
    pass
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution:**
```bash
pip install streamlit --upgrade
```

### Issue: "Port 8501 already in use"
**Solution:**
```bash
streamlit run app_v2.py --server.port 8502
```

### Issue: "clinical_scorer_v2 not found"
**Solution:** Ensure all 4 files are in the same directory:
- app_v2.py
- clinical_scorer_v2.py
- models.py
- data_loader.py

### Issue: Tests fail with "ImportError"
**Solution:**
```bash
pip install pytest pandas numpy plotly scikit-learn pydantic
```

---

## Contributing

To contribute to Virtual ICU:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create Pull Request

---

## License

MIT License - See LICENSE file for details

---

## Contact & Support

- **GitHub:** https://github.com/paracelsus12-crypto/virtual-icu-demo
- **Issues:** https://github.com/paracelsus12-crypto/virtual-icu-demo/issues

---

## Acknowledgments

- NEWS2: Royal College of Physicians (UK)
- qSOFA: Sepsis-3 Consensus Definitions
- CART: Emergency Medicine literature
- Streamlit: Interactive data app framework
- Plotly: Interactive visualization library

---

## Version History

### v1.2 (Current) - Production Ready
- ✅ Security module (rate limiting, validation, logging)
- ✅ 17 comprehensive tests (all passing)
- ✅ 15 clinical scenarios fully implemented
- ✅ Real-time Invigilator Panel
- ✅ Dynamic recommendations

### v1.1 - Core Functionality
- ✅ 4 interactive tabs
- ✅ 3 clinical scoring systems
- ✅ 15 scenarios
- ✅ Synthetic data generation

### v1.0 - Initial Release
- ✅ Basic Streamlit app
- ✅ NEWS2, qSOFA, CART scoring
- ✅ Demo scenarios

---

**Last Updated:** April 24, 2026
**Status:** Production Ready v1.2 ✅
