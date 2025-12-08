from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.database import get_db
from app.db import models
from app.schemas.profile import ProfileCreateRequest, ProfileUpdateRequest, ProfileResponse

router = APIRouter(prefix="/profile", tags=["User Profile"])


# -----------------------------
# Utility — BMI Calculator
# -----------------------------
def calculate_bmi(weight_kg: float, height_m: float):
    if height_m <= 0:
        return 0
    return round(weight_kg / (height_m ** 2), 2)


# -----------------------------
# CREATE USER PROFILE
# -----------------------------
@router.post("/create", response_model=ProfileResponse)
def create_profile(
    data: ProfileCreateRequest,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    # Check if profile already exists
    existing = db.query(models.UserHealthProfile).filter(
        models.UserHealthProfile.user_id == current_user.id
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Profile already exists. Use update endpoint."
        )

    # Compute BMI
    bmi_value = calculate_bmi(data.weight_kg, data.height_m)

    profile = models.UserHealthProfile(
        user_id=current_user.id,
        gender=data.gender,
        age=data.age,
        height_m=data.height_m,
        weight_kg=data.weight_kg,
        bmi=bmi_value,

        family_overweight_history=data.family_overweight_history,
        high_calorie_food=data.high_calorie_food,
        vegetable_intake_freq=data.vegetable_intake_freq,
        main_meals_per_day=data.main_meals_per_day,
        snack_frequency=data.snack_frequency,
        smokes=data.smokes,
        water_intake_liters=data.water_intake_liters,
        calorie_tracking=data.calorie_tracking,
        physical_activity_hours=data.physical_activity_hours,
        screentime_hours=data.screentime_hours,
        alcohol_consumption=data.alcohol_consumption,
        travel_mode=data.travel_mode
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile


# -----------------------------
# UPDATE USER PROFILE
# -----------------------------
@router.put("/update", response_model=ProfileResponse)
def update_profile(
    data: ProfileUpdateRequest,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    profile = db.query(models.UserHealthProfile).filter(
        models.UserHealthProfile.user_id == current_user.id
    ).first()

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    # Update only the fields provided by user
    update_data = data.dict(exclude_unset=True)

    for field, value in update_data.items():
        setattr(profile, field, value)

    # Recalculate BMI if height or weight changed
    if "weight_kg" in update_data or "height_m" in update_data:
        profile.bmi = calculate_bmi(profile.weight_kg, profile.height_m)

    db.commit()
    db.refresh(profile)

    return profile


# -----------------------------
# GET CURRENT USER PROFILE
# -----------------------------
@router.get("/me", response_model=ProfileResponse)
def get_profile(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    profile = db.query(models.UserHealthProfile).filter(
        models.UserHealthProfile.user_id == current_user.id
    ).first()

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not created yet")

    return profile
