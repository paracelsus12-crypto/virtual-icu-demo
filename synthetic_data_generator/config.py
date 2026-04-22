"""
Virtual ICU - Configuration Module
Contains all system parameters and clinical ranges
"""

import yaml
from typing import Dict, Any
from pathlib import Path

class VitalSignsConfig:
    """Configuration for vital signs parameters"""
    
    # Heart Rate (bpm)
    HEART_RATE = {
        "baseline": 70,
        "unit": "bpm",
        "range": [40, 180],
        "critical_low": 40,
        "critical_high": 150,
    }
    
    # Systolic Blood Pressure (mmHg)
    SYSTOLIC_BP = {
        "baseline": 120,
        "unit": "mmHg",
        "range": [50, 200],
        "critical_low": 70,
        "critical_high": 180,
    }
    
    # Diastolic Blood Pressure (mmHg)
    DIASTOLIC_BP = {
        "baseline": 80,
        "unit": "mmHg",
        "range": [30, 130],
        "critical_low": 40,
        "critical_high": 120,
    }
    
    # Respiratory Rate (breaths/min)
    RESPIRATORY_RATE = {
        "baseline": 14,
        "unit": "breaths/min",
        "range": [6, 40],
        "critical_low": 8,
        "critical_high": 35,
    }
    
    # Oxygen Saturation (%)
    SPO2 = {
        "baseline": 98,
        "unit": "%",
        "range": [70, 100],
        "critical_low": 88,
        "critical_high": 100,
    }
    
    # Temperature (°C)
    TEMPERATURE = {
        "baseline": 36.8,
        "unit": "°C",
        "range": [32, 42],
        "critical_low": 32,
        "critical_high": 40,
    }


class LaboratoryConfig:
    """Configuration for laboratory parameters"""
    
    # Lactate (mmol/L)
    LACTATE = {
        "baseline": 1.0,
        "unit": "mmol/L",
        "range": [0.5, 20],
        "normal_range": [0.5, 2.0],
        "elevated": 2.0,
        "severe": 4.0,
    }
    
    # pH (arterial blood gas)
    PH = {
        "baseline": 7.40,
        "unit": "pH",
        "range": [6.8, 7.8],
        "normal_range": [7.35, 7.45],
        "acidosis": 7.35,
        "alkalosis": 7.45,
    }
    
    # Creatinine (mg/dL)
    CREATININE = {
        "baseline": 0.9,
        "unit": "mg/dL",
        "range": [0.6, 5.0],
        "normal_range": [0.6, 1.2],
        "acute_kidney_injury": 1.5,
    }
    
    # Glucose (mg/dL)
    GLUCOSE = {
        "baseline": 100,
        "unit": "mg/dL",
        "range": [40, 400],
        "normal_range": [70, 120],
        "hyperglycemia": 180,
        "hypoglycemia": 70,
    }


class ClinicalScenarios:
    """Clinical scenario parameters and progressions"""
    
    # Timeline markers (hours)
    SEPSIS_TIMELINE = {
        "T+0": "Normal baseline",
        "T+2": "Early signs (fever, tachycardia)",
        "T+4": "Hypotension, hypoxemia",
        "T+6": "Severe sepsis/septic shock",
        "T+8": "Multi-organ failure",
    }
    
    ARREST_TIMELINE = {
        "T-10min": "Prodromal phase (chest pain, dyspnea)",
        "T+0": "Collapse/arrest event",
        "T+1": "CPR initiated",
        "T+4": "Consider termination of resuscitation",
        "T+6": "Neurological damage risk increases",
    }
    
    RESPIRATORY_TIMELINE = {
        "T+0": "Normal baseline",
        "T+1h": "Mild hypoxemia (SpO2 94%)",
        "T+3h": "Moderate hypoxemia (SpO2 88%)",
        "T+6h": "Severe hypoxemia + muscle fatigue",
    }


class AlertThresholds:
    """Alert thresholds and severity levels"""
    
    # Severity levels
    SEVERITY_LEVELS = {
        "INFO": 1,
        "WARNING": 2,
        "ALERT": 3,
        "CRITICAL": 4,
    }
    
    # NEWS2 Score thresholds
    NEWS2_THRESHOLDS = {
        "low_risk": (0, 4),
        "medium_risk": (5, 6),
        "high_risk": (7, float('inf')),
    }
    
    # qSOFA thresholds
    QSOFA_THRESHOLDS = {
        "low_risk": (0, 1),
        "medium_risk": 2,
        "high_risk": 3,
    }
    
    # CART score thresholds
    CART_THRESHOLDS = {
        "low_risk": (0, 2),
        "medium_risk": (3, 4),
        "high_risk": (5, float('inf')),
    }


