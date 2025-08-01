import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import pytz
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.session import SessionLocal
from app.core.config import settings, IS_DEV
from app.middleware.security import BlockExploitPathsMiddleware

ROMANIA_TZ = pytz.timezone("Europe/Bucharest")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🔧 Starting up RoBio Backend...")
    db = next(get_db())
    try:
        db.execute(text("SELECT 1"))
        print("✅ DB connection OK")
    except Exception as e:
        print(f"❌ DB connection failed: {e}")
        raise
    yield
    print("🧼 Shutting down RoBio Backend...")


app = FastAPI(
    title="RoBio Backend",
    version="0.1.0",
    docs_url="/docs" if IS_DEV else None,
    redoc_url="/redoc" if IS_DEV else None,
    openapi_url="/openapi.json" if IS_DEV else None,
    lifespan=lifespan,
)

# 🌐 CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔐 Bot/Exploit Protection Middleware
app.add_middleware(BlockExploitPathsMiddleware)


@app.get("/")
def root(db: Session = Depends(get_db)):
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    romania_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 3 * 3600))  # Simplified UTC+3
    return {
        "message": "RoBio backend is running.",
        "server_time_utc": server_time,
        "romania_time_estimate": romania_time,
        "env": settings.ENV
    }
