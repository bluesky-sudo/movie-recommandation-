# routes/recommendations.py
from fastapi import APIRouter

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])

@router.get("/")
def get_recommendations():
    return {"message": "Recommendations route working"}

