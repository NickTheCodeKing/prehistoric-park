from enum import Enum

class Sex(str, Enum):
    male = "male"
    female = "female"
    herm = "herm"
    other = "other"

class CautionLevel(str, Enum):
    none = "none"
    low = "low"
    medium = "medium"
    high = "high"
