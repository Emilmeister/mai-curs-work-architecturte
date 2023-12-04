from fastapi import FastAPI, Response
from models import User
from db_executor import execute
import jwt
import random
import string


app = FastAPI()
jwt_encode_secret = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))


@app.post("/user/create")
async def create(user: User):
    execute("SHOW DATABASES;")
    user.first_name = '/user/create'
    return user


@app.get("/user/{login}")
async def get(login):
    user = User()
    user.first_name = '/user/:login'
    return user


@app.get("/user/filter/{surname_mask}/{name_mask}")
async def filtering(surname_mask, name_mask):
    user = User()
    user.first_name = '/user/filter/{surname_mask}/{name_mask}'
    return user


users = [User()]


@app.post("/auth/login")
async def login(user: User, response: Response):
    user_list = list(filter(lambda u: u.login == user.login and u.password == user.password, users))
    if len(user_list) == 1:
        db_user = user_list[0]
        return jwt.encode({
            'id': db_user.id,
            'login': db_user.login,
            'password': db_user.password,
            'first_name': db_user.first_name,
            'last_name': db_user.last_name,
            'email': db_user.email,
            'insert_date': db_user.insert_date.isoformat(),
        }, jwt_encode_secret, algorithm="HS256")
    else:
        response.status_code = 401


@app.post("/auth/check")
async def login(jwt_string: str):
    try:
        jwt_decoded = jwt.decode(jwt_string, jwt_encode_secret, algorithms=["HS256"])
        return {'user': jwt_decoded, 'success': True}
    except Exception:
        return {'user': None, 'success': False}
