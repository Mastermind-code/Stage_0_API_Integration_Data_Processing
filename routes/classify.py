from fastapi import APIRouter
from fastapi.responses import JSONResponse
from datetime import datetime, timezone
from services.gendarize import fetch_user_data





router = APIRouter()

@router.get("/api/classify")
async def classify_name(name: str = None):
    
    # 1. Validation — fill these in
    if not name:  # missing or empty
        return JSONResponse(status_code=400, content={"status": "error", "message": "Name is required"})
    
    if not name.isalpha():  # not a valid string (contains non-letter characters)
        return JSONResponse(status_code=422, content={"status": "error", "message": "Invalid name format"})
    
    # 2. Call Genderize
    data, error = await fetch_user_data(name)
    
    if error:
        return JSONResponse(status_code=502, content={"status": "error", "message": error})
    
    # 3. Process — fill these in
    sample_size = data.get("count")  # rename count
    is_confident = (data.get("probability", 0) >= 0.7) and (sample_size >= 100)  # probability >= 0.7 AND sample_size >= 100
    processed_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # 4. Return success response
    return {
        "status": "success",
        "data": {
            "name": data.get("name"),
            "gender": data.get("gender"),
            "probability": data.get("probability"),
            "sample_size": sample_size,
            "is_confident": is_confident,
            "processed_at": processed_at
        }
    }
