"""
Virtual ICU v2.0 - LSTM Predictive Model
24-hour patient deterioration forecast
"""

import numpy as np
import pandas as pd
from typing import Dict, Tuple, List
import logging

logger = logging.getLogger(__name__)


class LSTMPredictor:
    """
    LSTM-based predictor for patient deterioration
    Forecasts vital signs 24 hours ahead
    """
    
    def __init__(self, lookback_window: int = 12):
        """
        Initialize LSTM predictor
        
        Args:
            lookback_window: Number of past timesteps to use (default 12 = 2 hours at 10-min intervals)
        """
        self.lookback_window = lookback_window
        self.models = {}  # Placeholder for actual LSTM models
        self.scaler_params = {}  # Min/max for normalization
        
    def _normalize(self, value: float, vital: str) -> float:
        """Normalize vital sign to 0-1 range"""
        ranges = {
            'heart_rate': (30, 200),
            'systolic_bp': (60, 180),
            'respiratory_rate': (6, 40),
            'spo2': (70, 100),
            'temperature': (35, 42),
        }
        
        if vital not in ranges:
            return value
        
        min_val, max_val = ranges[vital]
        normalized = (value - min_val) / (max_val - min_val)
        return np.clip(normalized, 0, 1)
    
    def _denormalize(self, normalized: float, vital: str) -> float:
        """Denormalize vital sign back to original range"""
        ranges = {
            'heart_rate': (30, 200),
            'systolic_bp': (60, 180),
            'respiratory_rate': (6, 40),
            'spo2': (70, 100),
            'temperature': (35, 42),
        }
        
        if vital not in ranges:
            return normalized
        
        min_val, max_val = ranges[vital]
        return normalized * (max_val - min_val) + min_val
    
    def prepare_sequences(self, vitals_history: List[Dict]) -> np.ndarray:
        """
        Prepare sequences for LSTM prediction
        
        Args:
            vitals_history: List of vital sign dictionaries
        
        Returns:
            Normalized sequence array
        """
        vitals_to_track = ['heart_rate', 'systolic_bp', 'respiratory_rate', 'spo2', 'temperature']
        
        # Create matrix of vitals
        sequence = []
        for vitals in vitals_history[-self.lookback_window:]:
            row = [self._normalize(vitals.get(vital, 0), vital) for vital in vitals_to_track]
            sequence.append(row)
        
        # Pad if necessary
        while len(sequence) < self.lookback_window:
            sequence.insert(0, sequence[0] if sequence else [0.5] * len(vitals_to_track))
        
        return np.array(sequence)
    
    def forecast_heuristic(self, vitals_history: List[Dict], 
                          hours_ahead: int = 24) -> Dict:
        """
        Heuristic-based forecast (v2.0 - placeholder for LSTM)
        
        Analyzes trends and predicts 24-hour trajectory
        
        Args:
            vitals_history: List of recent vital measurements
            hours_ahead: Hours to forecast (default 24)
        
        Returns:
            Forecast dictionary with predictions and confidence
        """
        
        if len(vitals_history) < 3:
            return {
                'status': 'insufficient_data',
                'message': 'Need at least 3 measurements for forecast',
                'confidence': 0.0
            }
        
        # Extract recent vitals
        recent = vitals_history[-10:]  # Last 10 measurements
        
        # Calculate trends
        trends = self._calculate_trends(recent)
        
        # Forecast using trends
        forecast_points = self._generate_forecast_points(recent[-1], trends, hours_ahead)
        
        # Predict deterioration risk
        deterioration_risk = self._assess_deterioration_risk(forecast_points)
        
        # Calculate confidence
        confidence = min(0.95, len(vitals_history) / 100)
        
        return {
            'status': 'success',
            'forecast_points': forecast_points,
            'deterioration_risk': deterioration_risk,
            'trend_analysis': trends,
            'confidence': confidence,
            'hours_ahead': hours_ahead,
            'recommendations': self._generate_recommendations(deterioration_risk)
        }
    
    def _calculate_trends(self, vitals_history: List[Dict]) -> Dict[str, float]:
        """Calculate slope trends for each vital"""
        vitals_to_track = ['heart_rate', 'systolic_bp', 'respiratory_rate', 'spo2', 'temperature']
        trends = {}
        
        for vital in vitals_to_track:
            values = [v.get(vital, 0) for v in vitals_history]
            
            if len(values) < 2:
                trends[vital] = 0.0
                continue
            
            # Calculate linear trend (change per measurement)
            x = np.arange(len(values))
            y = np.array(values)
            
            # Remove NaN values
            mask = ~np.isnan(y)
            if mask.sum() < 2:
                trends[vital] = 0.0
                continue
            
            x = x[mask]
            y = y[mask]
            
            # Linear regression
            try:
                slope = np.polyfit(x, y, 1)[0]
                trends[vital] = float(slope)
            except:
                trends[vital] = 0.0
        
        return trends
    
    def _generate_forecast_points(self, current_vitals: Dict, 
                                 trends: Dict[str, float], 
                                 hours_ahead: int) -> List[Dict]:
        """Generate forecast points for next N hours"""
        vitals_to_track = ['heart_rate', 'systolic_bp', 'respiratory_rate', 'spo2', 'temperature']
        forecast_points = []
        
        # Assume measurements every 10 minutes
        measurements_per_hour = 6
        total_measurements = hours_ahead * measurements_per_hour
        
        current = {vital: current_vitals.get(vital, 0) for vital in vitals_to_track}
        
        for i in range(total_measurements):
            # Apply trend with decay (uncertainty increases)
            decay_factor = 1 - (i / total_measurements) * 0.3  # Decay over time
            
            forecast_point = {}
            for vital in vitals_to_track:
                new_value = current[vital] + trends[vital] * decay_factor
                
                # Apply physiological bounds
                bounds = {
                    'heart_rate': (30, 200),
                    'systolic_bp': (60, 180),
                    'respiratory_rate': (6, 40),
                    'spo2': (70, 100),
                    'temperature': (35, 42),
                }
                
                min_val, max_val = bounds.get(vital, (0, 1000))
                new_value = np.clip(new_value, min_val, max_val)
                
                forecast_point[vital] = float(new_value)
                current[vital] = new_value
            
            # Add timestamp (relative hours)
            forecast_point['hours_from_now'] = (i + 1) / measurements_per_hour
            forecast_points.append(forecast_point)
        
        return forecast_points
    
    def _assess_deterioration_risk(self, forecast_points: List[Dict]) -> Dict:
        """Assess risk of patient deterioration in forecast period"""
        
        if not forecast_points:
            return {'risk_level': 'unknown', 'probability': 0.0}
        
        # Extract endpoints
        first = forecast_points[0]
        last = forecast_points[-1]
        
        risk_factors = 0
        max_risk_factors = 5
        
        # Factor 1: Increasing heart rate
        if last.get('heart_rate', 0) > first.get('heart_rate', 0) + 20:
            risk_factors += 1
        
        # Factor 2: Decreasing SpO2
        if last.get('spo2', 100) < first.get('spo2', 100) - 5:
            risk_factors += 1
        
        # Factor 3: Decreasing blood pressure
        if last.get('systolic_bp', 120) < first.get('systolic_bp', 120) - 20:
            risk_factors += 1
        
        # Factor 4: Increasing respiratory rate
        if last.get('respiratory_rate', 16) > first.get('respiratory_rate', 16) + 5:
            risk_factors += 1
        
        # Factor 5: Temperature changes (fever or hypothermia)
        temp_change = abs(last.get('temperature', 37) - first.get('temperature', 37))
        if temp_change > 1.5:
            risk_factors += 1
        
        # Calculate probability
        probability = risk_factors / max_risk_factors
        
        # Determine risk level
        if probability < 0.2:
            risk_level = 'Low'
        elif probability < 0.5:
            risk_level = 'Medium'
        elif probability < 0.8:
            risk_level = 'High'
        else:
            risk_level = 'Critical'
        
        return {
            'risk_level': risk_level,
            'probability': float(probability),
            'risk_factors_present': risk_factors,
            'max_risk_factors': max_risk_factors
        }
    
    def _generate_recommendations(self, deterioration_risk: Dict) -> List[str]:
        """Generate recommendations based on forecast"""
        recommendations = []
        risk_level = deterioration_risk.get('risk_level', 'Low')
        
        if risk_level == 'Low':
            recommendations.append("✅ Continue routine monitoring")
        
        elif risk_level == 'Medium':
            recommendations.append("🟡 Increase monitoring frequency")
            recommendations.append("🟡 Review medication compliance")
            recommendations.append("🟡 Ensure adequate hydration")
        
        elif risk_level == 'High':
            recommendations.append("🔴 Increase to continuous monitoring")
            recommendations.append("🔴 Consider escalation to ICU")
            recommendations.append("🔴 Prepare for intervention")
            recommendations.append("🔴 Notify physician immediately")
        
        else:  # Critical
            recommendations.append("🔴🔴 CRITICAL: Immediate physician notification")
            recommendations.append("🔴🔴 Prepare for advanced interventions")
            recommendations.append("🔴🔴 Consider ICU/Emergency Department")
        
        return recommendations


