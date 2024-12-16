from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import schemas, models, controller
from .db import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/imoveis", response_model=schemas.RealtyWithNegotiation)
async def realty_create(realty: schemas.RealtyCreate,
                        negotiation: schemas.NegotiationCreate,
                        db: Session = Depends(get_db)):
    realty_dict = controller.create_realty(db, realty, negotiation)

    return realty_dict


@app.get("/imoveis/{id}", response_model=schemas.RealtyWithRiskEvaluation)
async def get_realty(id: int, db: Session = Depends(get_db)):
    negotiation = controller.get_negotiation(db, id)
    if negotiation is None:
        raise HTTPException(status_code=404, detail="Negotiation not found")

    realty = db.query(models.Realty).filter(models.Realty.id == negotiation.realty_id).first()

    if realty is None:
        raise HTTPException(status_code=404, detail="Realty not found")

    return {**realty.__dict__, "risk_evaluation": negotiation.risk_evaluation}


@app.get("/imoveis", response_model=list[schemas.Realty])
async def realties_all(db: Session = Depends(get_db)):
    return controller.get_realties(db)
