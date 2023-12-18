from fastapi import FastAPI, Response, status

from models import Delivery
from repo.delivery_repo import create_delivery, get_delivery_by_applier_id_and_delivery_id, \
    get_delivery_by_sender_id_and_delivery_id, get_delivery_by_id

app = FastAPI()


# Создание доставки от пользователя к пользователю
# Входные параметры: идентификатор отправителя, идентификатор получаеля, дата отправки, дата получения, массив идентификаторов посылок.
# Выходные параметры: идентификатор доставки
@app.post("/delivery/create")
async def create(delivery: Delivery):
    return create_delivery(delivery)


# Получение информации о доставке по получателю
# Входные параметры: идентификатор получателя, идентификатор доставки
# Выходные параметры: идентификатор доставки, идентификатор получателя, идентификатор отправителя, дата отправки, дата получения, статус, массив идентификаторов посылок.
@app.post("/delivery/applier/{applier_id}/{delivery_id}")
async def info_by_applier(applier_id, delivery_id):
    return get_delivery_by_applier_id_and_delivery_id(applier_id, delivery_id)


# Получение информации о доставке по отправителю
# Входнае параметры: идентификатор отправителю, идентификатор доставки
# Выходные парамтеры: идентификатор доставки, идентификатор получателя, идентификатор отправителя, дата отправки, дата получения, статус, массив идентификаторов посылок.
@app.post("/delivery/sender/{sender_id}/{delivery_id}")
async def info_by_sender(sender_id, delivery_id):
    return get_delivery_by_sender_id_and_delivery_id(sender_id, delivery_id)

@app.post("/delivery/get_by_id/{delivery_id}")
async def info_by_sender(delivery_id):
    return get_delivery_by_id(delivery_id)
