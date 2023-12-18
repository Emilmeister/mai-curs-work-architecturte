from datetime import datetime
from pydantic import BaseModel, Field


class User(BaseModel):
    id: str | None = None
    login: str = Field(default=None)
    password: str = Field(default=None)
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    email: str = Field(default=None)
    insert_date: datetime | None = None
    update_date: datetime | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Delivery(BaseModel):
    id: str | None = None
    title: str | None = None
    sender_id: str | None = None
    applier_id: str | None = None
    status: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    insert_date: datetime | None = None
    update_date: datetime | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Package(BaseModel):
    id: str | None = None
    title: str | None = None
    description: str | None = None
    delivery_id: str | None = None
    sender_id: str | None = None
    applier_id: str | None = None
    insert_date: datetime | None = None
    update_date: datetime | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
