
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import AuditStat

app = FastAPI()

# 建立資料表（如果尚未存在）
Base.metadata.create_all(bind=engine)

# 依賴注入：取得 DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "CAEwatcher API is connected to Supabase"}

@app.get("/ranking")
def get_ranking(db: Session = Depends(get_db)):
    result = db.query(AuditStat).order_by(AuditStat.changes.desc()).all()
    return [{"company": r.company_name, "changes": r.changes} for r in result]
