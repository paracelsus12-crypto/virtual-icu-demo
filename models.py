"""
Virtual ICU v2 - Data Models with Pydantic Validation
Валідація всіх вхідних даних для забезпечення типу безпеки
"""

from pydantic import BaseModel, Field, validator
from typing import Optional, Dict, Any
from enum import Enum


class AlertStatus(str, Enum):
    """Alert status levels"""
    ALERT = "Alert"
    CONFUSED = "Confused"
    LETHARGIC = "Lethargic"
    UNRESPONSIVE = "Unresponsive"


class VitalsData(BaseModel):
    """Validated vital signs data model"""
    
    heart_rate: float = Field(..., gt=0, le=300, description="Heart rate in bpm")
    systolic_bp: float = Field(..., gt=0, le=300, description="Systolic BP in mmHg")
    diastolic_bp: Optional[float] = Field(None, gt=0, le=200, description="Diastolic BP in mmHg")
    respiratory_rate: float = Field(..., gt=0, le=100, description="Respiratory rate breaths/min")
    spo2: float = Field(..., ge=0, le=100, description="Oxygen saturation %")
    temperature: float = Field(..., ge=35.0, le=42.0, description="Temperature in °C")
    alert_status: AlertStatus = Field(default=AlertStatus.ALERT, description="Alert status")
    supplemental_oxygen: bool = Field(default=False, description="On supplemental oxygen")
    age: Optional[int] = Field(None, ge=0, le=120, description="Patient age")
    
    class Config:
        use_enum_values = True
    
    @validator('heart_rate')
    def validate_hr(cls, v):
        """Heart rate validation"""
        if not (20 < v < 300):
            raise ValueError('Heart rate must be between 20-300 bpm')
        return v
    
    @validator('respiratory_rate')
    def validate_rr(cls, v):
        """Respiratory rate validation"""
        if not (4 < v < 60):
            raise ValueError('RR must be between 4-60 breaths/min')
        return v
    
    @validator('spo2')
    def validate_spo2(cls, v):
        """SpO2 validation"""
        if not (0 <= v <= 100):
            raise ValueError('SpO2 must be between 0-100%')
        return v
    
    @validator('temperature')
    def validate_temp(cls, v):
        """Temperature validation"""
        if not (35.0 <= v <= 42.0):
            raise ValueError('Temperature must be between 35-42°C')
        return v


class NEWS2Score(BaseModel):
    """NEWS2 score output model"""
    total: int = Field(..., ge=0, le=20)
    components: Dict[str, int]
    risk_level: str  # "Low", "Medium", "High"
    max_possible: int = 20
    timestamp: Optional[str] = None


class qSOFAScore(BaseModel):
    """qSOFA score output model"""
    total: int = Field(..., ge=0, le=3)
    components: Dict[str, int]
    risk_level: str  # "Low", "High (Sepsis likely)"
    needs_investigation: bool
    max_possible: int = 3
    timestamp: Optional[str] = None


class CARTScore(BaseModel):
    """CART score output model"""
    total: int = Field(..., ge=0, le=20)
    risk_category: str  # "Low", "Medium", "High", "Highest"
    max_possible: int = 20
    percentile: float = Field(..., ge=0, le=100)
    timestamp: Optional[str] = None


class ClinicalRecommendation(BaseModel):
    """Single clinical recommendation"""
    priority: int = Field(..., ge=1, le=5, description="Priority 1-5 (1=highest)")
    action: str
    rationale: Optional[str] = None
    protocol_link: Optional[str] = None


class ClinicaRecommendations(BaseModel):
    """Complete clinical recommendations"""
    urgency: str  # "Low", "Medium", "High"
    recommendations: list[ClinicalRecommendation]
    summary: str


class PatientData(BaseModel):
    """Complete patient data model"""
    patient_id: str
    timestamp: str
    vitals: VitalsData
    news2: Optional[NEWS2Score] = None
    qsofa: Optional[qSOFAScore] = None
    cart: Optional[CARTScore] = None
    recommendations: Optional[ClinicaRecommendations] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "patient_id": "P001",
                "timestamp": "2024-04-24T09:00:00Z",
                "vitals": {
                    "heart_rate": 85,
                    "systolic_bp": 120,
                    "respiratory_rate": 16,
                    "spo2": 98,
                    "temperature": 37.0,
                    "alert_status": "Alert"
                }
            }
        }


class CSVValidationResult(BaseModel):
    """Result of CSV validation"""
    is_valid: bool
    required_columns: list[str]
    missing_columns: list[str]
    extra_columns: list[str]
    data_quality_issues: list[str]
    error_message: Optional[str] = None


# CSV Schema validation
REQUIRED_CSV_COLUMNS = {
    'heart_rate': float,
    'systolic_bp': float,
    'respiratory_rate': float,
    'spo2': float,
    'temperature': float,
}

OPTIONAL_CSV_COLUMNS = {
    'diastolic_bp': float,
    'alert_status': str,
    'supplemental_oxygen': bool,
    'age': int,
    'patient_id': str,
    'timestamp': str,
}


class CSVValidator:
    """CSV file validator"""
    
    @staticmethod
    def validate(df) -> CSVValidationResult:
        """Validate CSV dataframe"""
        required_cols = set(REQUIRED_CSV_COLUMNS.keys())
        actual_cols = set(df.columns)
        missing = list(required_cols - actual_cols)
        extra = list(actual_cols - required_cols - set(OPTIONAL_CSV_COLUMNS.keys()))
        
        issues = []
        
        # Check for missing values
        for col in REQUIRED_CSV_COLUMNS.keys():
            if col in df.columns and df[col].isna().any():
                issues.append(f"Column '{col}' has missing values")
        
        # Check data types
        for col, dtype in REQUIRED_CSV_COLUMNS.items():
            if col in df.columns:
                try:
                    pd.to_numeric(df[col])
                except:
                    issues.append(f"Column '{col}' is not numeric")
        
        # Check ranges
        if 'heart_rate' in df.columns:
            if (df['heart_rate'] < 20).any() or (df['heart_rate'] > 300).any():
                issues.append("Heart rate out of valid range (20-300)")
        
        is_valid = len(missing) == 0 and len(issues) == 0
        
        return CSVValidationResult(
            is_valid=is_valid,
            required_columns=list(required_cols),
            missing_columns=missing,
            extra_columns=extra,
            data_quality_issues=issues,
            error_message=None if is_valid else f"CSV validation failed: {len(issues)} issues"
        )


# Import pandas for type checking
import pandas as pd
