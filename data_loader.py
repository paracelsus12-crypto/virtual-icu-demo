"""
Virtual ICU v2 - Data Loader Component
Безпечне завантаження та валідація CSV файлів
"""

import pandas as pd
import streamlit as st
from typing import Tuple, Optional
import logging

logger = logging.getLogger(__name__)


class DataLoaderComponent:
    """Handle data loading with validation"""
    
    # Required columns for vital signs
    REQUIRED_COLUMNS = {
        'heart_rate',
        'systolic_bp',
        'respiratory_rate',
        'spo2',
        'temperature',
    }
    
    # Optional columns
    OPTIONAL_COLUMNS = {
        'diastolic_bp',
        'alert_status',
        'supplemental_oxygen',
        'age',
        'patient_id',
        'timestamp',
    }
    
    # Max file size (10 MB)
    MAX_FILE_SIZE = 10 * 1024 * 1024
    
    @classmethod
    def load_csv(cls, uploaded_file) -> Optional[pd.DataFrame]:
        """
        Safely load and validate CSV file
        
        Returns:
            DataFrame if valid, None if invalid
        """
        try:
            # Check file size
            if uploaded_file.size > cls.MAX_FILE_SIZE:
                st.error(f"❌ File too large. Max size: 10 MB")
                return None
            
            # Read CSV
            df = pd.read_csv(uploaded_file)
            
            # Validate structure
            is_valid, issues = cls.validate_structure(df)
            if not is_valid:
                for issue in issues:
                    st.error(f"❌ {issue}")
                return None
            
            # Validate data quality
            quality_issues = cls.validate_data_quality(df)
            if quality_issues:
                st.warning(f"⚠️ Data quality issues found:")
                for issue in quality_issues:
                    st.warning(f"  • {issue}")
            
            # Clean data
            df = cls.clean_data(df)
            
            st.success(f"✅ CSV loaded successfully: {len(df)} records, {len(df.columns)} columns")
            return df
            
        except pd.errors.ParserError as e:
            st.error(f"❌ CSV parsing error: {str(e)}")
            logger.error(f"CSV parse error: {e}")
            return None
        except Exception as e:
            st.error(f"❌ Error loading file: {str(e)}")
            logger.error(f"File load error: {e}")
            return None
    
    @classmethod
    def validate_structure(cls, df: pd.DataFrame) -> Tuple[bool, list]:
        """Validate CSV structure"""
        issues = []
        
        # Check for required columns
        missing_cols = cls.REQUIRED_COLUMNS - set(df.columns)
        if missing_cols:
            issues.append(f"Missing required columns: {', '.join(missing_cols)}")
        
        # Check for empty dataframe
        if df.empty:
            issues.append("CSV file is empty")
        
        # Check row count
        if len(df) > 100000:
            issues.append(f"Too many rows ({len(df)}). Max 100,000")
        
        return len(issues) == 0, issues
    
    @classmethod
    def validate_data_quality(cls, df: pd.DataFrame) -> list:
        """Validate data quality"""
        issues = []
        
        # Check for missing values in required columns
        for col in cls.REQUIRED_COLUMNS:
            if col in df.columns:
                missing_count = df[col].isna().sum()
                if missing_count > 0:
                    pct = (missing_count / len(df)) * 100
                    issues.append(f"Column '{col}': {missing_count} missing values ({pct:.1f}%)")
        
        # Validate vital signs ranges
        if 'heart_rate' in df.columns:
            out_of_range = ((df['heart_rate'] < 20) | (df['heart_rate'] > 300)).sum()
            if out_of_range > 0:
                issues.append(f"Heart rate: {out_of_range} values out of range (20-300)")
        
        if 'respiratory_rate' in df.columns:
            out_of_range = ((df['respiratory_rate'] < 4) | (df['respiratory_rate'] > 60)).sum()
            if out_of_range > 0:
                issues.append(f"RR: {out_of_range} values out of range (4-60)")
        
        if 'spo2' in df.columns:
            out_of_range = ((df['spo2'] < 0) | (df['spo2'] > 100)).sum()
            if out_of_range > 0:
                issues.append(f"SpO2: {out_of_range} values out of range (0-100)")
        
        if 'temperature' in df.columns:
            out_of_range = ((df['temperature'] < 35) | (df['temperature'] > 42)).sum()
            if out_of_range > 0:
                issues.append(f"Temperature: {out_of_range} values out of range (35-42°C)")
        
        return issues
    
    @classmethod
    def clean_data(cls, df: pd.DataFrame) -> pd.DataFrame:
        """Clean and standardize data"""
        df = df.copy()
        
        # Convert columns to proper types
        for col in cls.REQUIRED_COLUMNS:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Handle alert_status (standardize)
        if 'alert_status' in df.columns:
            df['alert_status'] = df['alert_status'].str.capitalize()
        
        # Handle supplemental_oxygen (convert to bool)
        if 'supplemental_oxygen' in df.columns:
            df['supplemental_oxygen'] = df['supplemental_oxygen'].astype(bool)
        
        # Fill missing age with default
        if 'age' not in df.columns:
            df['age'] = 65
        
        # Remove completely empty rows
        df = df.dropna(subset=cls.REQUIRED_COLUMNS, how='any')
        
        return df
    
    @classmethod
    def get_data_summary(cls, df: pd.DataFrame) -> dict:
        """Get summary statistics"""
        summary = {
            'total_records': len(df),
            'vital_means': {},
            'vital_ranges': {}
        }
        
        for col in cls.REQUIRED_COLUMNS:
            if col in df.columns:
                summary['vital_means'][col] = f"{df[col].mean():.1f}"
                summary['vital_ranges'][col] = f"{df[col].min():.1f}-{df[col].max():.1f}"
        
        return summary
