from datetime import datetime
from pydantic import BaseModel, Field


class User(BaseModel):
    id: str | None = None
    login: str = Field(default=None)
    password: str = Field(default=None)
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    email: str = Field(default=None)
    insert_date: str | None = None
    update_date: str | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Delivery(BaseModel):
    id: str | None = None
    title: str = Field(default=None)
    sender_id: int
    applier_id: int
    status: str = Field(default=None)
    insert_date: datetime | None = None
    update_date: datetime | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Package(BaseModel):
    id: str | None = None
    title: str = Field(default=None)
    description: str = Field(default=None)
    delivery_id: int
    insert_date: datetime | None = None
    update_date: datetime | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
