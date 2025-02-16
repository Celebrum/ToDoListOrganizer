from enum import Enum


class HealthcareContext(Enum):
    CARDIOPULMONARY = "cardiopulmonary"
    NEUROLOGY = "neurology"
    PSYCHIATRY = "psychiatry"
    IMMUNOLOGY = "immunology"
    DIABETES = "diabetes"
    EPIDEMIOLOGY = "epidemiology"

class ClinicalPriority(Enum):
    URGENT = "urgent"
    HIGH = "high"
    MODERATE = "moderate"
    ROUTINE = "routine"

class ResearchDomain(Enum):
    MEDICAL_DEVICE = "medical_device"
    PHARMACEUTICAL = "pharmaceutical"
    VACCINE = "vaccine"
    HEALTH_ECONOMICS = "health_economics"
    HEALTH_POLICY = "health_policy"
    DECISION_SCIENCE = "decision_science"

class HealthcareProfessional:
    def __init__(self, name, role, specialties=None):
        self.name = name
        self.role = role
        self.specialties = specialties or []
