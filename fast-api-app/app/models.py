from datetime import datetime
from pydantic import BaseModel, Field


class User(BaseModel):
    id: int | None = None
    login: str | None = None
    password: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    insert_date: datetime | None = None
    update_date: datetime | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = 0
        self.login = 'ivan'
        self.password = 'pass'
        self.first_name = 'Ivan'
        self.last_name = 'Ivanov'
        self.email = 'ivan.ivanov@mail.ru'
        self.insert_date = datetime.now()
        self.update_date = datetime.now()


class Delivery(BaseModel):
    id: int | None = None
    title: str | None = None
    sender_id: int | None = None
    applier_id: int | None = None
    status: str | None = None
    insert_date: datetime | None = None
    update_date: datetime | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = 0
        self.title = 'Delivery for new year'
        self.sender_id = 0
        self.applier_id = 0
        self.status = 'NEW'
        self.insert_date = datetime.now()
        self.update_date = datetime.now()


class Package(BaseModel):
    id: int | None = None
    title: str | None = None
    description: str | None = None
    delivery_id: int | None = None
    insert_date: datetime | None = None
    update_date: datetime | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = 0
        self.title = 'TV'
        self.description = 'Toshiba Ultra'
        self.delivery_id = 0
        self.insert_date = datetime.now()
        self.update_date = datetime.now()
