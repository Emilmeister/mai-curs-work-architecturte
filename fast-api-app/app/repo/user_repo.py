from db_executor import execute
from models import User
import uuid


def filter_users(surname_mask: str, name_mask: str, db):
    users = []
    for tup in execute("SELECT "
                       "user_entity_id, "
                       "login, "
                       "first_name, "
                       "last_name, "
                       "email, "
                       "insert_date, "
                       "update_date "
                       "FROM delivery_service.user_entity " +
                       "WHERE last_name like CONCAT('%', %s, '%') "
                       "and first_name like CONCAT('%', %s, '%') /*sharding " + str(db) + "*/;", (surname_mask, name_mask)):
        user = User()
        user.id = tup[0]
        user.login = tup[1]
        user.first_name = tup[2]
        user.last_name = tup[3]
        user.email = tup[4]
        user.insert_date = tup[5]
        user.update_date = tup[6]
        users.append(user)
    return users


def get_user_by_login(login: str, db):
    users = []
    for tup in execute("SELECT "
                       "user_entity_id, "
                       "login, "
                       "first_name, "
                       "last_name, "
                       "email, "
                       "insert_date, "
                       "update_date "
                       "FROM delivery_service.user_entity " +
                       "WHERE login = %s /*sharding " + db + "*/;", (login,)):
        user = User()
        user.id = tup[0]
        user.login = tup[1]
        user.first_name = tup[2]
        user.last_name = tup[3]
        user.email = tup[4]
        user.insert_date = tup[5]
        user.update_date = tup[6]
        users.append(user)
    if len(users) == 1:
        return users[0]
    else:
        return None


def chooseDb(uuid_str: str):
    numbers_sum = sum(ord(char) for char in uuid_str)
    return numbers_sum % 2


def create_user(user: User):
    user_id = str(uuid.uuid4())
    db = chooseDb(user_id)
    print(db)
    return execute("INSERT INTO delivery_service.user_entity "
                   "(login, first_name, password, last_name, email) "
                   "VALUES(%s, %s, %s, %s, %s) RETURNING user_entity_id /*sharding " + str(db) + "*/;", (
                       user.login,
                       user.password,
                       user.first_name,
                       user.last_name,
                       user.email
                   ))
