from pydantic import BaseModel, validator
from typing import Optional


class BetDataValidator(BaseModel):
    date_created: int
    userId: int
    eventId: int
    market: str

    @validator('date_created')
    def date_created_validator(cls, obj):
        if obj <= 0:
            raise ValueError("date_created must be greater than zero")
        return obj

    @validator('userId')
    def userid_validator(cls, obj):
        if obj <= 0:
            raise ValueError("userId must be greater than zero")
        return obj

    @validator('eventId')
    def event_id_validator(cls, obj):
        if obj <= 0:
            raise ValueError("eventId must be greater than zero")
        return obj

    @validator('market')
    def market_validator(cls, obj):
        if obj not in ['team_1', 'team_2', 'draw']:
            raise ValueError("wrong market")
        return obj


class BetUpdateDataValidator(BetDataValidator):
    date_created: Optional[int]
    userId: Optional[int]
    eventId: Optional[int]
    eventId: Optional[int]
    market: Optional[str]

    @validator('market')
    def market_validator(cls, obj):
        if obj:
            raise ValueError("Can't change state")
        return obj
