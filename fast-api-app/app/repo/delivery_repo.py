from db_executor import execute
from models import Delivery


def create_delivery(delivery: Delivery):
    return execute("INSERT INTO delivery_service.delivery"
                   "(title, sender_id, applier_id, status) "
                   "VALUES(%s, %s, %s, %s) RETURNING delivery_id;", (
                       delivery.title,
                       delivery.sender_id,
                       delivery.applier_id,
                       delivery.status
                   ))


def get_delivery_by_id(delivery_id: str):
    deliveries = []
    for tup in execute("SELECT "
                       "delivery_id, "
                       "title, "
                       "sender_id, "
                       "applier_id, "
                       "status, "
                       "insert_date, "
                       "update_date "
                       "FROM delivery_service.delivery "
                       "WHERE delivery_id = %s;", (delivery_id,)):
        delivery = Delivery()
        delivery.id = tup[0]
        delivery.title = tup[1]
        delivery.sender_id = tup[2]
        delivery.applier_id = tup[3]
        delivery.status = tup[4]
        delivery.insert_date = tup[5]
        delivery.update_date = tup[6]
        deliveries.append(delivery)
    if len(deliveries) == 1:
        return deliveries[0]
    else:
        return None


def get_delivery_by_applier_id_and_delivery_id(applier_id: str, delivery_id: str):
    deliveries = []
    for tup in execute("SELECT "
                       "delivery_id, "
                       "title, "
                       "sender_id, "
                       "applier_id, "
                       "status, "
                       "insert_date, "
                       "update_date "
                       "FROM delivery_service.delivery "
                       "WHERE applier_id = %s and delivery_id = %s;", (applier_id, delivery_id)):
        delivery = Delivery()
        delivery.id = tup[0]
        delivery.title = tup[1]
        delivery.sender_id = tup[2]
        delivery.applier_id = tup[3]
        delivery.status = tup[4]
        delivery.insert_date = tup[5]
        delivery.update_date = tup[6]
        deliveries.append(delivery)
    return deliveries


def get_delivery_by_sender_id_and_delivery_id(sender_id: str, delivery_id: str):
    deliveries = []
    for tup in execute("SELECT "
                       "delivery_id, "
                       "title, "
                       "sender_id, "
                       "applier_id, "
                       "status, "
                       "insert_date, "
                       "update_date "
                       "FROM delivery_service.delivery "
                       "WHERE sender_id = %s and delivery_id = %s;", (sender_id, delivery_id)):
        delivery = Delivery()
        delivery.id = tup[0]
        delivery.title = tup[1]
        delivery.sender_id = tup[2]
        delivery.applier_id = tup[3]
        delivery.status = tup[4]
        delivery.insert_date = tup[5]
        delivery.update_date = tup[6]
        deliveries.append(delivery)
    return deliveries
