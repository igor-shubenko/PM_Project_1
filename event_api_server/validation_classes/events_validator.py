from pydantic import BaseModel, validator
from typing import Optional


class EventDataValidator(BaseModel):
    """Validates event info before create"""
    type: str
    name: str
    event_date: int
    score: str
    state: str

    @validator('event_date')
    def event_date_validator(cls, obj):
        if obj <= 0:
            raise ValueError("event_date must be greater than zero")
        return obj

    @validator('score')
    def score_validator(cls, obj):
        values = obj.split('-')
        if not values[0].isdigit() or not values[1].isdigit():
            raise ValueError("Score must be digits separated with '-'")
        return obj

    @validator('state')
    def event_state_validator(cls, obj):
        if obj != 'created':
            raise ValueError("wrong event state")
        return obj


class EventUpdateDataValidator(EventDataValidator):
    """Validates info before update"""
    type: Optional[str]
    name: Optional[str]
    event_date: Optional[int]
    score: Optional[str]
    state: Optional[str]

    @validator('state')
    def event_state_validator(cls, obj):
        if obj not in ['created', 'active', 'finished']:
            raise ValueError("wrong event state")
        return obj
