from fastapi import APIRouter, HTTPException, Depends
from models.user import UserCreate, UserLogin, UserResponse
from services.db import user_collection
from auth.jwt_handler import hash_password, verify_password, sign_jwt, get_current_user
from datetime import datetime

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/signup")
async def signup(user: UserCreate):
    from fastapi.responses import JSONResponse
    try:
        existing_user = await user_collection.find_one({"email": user.email})
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        hashed_pass = hash_password(user.password)
        new_user = {
            "name": user.name,
            "email": user.email,
            "password": hashed_pass,
            "created_at": datetime.utcnow()
        }
        
        result = await user_collection.insert_one(new_user)
        return {"message": "User created successfully", "user_id": str(result.inserted_id)}
    except HTTPException:
        raise
    except Exception as e:
        print(f"Server error during signup: {e}")
        return JSONResponse(status_code=500, content={"detail": f"Internal Server Error: {str(e)}"})

@router.post("/login")
async def login(user: UserLogin):
    from fastapi.responses import JSONResponse
    try:
        db_user = await user_collection.find_one({"email": user.email})
        if not db_user or not verify_password(user.password, db_user["password"]):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        return sign_jwt(str(db_user["_id"]))
    except HTTPException:
        raise
    except Exception as e:
        print(f"Server error during login: {e}")
        return JSONResponse(status_code=500, content={"detail": f"Internal Server Error: {str(e)}"})

@router.get("/me")
async def get_me(user_id: str = Depends(get_current_user)):
    from bson import ObjectId
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return UserResponse(
        id=str(user["_id"]),
        name=user["name"],
        email=user["email"],
        created_at=user["created_at"]
    )
