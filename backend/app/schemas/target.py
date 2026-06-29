from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TargetCreate(BaseModel):
    domain: str
    project_id: int


class TargetUpdate(BaseModel):
    domain: str


class TargetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    domain: str
    project_id: int
    created_at: datetime
    