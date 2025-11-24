from pydantic import BaseModel

class PredictionRequest(BaseModel):
    gender: str = "Female"
    age: float = 25.0
    height_m: float = 1.65
    weight_kg: float = 65.0
    
    family_overweight_history: str = "no"
    high_calorie_food: str = "no"
    
    vegetable_intake_freq: float = 2.0
    main_meals_per_day: float = 3.0
    
    snack_frequency: str = "Sometimes"  # matches dataset
    smokes: str = "no"
    
    water_intake_liters: float = 2.0
    calorie_tracking: str = "no"
    
    physical_activity_hours: float = 0.5
    screentime_hours: float = 4.0
    
    alcohol_consumption: str = "no"
    travel_mode: str = "Public_Transportation"
    
    


class PredictionResponse(BaseModel):
    prediction: str
