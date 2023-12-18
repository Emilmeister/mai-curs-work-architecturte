from fastapi import FastAPI, Response, status

from models import Package
from repo.package_repo import get_package_by_user_id, create_package

app = FastAPI()


# Создание посылки
#  Входные параметры: название посылки, описание, идентификатор пользователя
#  Выходные параметры: идентификатор посылки
@app.post("/package/create")
async def create(package: Package):
    return create_package(package)


# Получение посылок пользователя
#  Входные параметры: идентификатор пользователя
#  Выходные параметры: массив из посылок, где для каждой указан идентификатор, название, описание, дата создания.
@app.get("/package/list/{user_id}")
async def list(user_id: str):
    return get_package_by_user_id(user_id)
