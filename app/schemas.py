from pydantic import BaseModel

class RealtyBase(BaseModel):
    address: str
    description: str
    price: int

class RealtyCreate(RealtyBase):
    pass

class Realty(RealtyBase):
    id: int

    class Config:
        orm_mode = True

class NegotiationBase(BaseModel):
    score: int
    income: float

class NegotiationCreate(NegotiationBase):
    pass

class Negotiation(NegotiationBase):
    id: int
    risk_evaluation: bool

    class Config:
        orm_mode = True

class RealtyWithNegotiation(BaseModel):
    address: str
    description: str
    price: int
    id: int
    risk_evaluation: bool

    class Config:
        orm_mode = True

class RealtyWithRiskEvaluation(RealtyBase):
    id: int
    risk_evaluation: bool

    class Config:
        orm_mode = True
