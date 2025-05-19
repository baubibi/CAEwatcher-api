
from sqlalchemy import Column, Integer, String
from database import Base

class AuditStat(Base):
    __tablename__ = "audit_stats"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    changes = Column(Integer, nullable=False)
