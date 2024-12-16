from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .db import Base

class Realty(Base):
    __tablename__ = 'realties'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    address = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Numeric, index=False)

    negotiations = relationship('Negotiation', back_populates='realty')

class Negotiation(Base):
    __tablename__ = 'negotiation'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    score = Column(Numeric, index=False)
    income = Column(Numeric, index=False)
    risk_evaluation = Column(Boolean, index=False)
    realty_id = Column(Integer, ForeignKey('realties.id'))
    realty = relationship('Realty', back_populates='negotiations')