# VitalCare Admin Analytics Dashboard — Backend

Python backend for the VitalCare Admin Analytics Dashboard, built with **FastAPI** and **SQLAlchemy**. It provides REST APIs to retrieve healthcare operations analytics from **Databricks Lakebase PostgreSQL**.

## Tech Stack

- **Python** — Backend programming language
- **FastAPI** — REST API framework
- **Uvicorn** — ASGI application server
- **SQLAlchemy** — Database connectivity and SQL execution
- **Psycopg 3** — PostgreSQL database driver
- **Pydantic Settings** — Environment-based configuration
- **Databricks Lakebase PostgreSQL** — Analytics data source

## Project Structure

```text
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── dashboard.py
│   │   ├── trends.py
│   │   ├── facilities.py
│   │   ├── routing.py
│   │   └── alerts.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   └── session.py
│   ├── schemas/
│   └── services/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Features

- Dashboard overview metrics and KPIs
- Daily consultation trends
- Facility performance analytics
- Routing tier performance analytics
- Operational alerts and severity information
- Database connectivity checks
- Interactive API documentation through Swagger UI
- Environment-based configuration
- CORS support for the local React frontend

## API Endpoints

Base URL for local development: `http://localhost:8000`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Checks API health |
| GET | `/api/dashboard/overview` | Retrieves dashboard overview metrics |
| GET | `/api/dashboard/trends` | Retrieves daily consultation trends |
| GET | `/api/dashboard/facilities` | Retrieves facility performance |
| GET | `/api/dashboard/routing` | Retrieves routing tier metrics |
| GET | `/api/dashboard/alerts` | Retrieves operational alerts |

### API Documentation

When the backend is running, access:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- Health check: `http://localhost:8000/api/health`

## Prerequisites

- Python 3.9 or a compatible Python version
- Access to the Databricks workspace and Lakebase PostgreSQL instance
- A valid Lakebase authentication token
- Git

## Local Setup

### 1. Navigate to the backend

```bash
cd backend
```

### 2. Create a virtual environment

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a local `.env` file in the `backend/` directory.

```dotenv
DATABASE_URL=postgresql://YOUR_DATABASE_USERNAME@YOUR_LAKEBASE_HOST/databricks_postgres?sslmode=require
LAKEBASE_ACCESS_TOKEN=YOUR_VALID_LAKEBASE_OAUTH_TOKEN
```

Replace the example values with your actual Lakebase connection details and valid authentication token.

**Security:** Never commit `.env` or share database credentials and OAuth tokens. The `.env` file must be excluded through `.gitignore`.

### 5. Start the development server

From the `backend/` directory, with the virtual environment activated:

```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at:

```text
http://localhost:8000
```

The `--reload` option automatically restarts the development server when application files change.

## Database Integration

The backend connects to Databricks Lakebase PostgreSQL using SQLAlchemy and Psycopg.

Dashboard data is retrieved from the following database views in the `vitalcare` schema:

- `v_dashboard_overview`
- `v_daily_consultation_trends`
- `v_facility_performance`
- `v_routing_performance`
- `v_operational_alerts`

The API reads from these views and returns JSON responses to the React frontend.

### Authentication

Local development currently uses a Lakebase OAuth access token supplied through environment configuration. These tokens may expire, so refresh the token when necessary.

For deployment, configure the supported Databricks Apps authentication and Lakebase access mechanism instead of relying on a manually copied, short-lived local token.

## Frontend Integration

The React frontend runs locally on port `5173` and calls the FastAPI backend on port `8000`.

The backend must allow the frontend origin through FastAPI CORS middleware.

For local development, the frontend origin is:

```text
http://localhost:5173
```

Only configure the origins required by your environment. Production origins should be configured separately.

## Error Handling

The API endpoints return JSON responses and use appropriate HTTP status codes.

- `200 OK` — Request completed successfully
- `404 Not Found` — Requested overview data is unavailable
- `500 Internal Server Error` — A database query or other handled database operation failed

Detailed database exceptions should be logged securely on the server rather than exposed to API clients.

## Development Notes

- Keep API routes organized under `app/api/`.
- Keep database connection logic in `app/db/`.
- Store configuration in environment variables.
- Avoid hardcoding credentials or access tokens.
- Validate API responses before changing frontend TypeScript interfaces.
- Keep synthetic demonstration data clearly distinguished from production healthcare data.

## License

Add the appropriate license information when the project license is finalized.