class DataGenerationConfig:
    """Configuration for synthetic data generation"""
    
    # Noise and variability
    NOISE_LEVELS = {
        "heart_rate": 2,      # ±2 bpm
        "systolic_bp": 3,     # ±3 mmHg
        "respiratory_rate": 1, # ±1 breaths/min
        "spo2": 1,            # ±1%
        "temperature": 0.3,   # ±0.3°C
    }
    
    # Correlation strengths
    CORRELATIONS = {
        "hypoxia_tachycardia": 0.15,      # +15% HR for SpO2 < 94%
        "hypotension_tachycardia": 0.20,  # +20% HR for SBP < 90
        "hypoxia_tachypnea": 8,           # +8 breaths/min
        "shock_altered_mental": True,      # Boolean: occurs or not
    }
    
    # Number of synthetic patients
    DEFAULT_PATIENTS_PER_SCENARIO = 100
    DEFAULT_SAMPLING_INTERVAL = 300  # 5 minutes in seconds


class SystemConfig:
    """General system configuration"""
    
    # File paths
    PROJECT_ROOT = Path(__file__).parent.parent
    DATA_DIR = PROJECT_ROOT / "data"
    SYNTHETIC_DATA_DIR = DATA_DIR / "synthetic_patients"
    REFERENCE_DATA_DIR = DATA_DIR / "reference"
    MODELS_DIR = DATA_DIR / "models"
    LOGS_DIR = PROJECT_ROOT / "logs"
    
    # Database (for future use)
    DB_HOST = "localhost"
    DB_PORT = 5432
    DB_NAME = "virtual_icu"
    DB_USER = "icu_user"
    
    # Streamlit settings
    STREAMLIT_PORT = 8501
    STREAMLIT_HOST = "0.0.0.0"
    
    # Logging
    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Cache settings
    CACHE_TTL = 3600  # 1 hour in seconds


# Clinical Reference Data
CLINICAL_GUIDELINES = {
    "sepsis": {
        "definition": "SIRS + suspected or confirmed infection",
        "reference": "Sepsis-3 Consensus (Singer et al., 2016)",
        "bundle": [
            "Lactate measurement",
            "Blood cultures before antibiotics",
            "Broad-spectrum antibiotics (< 3 hours)",
            "Fluid resuscitation (30 mL/kg in first 3 hours)",
            "Vasopressors for hypotension (MAP ≥ 65 mmHg)"
        ]
    },
    "respiratory_failure": {
        "definition": "PaO₂ < 60 mmHg (Type 1) or PaCO₂ > 50 mmHg (Type 2)",
        "reference": "ACCP Guidelines",
        "interventions": [
            "Oxygen therapy (nasal cannula → mask → CPAP → intubation)",
            "Ventilator modes (PEEP titration)",
            "Weaning parameters (SBT, RSBI)"
        ]
    },
    "cardiac_arrest": {
        "definition": "Loss of effective perfusion",
        "reference": "AHA ACLS Guidelines 2020",
        "interventions": [
            "High-quality CPR (100-120 compressions/min)",
            "Early defibrillation (< 3 min from collapse)",
            "Medication: Epinephrine 1 mg IV q3-5 min",
            "Amiodarone 300 mg for VF/VT"
        ]
    }
}


def get_config() -> Dict[str, Any]:
    """
    Get complete configuration dictionary
    
    Returns:
        Dict[str, Any]: Configuration dictionary
    """
    return {
        "vital_signs": VitalSignsConfig.__dict__,
        "laboratory": LaboratoryConfig.__dict__,
        "scenarios": ClinicalScenarios.__dict__,
        "alerts": AlertThresholds.__dict__,
        "data_generation": DataGenerationConfig.__dict__,
        "system": SystemConfig.__dict__,
        "guidelines": CLINICAL_GUIDELINES,
    }


if __name__ == "__main__":
    # Print configuration for debugging
    import json
    config = get_config()
    print(json.dumps(config, indent=2, default=str))
