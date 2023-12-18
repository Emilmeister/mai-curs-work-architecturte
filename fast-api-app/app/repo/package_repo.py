from db_executor import execute
from models import Package, Delivery
import httpx


def create_package(package: Package):
    delivery = get_delivery_by_id(package.delivery_id)
    return execute("INSERT INTO delivery_service.package" +
                   "(title, description, delivery_id, sender_id, applier_id) " +
                   "VALUES(%s, %s, %s, %s, %s) RETURNING package_id;", (
                       package.title,
                       package.description,
                       package.delivery_id,
                       delivery.sender_id,
                       delivery.applier_id
                   ))


def get_delivery_by_id(delivery_id):
    url = "http://fast-api-delivery:82/delivery/get_by_id/" + delivery_id
    response = httpx.post(url)
    if response.status_code == 200:
        response_model = Delivery(**response.json())
        return response_model
    else:
        print(f"Error {response.status_code}: {response.text}")

def get_package_by_user_id(user_id: str):
    packages = []
    for tup in execute("SELECT "
                       "package_id, "
                       "title, "
                       "description, "
                       "delivery_id, "
                       "sender_id, "
                       "applier_id, "
                       "insert_date, "
                       "update_date "
                       "FROM delivery_service.package "
                       "WHERE applier_id = %s;", (user_id,)):
        package = Package()
        package.id = tup[0]
        package.title = tup[1]
        package.description = tup[2]
        package.delivery_id = tup[3]
        package.sender_id = tup[4]
        package.applier_id = tup[5]
        package.insert_date = tup[6]
        package.update_date = tup[6]
        packages.append(package)
    return packages
