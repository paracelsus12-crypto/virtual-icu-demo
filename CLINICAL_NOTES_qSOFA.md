"""
CLINICAL NOTES: qSOFA SCORING SYSTEM
Understanding when sepsis alerts are APPROPRIATE vs FALSE POSITIVES
"""

# ════════════════════════════════════════════════════════════════════
# qSOFA CRITERIA & CLINICAL CONTEXT
# ════════════════════════════════════════════════════════════════════

"""
qSOFA SCORING (Quick Sequential Organ Failure Assessment):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Component 1: ALTERED MENTAL STATUS (1 point if YES)
  Clinical signs: Confusion, disorientation, acute change in consciousness
  Mechanism: Sepsis-induced organ dysfunction
  ✅ Appropriate: Fever + infection + confusion
  ❌ False positive: Confusion from hypoxia alone, AFib, or intoxication

Component 2: SYSTOLIC BP ≤100 mmHg (1 point if YES)
  Clinical signs: Hypotension, weak perfusion
  Mechanism: Septic shock (vasodilation, cardiomyopathy)
  ✅ Appropriate: Low BP + fever + lactate elevation
  ❌ False positive: Low BP from aortic stenosis, VT, dehydration (non-septic)

Component 3: RESPIRATORY RATE ≥22/min (1 point if YES)
  Clinical signs: Tachypnea, increased work of breathing
  Mechanism: Metabolic acidosis (sepsis) or respiratory compensation
  ✅ Appropriate: High RR + fever + altered mental status
  ❌ False positive: High RR from pain, anxiety, AFib (heart rate response), pneumonia

SCORE ≥2 = HIGH RISK OF SEPSIS (9.4-15.4% in-hospital mortality)
           → Blood cultures, lactate, antibiotics within 1 hour

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ════════════════════════════════════════════════════════════════════
# CASE EXAMPLES
# ════════════════════════════════════════════════════════════════════

"""
CASE 1: TRUE SEPSIS (qSOFA ≥2 is APPROPRIATE) ✅
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Patient: 72-year-old woman with UTI
Vitals:
  • HR: 110 (tachycardia)
  • RR: 24 (/min) ✅ QSOFA POINT 1
  • SBP: 95 mmHg ✅ QSOFA POINT 2
  • Temp: 38.5°C (fever)
  • SpO2: 94%
  • Mental status: CONFUSED ✅ QSOFA POINT 3 (BONUS!)

qSOFA Score: 3/3 (CRITICAL!)
Diagnosis: Urosepsis with septic shock
Action: IMMEDIATE → Blood cultures, broad-spectrum antibiotics, fluids
Result: ✅ CORRECT ALERT - saves life


CASE 2: AFib WITHOUT SEPSIS (qSOFA ≥2 is FALSE POSITIVE) ❌ NOW FIXED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Patient: 68-year-old man with new-onset AFib
Vitals (OLD, INCORRECT):
  • HR: 166 (tachycardia - PRIMARY problem)
  • RR: 25 (/min) ❌ HIGH (secondary to HR response, not sepsis)
  • SBP: 90 mmHg ❌ LOW (from rapid rate, not septic shock)
  • Temp: 37°C (NORMAL)
  • SpO2: 92% ❌ (mild hypoxia from poor cardiac output)
  • Mental status: Alert

qSOFA Score: 2/3 (FALSE POSITIVE!)
Problem: AFib triggers tachypnea + hypotension, mimics sepsis
Result: ❌ INAPPROPRIATE SEPSIS ALERT

Vitals (NEW, CORRECTED):
  • HR: 160 (tachycardia - PRIMARY problem)
  • RR: 16 (/min) ✅ NORMAL (respiratory rate NOT affected by heart rate alone)
  • SBP: 118 mmHg ✅ NORMAL (AFib patients often maintain reasonable BP)
  • Temp: 37°C ✅ NORMAL (NO fever)
  • SpO2: 97% ✅ NORMAL (SpO2 usually preserved)
  • Mental status: Alert ✅ NORMAL

qSOFA Score: 0/3
Diagnosis: Supraventricular tachycardia (AFib)
Action: ECG, rate control (beta-blockers), consider anticoagulation
Result: ✅ CORRECT - no false sepsis alert


CASE 3: VT WITH SHOCK (qSOFA MAY BE ELEVATED) ⚠️
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Patient: 55-year-old with ischemic heart disease, VT
Vitals:
  • HR: 180 (very rapid, unstable)
  • RR: 24 (/min) ✅ QSOFA POINT 1 (compensation)
  • SBP: 85 mmHg ✅ QSOFA POINT 2 (cardiogenic shock)
  • Temp: 37°C (NORMAL)
  • SpO2: 89% ❌ (severe hypoxia)
  • Mental status: Confused/LOC

qSOFA Score: 2-3/3
Differential diagnosis: VT with cardiogenic shock vs sepsis
Key difference:
  • NO fever (against sepsis)
  • NO infection source (against sepsis)
  • Acute ECG changes (favors VT)
  • Lactate elevated from shock (not sepsis-specific)
Action: STAT ECG, defibrillation prep, IV access, ICU
Result: ✅ HIGH ALERT APPROPRIATE (though for different reason: cardiogenic shock, not sepsis)
"""

# ════════════════════════════════════════════════════════════════════
# KEY TEACHING POINTS
# ════════════════════════════════════════════════════════════════════

"""
🎓 WHY THE FIX IS IMPORTANT:

1. qSOFA ≥2 is a SCREENING TOOL for SEPSIS
   → Should trigger sepsis workup (cultures, lactate, antibiotics)
   → NOT a diagnosis tool (can have false positives)