class DeteriortationDetector:
    """
    Real-time detector for acute patient deterioration
    Identifies dangerous changes within hours
    """
    
    def __init__(self, alert_threshold: float = 0.7):
        """
        Initialize deterioration detector
        
        Args:
            alert_threshold: Probability threshold for alerts (0-1)
        """
        self.alert_threshold = alert_threshold
    
    def detect(self, current_vitals: Dict, 
               previous_vitals: Dict = None,
               hours_since_last: float = 1.0) -> Dict:
        """
        Detect signs of acute deterioration
        
        Args:
            current_vitals: Current vital signs
            previous_vitals: Previous vital signs (optional)
            hours_since_last: Time elapsed (hours)
        
        Returns:
            Detection results with alerts
        """
        
        alerts = []
        deterioration_score = 0
        max_score = 10
        
        # Critical value checks
        critical_checks = {
            'heart_rate': [('>', 180), ('<', 40)],
            'systolic_bp': [('>', 180), ('<', 90)],
            'respiratory_rate': [('>', 40), ('<', 6)],
            'spo2': [('<', 88)],
            'temperature': [('>', 40), ('<', 35)],
        }
        
        for vital, conditions in critical_checks.items():
            value = current_vitals.get(vital, 0)
            
            for op, threshold in conditions:
                triggered = False
                if op == '>' and value > threshold:
                    triggered = True
                elif op == '<' and value < threshold:
                    triggered = True
                
                if triggered:
                    alerts.append({
                        'severity': 'Critical',
                        'vital': vital,
                        'value': value,
                        'threshold': threshold,
                        'message': f'{vital} {threshold} {threshold}'
                    })
                    deterioration_score += 3
        
        # Trend analysis (if previous vitals available)
        if previous_vitals:
            deterioration_score += self._analyze_trends(
                current_vitals, previous_vitals, hours_since_last
            )
        
        # Calculate deterioration probability
        deterioration_probability = min(1.0, deterioration_score / max_score)
        
        # Determine alert status
        alert_status = 'Normal'
        if deterioration_probability >= self.alert_threshold:
            alert_status = 'ALERT'
        elif deterioration_probability >= 0.5:
            alert_status = 'Warning'
        
        return {
            'alert_status': alert_status,
            'deterioration_probability': float(deterioration_probability),
            'deterioration_score': int(deterioration_score),
            'alerts': alerts,
            'action_required': alert_status == 'ALERT'
        }
    
    def _analyze_trends(self, current: Dict, previous: Dict, hours: float) -> int:
        """Analyze trends and return score"""
        score = 0
        
        vitals_to_check = ['heart_rate', 'systolic_bp', 'respiratory_rate', 'spo2']
        
        for vital in vitals_to_check:
            curr = current.get(vital, 0)
            prev = previous.get(vital, 0)
            
            if prev == 0:
                continue
            
            change = curr - prev
            change_per_hour = change / max(hours, 0.1)
            
            # Thresholds for concerning changes
            if vital == 'heart_rate' and change_per_hour > 30:
                score += 2  # Rapid tachycardia
            elif vital == 'systolic_bp' and change_per_hour < -15:
                score += 2  # Rapid BP drop
            elif vital == 'respiratory_rate' and change_per_hour > 10:
                score += 1  # Rapid RR increase
            elif vital == 'spo2' and change_per_hour < -3:
                score += 2  # Rapid desaturation
        
        return score


# ════════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ════════════════════════════════════════════════════════════════════

def create_forecast_plot_data(forecast_points: List[Dict]) -> Dict:
    """Create data suitable for Plotly visualization"""
    
    if not forecast_points:
        return {}
    
    vitals_to_plot = ['heart_rate', 'systolic_bp', 'respiratory_rate', 'spo2']
    
    plot_data = {}
    
    for vital in vitals_to_plot:
        hours = [p.get('hours_from_now', 0) for p in forecast_points]
        values = [p.get(vital, 0) for p in forecast_points]
        
        plot_data[vital] = {
            'hours': hours,
            'values': values
        }
    
    return plot_data
