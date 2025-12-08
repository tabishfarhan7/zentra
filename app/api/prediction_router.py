from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.predict import PredictionRequest, PredictionResponse
from app.db.database import get_db
from app.core.dependencies import get_current_user
from app.db import models

from app.ml.inference_pipeline import predict_obesity

router = APIRouter(prefix="/predict", tags=["Predictions"])

@router.post("/", response_model=PredictionResponse)
def predict_endpoint(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    # 1. Fetch user health profile
    profile = (
        db.query(models.UserHealthProfile)
        .filter(models.UserHealthProfile.user_id == current_user.id)
        .first()
    )

    if not profile:
        raise HTTPException(
            status_code=400,
            detail="Health profile not found. Please create your profile first."
        )

    # 2. Convert SQLAlchemy model → dict for inference pipeline
    user_input = {
        "gender": profile.gender,
        "age": profile.age,
        "height_m": profile.height_m,
        "weight_kg": profile.weight_kg,
        "bmi": profile.bmi,  # optional, depends on pipeline

        "family_overweight_history": profile.family_overweight_history,
        "high_calorie_food": profile.high_calorie_food,

        "vegetable_intake_freq": profile.vegetable_intake_freq,
        "main_meals_per_day": profile.main_meals_per_day,

        "snack_frequency": profile.snack_frequency,
        "smokes": profile.smokes,

        "water_intake_liters": profile.water_intake_liters,
        "calorie_tracking": profile.calorie_tracking,

        "physical_activity_hours": profile.physical_activity_hours,
        "screentime_hours": profile.screentime_hours,

        "alcohol_consumption": profile.alcohol_consumption,
        "travel_mode": profile.travel_mode,
    }

    # 3. Run the ML model
    prediction_label = predict_obesity(user_input)

    # 4. Store prediction history
    record = models.PredictionHistory(
        user_id=current_user.id,
        input_data=str(user_input),
        prediction=prediction_label
    )

    db.add(record)
    db.commit()

    return PredictionResponse(obesity_level=prediction_label)