2. AFib patients may have ELEVATED qSOFA from:
   • High RR (compensatory tachypnea)
   • Low BP (from rapid rate reducing diastolic filling time)
   → BUT no sepsis! (No fever, no infection, alert mental status)

3. The FIX ensures:
   • AFib = HIGH HR + NORMAL RR + NORMAL BP + NORMAL SpO2
   • VT = HIGH HR + ELEVATED RR + LOW BP + LOW SpO2 (true shock)
   • This preserves clinical accuracy and prevents unnecessary antibiotic use

4. SEPSIS-3 CRITERIA (Sepsis-3 Consensus):
   "Sepsis = life-threatening organ dysfunction caused by dysregulated host response to infection"
   
   KEY: Requires INFECTION (fever, source, labs) + ORGAN DYSFUNCTION
   
   AFib alone = Cardiac dysrhythmia, NOT sepsis
   AFib + fever + elevated lactate = Possible sepsis complicating AFib
"""

# ════════════════════════════════════════════════════════════════════
# CLINICAL DECISION TREE
# ════════════════════════════════════════════════════════════════════

"""
If qSOFA ≥2, ask yourself:

┌─────────────────────────────────────────────────────────────────┐
│ Step 1: Is there FEVER (Temp >38°C or <36°C)? │
├─────────────────────────────────────────────────────────────────┤
│ NO  → Unlikely to be sepsis                                      │
│       (Consider: AFib, VT, MI, PE, other cardiac/pulm causes)   │
│       Action: Investigate primary cause (ECG, imaging, etc.)    │
│                                                                  │
│ YES → Continue to Step 2                                         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ Step 2: Is there a KNOWN or SUSPECTED INFECTION SOURCE?         │
├─────────────────────────────────────────────────────────────────┤
│ NO  → Fever + hypotension but no source?                         │
│       Action: Urgent cultures, CXR, lactate; start empiric ABX  │
│       (Still treat as sepsis until proven otherwise)            │
│                                                                  │
│ YES → Continue to Step 3                                         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ Step 3: Are there ADDITIONAL organ dysfunction markers?          │
├─────────────────────────────────────────────────────────────────┤
│ Check: Lactate >2, Creatinine ↑, Bilirubin ↑, Platelets ↓      │
│        GCS change, Input/output imbalance                       │
│                                                                  │
│ YES → qSOFA ≥2 + Fever + Source + Organ dysfunction             │
│       = SEPSIS (or at least must be treated as such)            │
│       Action: SEPSIS BUNDLE - antibiotics, fluids, vasopressors │
│                                                                  │
│ NO  → qSOFA ≥2 + Fever + Source, but NO organ dysfunction       │
│       = Possible SIRS from localized infection                  │
│       Action: Treat infection, but sepsis bundle NOT automatic  │
└─────────────────────────────────────────────────────────────────┘
"""

# ════════════════════════════════════════════════════════════════════
# WHAT CHANGED IN Virtual ICU v2.0 FIX
# ════════════════════════════════════════════════════════════════════

"""
ARRHYTHMIA SCENARIOS (AFib, SVT, Bradycardia):

BEFORE FIX (INCORRECT):
  • HR: 150-180 (high - correct for AFib)
  • RR: 25 (/min) ❌ TOO HIGH (not physiologic for AFib alone)
  • SBP: 90 mmHg ❌ TOO LOW (AFib can compensate better)
  • SpO2: 92% ❌ TOO LOW (not typical)
  • Temp: 37°C (correct)
  
  Result: qSOFA = 2/3 (FALSE ALERT)
          → "Sepsis Alert" shown to students
          → Teaches WRONG clinical behavior

AFTER FIX (CORRECT):
  • HR: 120-160 (tachycardia from AFib)
  • RR: 14-16 (/min) ✅ NORMAL (not sepsis-elevated)
  • SBP: 115-125 mmHg ✅ NORMAL (AFib maintains reasonable perfusion)
  • SpO2: 97% ✅ NORMAL (preserved oxygenation)
  • Temp: 37°C (normal)
  
  Result: qSOFA = 0/3 (CORRECT - no alert)
          → "Cardiac arrhythmia, not sepsis"
          → Teaches CORRECT clinical behavior
          → Students learn to differentiate causes of tachypnea/hypotension

VT SCENARIO (more unstable):
  • HR: 140-180 (very rapid, malignant)
  • RR: 16-24 (/min) ⚠️ ELEVATED (from cardiogenic shock, not sepsis)
  • SBP: 90 mmHg ⚠️ LOW (cardiogenic shock)
  • SpO2: 90-95% (hypoxia from shock)
  • Temp: 37°C (normal)
  
  Result: qSOFA = 2/3 (elevated, BUT...)
          → HIGH ALERT STILL APPROPRIATE
          → Reason: Cardiogenic shock (different treatment than sepsis)
          → But students learn: Not all qSOFA ≥2 = sepsis
"""

# ════════════════════════════════════════════════════════════════════
# SUMMARY FOR STUDENTS
# ════════════════════════════════════════════════════════════════════

"""
✅ KEY TAKEAWAY:

qSOFA is a SCREENING tool, not a diagnosis tool.

It helps you identify SICK patients who MIGHT have sepsis.

But you MUST also look for:
  ✓ Fever or hypothermia
  ✓ Known infection source
  ✓ Lactate elevation
  ✓ Other organ dysfunction signs

AFib with HR 160 + RR 25 + SBP 90 might LOOK like sepsis...
But NO fever + NO infection + Normal SpO2 = NOT sepsis!

Don't be fooled by vital sign patterns alone.
Always ask: "What is the PATHOPHYSIOLOGY here?"
"""
