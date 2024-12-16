from sqlalchemy.orm import Session
from . import models, schemas, risk_evaluation

def get_negotiation(db: Session, negotiation_id: int):
    return db.query(models.Negotiation).filter(models.Negotiation.id == negotiation_id).first()

def get_realties(db: Session):
    return db.query(models.Realty).all()

def create_realty(db: Session, realty: schemas.RealtyCreate, negotiation: schemas.NegotiationCreate):
    db_realty = models.Realty(address=realty.address,
                              description=realty.description,
                              price=realty.price)
    db.add(db_realty)
    db.commit()
    db.refresh(db_realty)

    risk = risk_evaluation.evaluate_risk(realty.price, negotiation.score, negotiation.income)

    db_negotiation = models.Negotiation(
        score=negotiation.score,
        income=negotiation.income,
        risk_evaluation=risk,
        realty_id=db_realty.id
    )
    db.add(db_negotiation)
    db.commit()
    db.refresh(db_negotiation)


    return {
        "id": db_realty.id,
        "address": db_realty.address,
        "description": db_realty.description,
        "price": db_realty.price,
        "risk_evaluation": db_negotiation.risk_evaluation
    }
