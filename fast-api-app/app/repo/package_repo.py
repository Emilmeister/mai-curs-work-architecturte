from db_executor import execute
from models import Package


def create_package(package: Package):
    return execute("INSERT INTO delivery_service.package" +
                   "(title, description, delivery_id) " +
                   "VALUES(%s, %s, %s);", (
                       package.title,
                       package.description,
                       package.delivery_id,
                   ))


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
