
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.dashboard import router as dashboard_router
from app.api.trends import router as trends_router
from app.api.facilities import router as facilities_router
from app.api.routing import router as routing_router
from app.api.alerts import router as alerts_router

app = FastAPI(
    title="VitalCare Admin API",
    description="Backend APIs for the VitalCare Admin Analytics Dashboard",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "service": "vitalcare-admin-api",
        "message": "VitalCare Admin API is running",
    }


app.include_router(dashboard_router)
app.include_router(trends_router)
app.include_router(facilities_router)
app.include_router(routing_router)
app.include_router(alerts_router)