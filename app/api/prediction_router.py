from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.predict import PredictionRequest, PredictionResponse
from app.db.database import get_db
from app.core.dependencies import get_current_user
from app.db import models

from app.ml.inference_pipeline import predict_obesity

router = APIRouter(prefix="/predict", tags=["Predictions"])

@router.post("/")
def predict_endpoint(req : PredictionRequest, db: Session=Depends(get_db),current_user:models.User=Depends(get_current_user))->str:
    
    try:
        prediction_label = predict_obesity(req.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"model error: {str(e)}")
    
    record=models.PredictionHistory(
        user_id=current_user.id,
        input_data=req.json(),
        prediction=prediction_label
    )
    
    db.add(record)
    db.commit()
    db.refresh(record)
    return prediction_label
    
    
