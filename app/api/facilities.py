
from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import engine

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard Facilities"],
)


@router.get("/facilities")
def get_facility_performance():
    query = text("""
        SELECT *
        FROM vitalcare.v_facility_performance
        ORDER BY 1
    """)

    try:
        with engine.connect() as connection:
            result = connection.execute(query).mappings().all()
            return [dict(row) for row in result]

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Unable to retrieve facility performance",
        )