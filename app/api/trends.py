
from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import engine

router = APIRouter(prefix="/api/dashboard", tags=["Dashboard Trends"])


@router.get("/trends")
def get_daily_consultation_trends():
    query = text("""
        SELECT *
        FROM vitalcare.v_daily_consultation_trends
        ORDER BY 1
    """)

    try:
        with engine.connect() as connection:
            result = connection.execute(query).mappings().all()
            return [dict(row) for row in result]

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Unable to retrieve daily consultation trends",
        )
