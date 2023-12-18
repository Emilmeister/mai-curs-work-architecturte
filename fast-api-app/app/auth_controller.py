from fastapi import FastAPI, Response, status
from models import User
from repo.user_repo import filter_users, get_user_by_login, create_user
import jwt
import random
import string

app = FastAPI()
jwt_encode_secret = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))


@app.post("/user/create")
async def create(user: User):
    return create_user(user)


@app.get("/user/{login}")
async def get(login):
    return get_user_by_login(login)


@app.get("/user/filter/{surname_mask}/{name_mask}")
async def filtering(surname_mask, name_mask):
    user = User()
    user.first_name = '/user/filter/{surname_mask}/{name_mask}'
    return filter_users(surname_mask, name_mask)


users = [User()]


@app.post("/auth/login")
async def login(user: User, response: Response):
    print(user)
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
        response.status_code = status.HTTP_401_UNAUTHORIZED


@app.post("/auth/check")
async def login_in(jwt_string: str):
    try:
        jwt_decoded = jwt.decode(jwt_string, jwt_encode_secret, algorithms=["HS256"])
        return {'user': jwt_decoded, 'success': True}
    except Exception:
        return {'user': None, 'success': False}
