from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from routes.auth import router as auth_router
from routes.dashboard import router as dashboard_router
from routes.wizard import router as wizard_router
from routes.mfxray import router as mfxray_router

load_dotenv()

app = FastAPI(title="MintMind API")

# Setup CORS properly
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

# Register routes
app.include_router(auth_router)
app.include_router(dashboard_router)
app.include_router(wizard_router)
app.include_router(mfxray_router)

# Serve the static files
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    # Setup for production readiness
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
